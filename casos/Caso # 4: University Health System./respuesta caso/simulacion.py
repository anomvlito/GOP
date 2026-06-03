# -*- coding: utf-8 -*-
"""
Simulacion de eventos discretos — University Health Services, Walk-In Clinic (Caso 4).
=====================================================================================

Modulo atomico y autocontenido (solo libreria estandar). Reproduce un dia de operacion
de la clinica bajo el sistema de triage y permite comparar escenarios.

Modelo
------
  Llegada -> [Triage: 2 coordinadoras, U(3,4) min]
          -> con prob. p_np a Enfermeras Practicantes (NP), si no a Medicos (MD)
  MD: servicio Exp(media 60/3.1 = 19.35 min);  NP: Exp(media 60/1.8 = 33.33 min).
  5% de los pacientes NP son referidos despues a un MD (Exhibit 4 / texto del caso).
  24% de los pacientes pide un proveedor especifico -> queda atado a UN servidor
  (no aprovecha el pooling), lo que alarga su espera.

Decisiones de modelado (correctas y documentadas)
-------------------------------------------------
  * Llegadas: proceso de Poisson NO homogeneo con tasa constante por hora (Exhibit 2).
    Se generan por hora con N_h ~ Poisson(lambda_h) y tiempos Uniformes dentro de la hora
    (exacto; evita el sesgo por truncar la ultima interllegada de cada hora).
  * Capacidad por hora (Exhibit 4): el dia promedio usa el PROMEDIO real de lunes a
    viernes por tramo (no el horario del lunes). Las dotaciones fraccionarias (p.ej. 2.5
    medicos) se resuelven con REDONDEO ALEATORIO insesgado por replica, de modo que la
    capacidad esperada coincide con la del analisis analitico (28.1 h-MD el dia promedio).
  * Turnos: el numero de servidores activos cambia hora a hora. Un servidor ocupado al
    cambiar de turno TERMINA su paciente (sin preempcion) pero no toma nuevos si sale de
    turno. El personal permanece despues de las 18:00 hasta drenar la cola.
  * Especificos: al salir de triage el paciente se ata a un servidor concreto (elegido
    al azar entre los de turno). Si ese servidor sale de turno de forma permanente, el
    paciente cae a la cola general (no se pierde).
  * Numeros aleatorios comunes (CRN): las llegadas y la capacidad de cada replica usan
    una semilla dependiente solo de la replica, identica entre escenarios, para que las
    diferencias observadas se deban al cambio de politica y no al ruido muestral.

Salida
------
  Espera media en triage, espera media para MD, espera media para NP, y "rezagados/dia"
  (pacientes aun en el sistema a las 18:00, i.e. cuya atencion termina despues de las
  600 min). Util porque, con utilizacion > 100%, el modelo analitico M/M/c daria espera
  infinita; la simulacion captura la sobrecarga transitoria real.
"""

import heapq
import math
import random
from collections import deque

# --------------------------------------------------------------------- Parametros
OPEN_MIN = 0.0          # 8:00 AM
LAST_ADMIT = 570.0      # 5:30 PM (ultima admision)
CLOSE_MIN = 600.0       # 6:00 PM (el personal se queda hasta drenar)
N_HOURS = 10            # tramos horarios 8-9 ... 17-18
N_TRIAGE = 2            # coordinadoras de triage

MU_MD, MU_NP = 3.1, 1.8                 # pacientes/hora
ST_MD, ST_NP = 60.0 / MU_MD, 60.0 / MU_NP   # min/paciente (19.35 y 33.33)
TRIAGE_LO, TRIAGE_HI = 3.0, 4.0         # min, Uniforme
P_REFERRAL = 0.05                       # NP -> MD

# Llegadas promedio por hora (Exhibit 2); el lunes escala por 163/143.
ARR_RATES = [18.2, 17.6, 16.8, 15.2, 11.8, 16.9, 16.2, 15.9, 11.6, 2.8]
MONDAY_FACTOR = 163.0 / 143.0

# Dotacion MD por tramo (Exhibit 4). Promedio real lunes-viernes vs. horario del lunes.
MD_AVG = [2.0, 2.5, 4.8, 3.4, 2.6, 2.7, 3.4, 4.0, 2.7, 1.0]
MD_MON = [2.0, 2.5, 5.0, 3.0, 3.0, 3.0, 3.0, 4.0, 3.0, 1.0]
# Dotacion NP por tramo: identica de lunes a viernes en el Exhibit 4.
NP_ALL = [2.0, 4.0, 4.0, 4.0, 2.5, 2.5, 4.0, 4.0, 2.5, 2.0]


def hour_of(t):
    """Indice de tramo horario [0..9] para el instante t (min). Clampa al ultimo tramo."""
    h = int(t // 60.0)
    return 9 if h > 9 else h


def poisson(rng, lam):
    """Muestra Poisson(lam) por el metodo de Knuth."""
    if lam <= 0:
        return 0
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        k += 1
        p *= rng.random()
        if p <= L:
            return k - 1


def resolve_capacity(frac_sched, rng):
    """Redondeo aleatorio insesgado de una dotacion fraccionaria a enteros (>=1)."""
    out = []
    for v in frac_sched:
        base = int(math.floor(v))
        extra = 1 if rng.random() < (v - base) else 0
        out.append(max(1, base + extra))
    return out


def generate_arrivals(rng, monday_factor):
    """Tiempos de llegada de un dia (Poisson no homogeneo, exacto por tramo)."""
    arrivals = []
    for h in range(N_HOURS):
        lam = ARR_RATES[h] * monday_factor
        for _ in range(poisson(rng, lam)):
            t = (h + rng.random()) * 60.0
            if t <= LAST_ADMIT:
                arrivals.append(t)
    arrivals.sort()
    return arrivals


class Patient:
    __slots__ = ("arr", "qentry", "dest", "specific", "referred", "depart")

    def __init__(self, arr):
        self.arr = arr
        self.qentry = arr
        self.dest = "MD"
        self.specific = False
        self.referred = False
        self.depart = None


def make_pool(cap, service_fn):
    """Pool de servidores con turnos por hora, cola general y colas por servidor (especificos)."""
    mc = max(cap)
    return {
        "cap": cap,                       # enteros por tramo horario
        "free": [True] * mc,              # servidor libre?
        "occ": [None] * mc,               # paciente en cada servidor
        "sq": [deque() for _ in range(mc)],  # cola especifica por servidor
        "gq": deque(),                    # cola general (pooling)
        "svc": service_fn,
        "wsum": 0.0, "wn": 0,             # acumuladores de espera
    }


def run_day(md_frac, np_frac, monday_factor, p_np, p_specific, rep):
    """Simula un dia y devuelve (sum/n espera triage, MD, NP, rezagados)."""
    rng_a = random.Random(rep)               # llegadas + capacidad (comun entre escenarios)
    rng_s = random.Random(100003 + rep)      # ruteo + servicios (CRN parcial)

    md_cap = resolve_capacity(md_frac, rng_a)
    np_cap = resolve_capacity(np_frac, rng_a)
    arrivals = generate_arrivals(rng_a, monday_factor)

    T = make_pool([N_TRIAGE] * N_HOURS, lambda: rng_s.uniform(TRIAGE_LO, TRIAGE_HI))
    MD = make_pool(md_cap, lambda: rng_s.expovariate(1.0 / ST_MD))
    NP = make_pool(np_cap, lambda: rng_s.expovariate(1.0 / ST_NP))
    pools = {"T": T, "MD": MD, "NP": NP}

    heap = []
    seq = [0]

    def push(t, kind, *data):
        heapq.heappush(heap, (t, seq[0], kind, data))
        seq[0] += 1

    def enqueue(tag, p, t):
        pool = pools[tag]
        if p.specific and tag != "T":
            r0 = rng_s.randrange(pool["cap"][hour_of(t)])
            pool["sq"][r0].append(p)
        else:
            pool["gq"].append(p)

    def start(tag, r, p, t):
        pool = pools[tag]
        pool["free"][r] = False
        pool["occ"][r] = p
        pool["wsum"] += t - p.qentry
        pool["wn"] += 1
        p.depart = t + pool["svc"]()
        push(p.depart, "done", tag, r)

    def dispatch(tag, t):
        pool = pools[tag]
        ch = pool["cap"][hour_of(t)]
        # especificos: cada servidor de turno atiende su propia cola
        for r in range(ch):
            if pool["free"][r] and pool["sq"][r]:
                start(tag, r, pool["sq"][r].popleft(), t)
        # generales: cualquier servidor de turno libre toma de la cola comun
        for r in range(ch):
            if pool["free"][r] and pool["gq"]:
                start(tag, r, pool["gq"].popleft(), t)

    def rescue_offshift(tag, t):
        """Especificos atados a un servidor fuera de turno caen a la cola general."""
        pool = pools[tag]
        ch = pool["cap"][hour_of(t)]
        for r in range(ch, len(pool["sq"])):
            while pool["sq"][r]:
                pool["gq"].append(pool["sq"][r].popleft())

    departures = []

    # eventos iniciales: llegadas y cambios de turno
    for a in arrivals:
        push(a, "arrival", Patient(a))
    for h in range(1, N_HOURS):
        push(h * 60.0, "shift")

    while heap:
        t, _, kind, data = heapq.heappop(heap)

        if kind == "arrival":
            p = data[0]
            p.dest = "NP" if rng_s.random() < p_np else "MD"
            p.specific = rng_s.random() < p_specific
            p.referred = (p.dest == "NP") and (rng_s.random() < P_REFERRAL)
            p.qentry = t
            enqueue("T", p, t)
            dispatch("T", t)

        elif kind == "done":
            tag, r = data
            pool = pools[tag]
            p = pool["occ"][r]
            pool["occ"][r] = None
            pool["free"][r] = True

            if tag == "T":
                p.qentry = t
                enqueue(p.dest, p, t)
                dispatch(p.dest, t)
                dispatch("T", t)
            elif tag == "NP" and p.referred:
                p.qentry = t
                p.specific = False           # la referencia entra como general
                enqueue("MD", p, t)
                dispatch("MD", t)
                dispatch("NP", t)
            else:
                departures.append(p.depart)
                dispatch(tag, t)

        else:  # shift
            for tag in ("MD", "NP"):
                rescue_offshift(tag, t)
                dispatch(tag, t)
            dispatch("T", t)

    rez = sum(1 for d in departures if d > CLOSE_MIN)
    return (T["wsum"], T["wn"], MD["wsum"], MD["wn"],
            NP["wsum"], NP["wn"], rez, len(arrivals))


def simulate(label, md_frac, monday_factor, p_np, p_specific, reps):
    tw = tn = mw = mn = nw = nn = rez = npat = 0.0
    for rep in range(reps):
        a, b, c, d, e, f, g, n = run_day(md_frac, NP_ALL, monday_factor,
                                         p_np, p_specific, rep)
        tw += a; tn += b; mw += c; mn += d; nw += e; nn += f; rez += g; npat += n
    return {
        "label": label,
        "triage": tw / tn if tn else 0.0,
        "md": mw / mn if mn else 0.0,
        "np": nw / nn if nn else 0.0,
        "rez": rez / reps,
        "pacientes": npat / reps,
    }


if __name__ == "__main__":
    REPS = 3000
    print(f"Simulacion UHS Walk-In Clinic  |  {REPS} replicas por escenario\n")
    print(f"{'Escenario':<34}{'Triage':>9}{'Esp.MD':>9}{'Esp.NP':>9}"
          f"{'Rezag/dia':>11}{'Pac/dia':>9}")
    print("-" * 81)

    DAYS = [("Dia promedio", MD_AVG, 1.0), ("Lunes (punta)", MD_MON, MONDAY_FACTOR)]
    SCEN = [
        ("Base",            0.33, 0.24),
        ("Sol.1 pooling",   0.33, 0.00),   # se elimina la peticion de medico especifico
        ("Sol.2 NP 50%",    0.50, 0.24),   # se amplian las guias clinicas de las NP
    ]

    for day_label, md_frac, mf in DAYS:
        for sc_label, p_np, p_spec in SCEN:
            r = simulate(f"{day_label} - {sc_label}", md_frac, mf, p_np, p_spec, REPS)
            print(f"{r['label']:<34}{r['triage']:>8.2f} {r['md']:>8.2f} "
                  f"{r['np']:>8.2f} {r['rez']:>10.2f} {r['pacientes']:>8.1f}")
        print("-" * 81)

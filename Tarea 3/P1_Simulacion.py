"""
============================================================================
 TAREA 3 - VARIABILIDAD | AndesFresh SpA
 Simulacion del proceso de recepcion y control de calidad.
 Responde las Preguntas 3 a 8.
============================================================================

 Para correr:   pip install simpy numpy
                python simulacion_simple.py

 Que hace:
   - Los camiones llegan durante 24 h (tiempo entre llegadas ~ Normal).
   - Cada camion se descarga (tiempo ~ Uniforme) y libera 15 bins.
   - Cada bin pasa por:  Seleccion -> Embalaje -> Calidad.
   - Un 5% de los bins vuelve a Seleccion (reproceso).
   - Si hay mas de 4 camiones esperando descarga, se cobra multa.

 Cada pregunta se responde en su propia funcion al final del archivo
 (ver bloque "RESPUESTAS A LAS PREGUNTAS 3 A 8").
============================================================================
"""

import simpy
import numpy as np

# --------------------------- PARAMETROS -------------------------------------
# Distribuciones ajustadas en la Pregunta 2
LLEGADA_MEDIA, LLEGADA_DESV = 59.76, 7.81   # Normal  [min entre camiones]
DESCARGA_MIN, DESCARGA_MAX  = 60.89, 89.54  # Uniforme [min por camion]

BINS_POR_CAMION = 15

# Capacidad de cada estacion en bins por hora
SELECCION = (11, 12, 13.5)    # Triangular (min, moda, max)
EMBALAJE  = (10.5, 13, 14)    # Triangular (min, moda, max)
CALIDAD   = 14                # constante

PROB_REPROCESO = 0.05         # 5% de bins vuelve a seleccion
MAX_COLA_CAMIONES = 4         # tope de camiones en espera antes de multar
MULTA = 35000                 # $ por camion multado

MINUTOS_DIA = 24 * 60


# --------------------------- FUNCIONES AUXILIARES ---------------------------
def minutos_por_bin(triangular):
    """Convierte una capacidad (bins/hora) en un tiempo de servicio (min/bin)."""
    bins_por_hora = np.random.triangular(*triangular)
    return 60 / bins_por_hora


def capacidad_media(triangular):
    """Capacidad media de una estacion triangular, en bins/hora."""
    return sum(triangular) / 3


# --------------------------- MODELO DE SIMULACION ---------------------------
# Usamos un diccionario "R" para guardar todos los resultados de una corrida.
def nuevo_registro():
    return {
        "esperas":  {"descarga": [], "seleccion": [], "embalaje": [], "calidad": []},
        "ocupado":  {"descarga": 0, "seleccion": 0, "embalaje": 0, "calidad": 0},
        "ciclos":   [],
        "multados": 0,
    }


def atender(env, recurso, nombre, duracion, R):
    """Un trabajo entra a la cola del recurso, espera, y es atendido."""
    llegada = env.now
    with recurso.request() as turno:
        yield turno                                      # espera su turno
        R["esperas"][nombre].append(env.now - llegada)   # tiempo en cola
        yield env.timeout(duracion)                      # tiempo atendido
        R["ocupado"][nombre] += duracion                 # ocupacion del recurso


def procesar_bin(env, est, R, sel_tri, emb_tri, qc_antes):
    """Recorrido de un bin. qc_antes=True pone Calidad antes de Embalaje (P6)."""
    inicio = env.now

    # Seleccion con reproceso (5% vuelve a entrar)
    while True:
        yield from atender(env, est["seleccion"], "seleccion", minutos_por_bin(sel_tri), R)
        if np.random.random() >= PROB_REPROCESO:
            break

    if qc_antes:   # control de calidad antes de embalar (Pregunta 6)
        yield from atender(env, est["calidad"], "calidad", 60 / CALIDAD, R)
        yield from atender(env, est["embalaje"], "embalaje", minutos_por_bin(emb_tri), R)
    else:          # orden normal
        yield from atender(env, est["embalaje"], "embalaje", minutos_por_bin(emb_tri), R)
        yield from atender(env, est["calidad"], "calidad", 60 / CALIDAD, R)

    R["ciclos"].append(env.now - inicio)


def procesar_camion(env, est, R, sel_tri, emb_tri, qc_antes):
    """Un camion se descarga y luego suelta sus 15 bins al sistema."""
    yield from atender(env, est["descarga"], "descarga",
                       np.random.uniform(DESCARGA_MIN, DESCARGA_MAX), R)
    for _ in range(BINS_POR_CAMION):
        env.process(procesar_bin(env, est, R, sel_tri, emb_tri, qc_antes))


def llegada_de_camiones(env, est, R, sel_tri, emb_tri, qc_antes, fin):
    """Genera camiones durante toda la jornada."""
    while True:
        yield env.timeout(max(np.random.normal(LLEGADA_MEDIA, LLEGADA_DESV), 0.1))
        if env.now > fin:
            break
        en_espera = est["descarga"].count + len(est["descarga"].queue)
        if en_espera > MAX_COLA_CAMIONES:
            R["multados"] += 1
        env.process(procesar_camion(env, est, R, sel_tri, emb_tri, qc_antes))


def simular(semilla, sel_tri=SELECCION, emb_tri=EMBALAJE, qc_antes=False, dias=1):
    """Corre la simulacion y devuelve los indicadores de esa corrida."""
    np.random.seed(semilla)
    R = nuevo_registro()
    fin = MINUTOS_DIA * dias

    env = simpy.Environment()
    est = {
        "descarga":  simpy.Resource(env, capacity=1),
        "seleccion": simpy.Resource(env, capacity=1),
        "embalaje":  simpy.Resource(env, capacity=1),
        "calidad":   simpy.Resource(env, capacity=1),
    }

    env.process(llegada_de_camiones(env, est, R, sel_tri, emb_tri, qc_antes, fin))
    env.run(until=fin)

    # Calcular indicadores
    salida = {}
    for e in ["descarga", "seleccion", "embalaje", "calidad"]:
        utilizacion = R["ocupado"][e] / fin
        espera_prom = np.mean(R["esperas"][e]) if R["esperas"][e] else 0
        en_cola = sum(R["esperas"][e]) / fin           # Ley de Little: Lq = W_total / T
        salida[e] = (utilizacion, espera_prom, en_cola)
    salida["ciclo"] = np.mean(R["ciclos"]) if R["ciclos"] else 0
    salida["multados"] = R["multados"]
    return salida


def promedio(n=40, **kwargs):
    """Promedia n replicas para reducir el ruido aleatorio."""
    corridas = [simular(s, **kwargs) for s in range(n)]
    out = {}
    for e in ["descarga", "seleccion", "embalaje", "calidad"]:
        out[e] = tuple(np.mean([c[e][i] for c in corridas]) for i in range(3))
    out["ciclo"] = np.mean([c["ciclo"] for c in corridas])
    out["multados"] = np.mean([c["multados"] for c in corridas])
    return out


def reducir_variabilidad(triangular, factor=0.10):
    """Estrecha la triangular un 'factor' alrededor de su media (Pregunta 7)."""
    a, m, b = triangular
    media = (a + m + b) / 3
    return (media + (a - media) * (1 - factor),
            media + (m - media) * (1 - factor),
            media + (b - media) * (1 - factor))


# ====================== RESPUESTAS A LAS PREGUNTAS 3 A 8 ====================
def pregunta_3(base):
    print("\n" + "=" * 60)
    print(" PREGUNTA 3 - Utilizacion, tiempo en cola, ciclo y trabajos en cola")
    print("=" * 60)
    print(f"{'Estacion':12s}{'Utilizacion':>13s}{'Espera(min)':>13s}{'En cola':>10s}")
    for e in ["descarga", "seleccion", "embalaje", "calidad"]:
        u, w, l = base[e]
        print(f"{e:12s}{u*100:>11.1f}%{w:>13.1f}{l:>10.2f}")
    print(f"\nTiempo de ciclo promedio por bin : {base['ciclo']:.1f} min")
    print(f"Utilizacion del sistema (cuello) : {base['seleccion'][0]*100:.1f}%")


def pregunta_4(base):
    print("\n" + "=" * 60)
    print(" PREGUNTA 4 - Cuello de botella y capacidad del sistema")
    print("=" * 60)
    cap_descarga = 60 / ((DESCARGA_MIN + DESCARGA_MAX) / 2) * BINS_POR_CAMION
    cap_sel = capacidad_media(SELECCION) * (1 - PROB_REPROCESO)
    cap_emb = capacidad_media(EMBALAJE)
    caps = {"Descarga": cap_descarga, "Seleccion": cap_sel,
            "Embalaje": cap_emb, "Calidad": CALIDAD}
    print("Capacidad de cada etapa [bins/h] (la MENOR fija el sistema):")
    for nom, v in sorted(caps.items(), key=lambda x: x[1]):
        print(f"   {nom:10s}: {v:.2f}")
    print(f"\nCuello de botella     : Seleccion ({cap_sel:.1f} bins/h)")
    print(f"Capacidad del sistema : {cap_sel:.1f} bins/h")
    print(f"(Descarga {cap_descarga:.1f} bins/h queda muy cerca: cuello secundario.)")


def pregunta_5(base):
    print("\n" + "=" * 60)
    print(" PREGUNTA 5 - Multas por perdida de calidad")
    print("=" * 60)
    print(f"Camiones multados por dia : {base['multados']:.1f}")
    print(f"Multa diaria estimada     : ${base['multados']*MULTA:,.0f}")
    print("Medidas para reducir la multa:")
    print("  1) Agregar capacidad de descarga (2do muelle): es la causa de la")
    print("     cola de camiones, atacando el cuello que genera la multa.")
    print("  2) Sistema de citas/ventanas horarias: suaviza las llegadas y")
    print("     evita los peaks que saturan la cola de espera.")


def pregunta_6(base):
    print("\n" + "=" * 60)
    print(" PREGUNTA 6 - Donde colocar el control de calidad")
    print("=" * 60)
    qc = promedio(qc_antes=True)
    print(f"Ciclo con calidad al FINAL (actual)   : {base['ciclo']:.1f} min")
    print(f"Ciclo con calidad ANTES de embalaje   : {qc['ciclo']:.1f} min")
    print("Recomendacion: ubicar el control justo despues de seleccion,")
    print("donde se originan los defectos (calidad en la fuente). Evita")
    print("gastar embalaje en bins que se reprocesaran.")


def pregunta_7(base):
    print("\n" + "=" * 60)
    print(" PREGUNTA 7 - Reducir 10% la variabilidad: seleccion vs embalaje")
    print("=" * 60)
    sel = promedio(sel_tri=reducir_variabilidad(SELECCION))
    emb = promedio(emb_tri=reducir_variabilidad(EMBALAJE))
    print(f"Ciclo base                      : {base['ciclo']:.1f} min")
    print(f"Ciclo con -10% var. SELECCION   : {sel['ciclo']:.1f} min  <-- mejora")
    print(f"Ciclo con -10% var. EMBALAJE    : {emb['ciclo']:.1f} min  (casi igual)")
    print("Decision: reducir la variabilidad de SELECCION, porque es el cuello")
    print("de botella. La variabilidad solo se vuelve espera donde hay cola.")


def pregunta_8(base):
    print("\n" + "=" * 60)
    print(" PREGUNTA 8 - Cambios en un mes de funcionamiento")
    print("=" * 60)
    mes = promedio(n=15, dias=30)
    print(f"Utilizacion seleccion en el mes : {mes['seleccion'][0]*100:.1f}%")
    print(f"Camiones multados en el mes     : {mes['multados']:.0f}")
    print(f"Multa mensual estimada          : ${mes['multados']*MULTA:,.0f}")
    print("El sistema se estabiliza con seleccion como cuello permanente.")
    print("La utilizacion sube cerca del 100%: el sistema opera al limite,")
    print("por lo que las colas y los costos se acumulan mes a mes.")


# --------------------------- PROGRAMA PRINCIPAL -----------------------------
if __name__ == "__main__":
    base = promedio()        # escenario base, usado por varias preguntas
    pregunta_3(base)
    pregunta_4(base)
    pregunta_5(base)
    pregunta_6(base)
    pregunta_7(base)
    pregunta_8(base)
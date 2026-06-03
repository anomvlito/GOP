# Ayudantía 7 - Variabilidad

**Pontificia Universidad Católica de Chile**  
**Escuela de Ingeniería**  
**Departamento de Ingeniería Industrial y de Sistemas**  
**ICS3213: Gestión de Operaciones**  
*Profesores: Alejandro Mac Cawley - Rodrigo Carrasco*  
*Semestre: Primer Semestre 2026*  
*Ayudante: Alonso Parada Frigerio (alonso.parada@uc.cl)*  

---

## Problema 1 (Teoría de Colas M/M/1)

Un promedio de 10 automóviles por hora llegan a un cajero con un solo servidor que proporciona un servicio sin que los clientes desciendan del automóvil. Suponga que el tiempo de ciclo promedio por cada cliente es de 4 minutos, y que tanto los tiempos entre llegadas como los tiempos de servicio son exponenciales.

Determine:
1.  **¿Cuál es la probabilidad de que el cajero esté ocioso?**
2.  **¿Cuál es el número promedio de autos que están en la cola del cajero?** *(Considere que un automóvil que está siendo atendido no está en la cola esperando)*.
3.  **¿Cuál es la cantidad promedio de tiempo que un cliente pasa en el sistema** *(incluyendo el tiempo de servicio)?*
4.  **¿Cuántos clientes atenderá en promedio el cajero por hora?**

---

## Problema 2 (Redes de Colas G/G/1 en Serie)

Usted es el encargado de la mesa de ayuda de una prestigiosa empresa de software. Su mesa de ayuda recibe 2 tipos de tickets: simples y complejos. Los tickets simples son resueltos directamente por cada técnico en el teléfono. No obstante, los tickets complejos son derivados a una área especialista. 

El área especialista en resolver tickets complejos consta de 2 etapas ($E_1$ y $E_2$), cada una de estas tiene un buffer ($B_1$ y $B_2$ respectivamente), en los cuales los clientes pueden quedar en espera.

*   Los tickets llegan a $B_1$ a una tasa de $12\text{ tickets/hora}$ con una distribución $G/G/1$ y tienen un coeficiente de variación entre tiempos de llegada de $c_a = 1.1$.
*   La etapa $E_1$ tiene un tiempo medio de procesamiento de 4 minutos con un coeficiente de variación de $c_{e1} = 0.7$.
*   La etapa $E_2$ tiene un tiempo medio de procesamiento de 4.2 minutos con un coeficiente de variación de $c_{e2} = 1$.
*   La capacidad de los buffers es infinita.

Determine el **tiempo total de ciclo** y el **largo medio de las colas**.

---

## Problema 3 (Líneas de Producción y Kingman)

Considere el siguiente proceso productivo en serie de dos etapas:

$$\text{Materia Prima} \rightarrow \text{Buffer 1} \rightarrow \text{Proceso 1} \rightarrow \text{Buffer 2} \rightarrow \text{Proceso 2} \rightarrow \text{Producto Terminado}$$

*   El **Proceso 1** tiene un tiempo de proceso de $21\text{ minutos por trabajo}$.
*   El **Proceso 2** procesa $3\text{ productos por hora}$.
*   Ambos procesos tienen un coeficiente de variación cuadrático de $c^2 = 1$ para cada unidad producida (distribución exponencial).
*   La capacidad máxima del buffer es ilimitada. No hay restricciones de insumos ni de bodegaje de productos terminados.

### Preguntas
1.  Con esta información determine:
    *   ¿Cuál es el throughput en la cola?
    *   ¿Cuál es el throughput del proceso completo?
    *   ¿Cuántas unidades se encuentran en proceso ($WIP$)?
    *   ¿Cuál es el tiempo de ciclo total (no incluyendo el tiempo en insumos)?
    *   ¿Cuál es el Work in Process en el buffer ($WIPP$)?
2.  Para la situación inicial (no hay límite en la espera) usted se percata de que el proceso no sigue una distribución de procesos exponencial, sino que más bien una distribución general. ¿Cómo cambian los indicadores del proceso? ¿Es mejor o peor que el proceso tenga distribución general?

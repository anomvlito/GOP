       Pontificia Universidad Católica de Chile
       Departamento de Ingeniería Industrial y Sistemas
       ICS3213 Gestión de Operaciones
       Profesores: Alejandro Mac Cawley – Isabel Alarcón




                                    Guía de Ejercicios de Bodegas

Gonzalo Vargas (grvargas@uc.cl)

Problema 1

Usted está diseñando una bodega de pallets a piso cuyos pasillos son de 4,2 m de ancho.
Los pallets son de 1,2 m x 1 m y se ubican con la cara más angosta hacia el pasillo. Asuma
que cada SKU tiene una demanda constante y es reordenado de acuerdo al ciclo de pedido a
continuación:

            Cantidad de pallets
SKU                                        Altura de apilado (pallets) Ciclo de pedido (semanas)
                 pedidos
  A                32                                       1                     5
  B                28                                       2                     4
  C                14                                       3                     6


a) Para cada SKU determine la profundidad óptima para ser guardado.

b) Para todas las SKU, determine una profundidad óptima única.

Solución:

a) Usando la formula:

                                                                𝑎 𝑞%
                                                  𝑝𝑟𝑜𝑓% =
                                                                2 𝑧%

                                               𝑎𝑛𝑐ℎ𝑜 𝑝𝑎𝑠𝑖𝑙𝑙𝑜
                                            𝑎=
                                                𝑎𝑛𝑐ℎ𝑜 𝑝𝑎𝑙𝑙𝑒𝑡
                                        𝑞% = 𝑐𝑎𝑛𝑡𝑖𝑑𝑎𝑑 𝑜𝑟𝑑𝑒𝑛𝑎𝑑𝑎

                                          𝑧% = 𝑎𝑙𝑡𝑢𝑟𝑎 𝑑𝑒 𝑝𝑎𝑙𝑙𝑒𝑡𝑠

*Recordar que la cara más angosta del pallet está hacia al pasillo, y para calcular 𝑎 se usa el
largo de la otra cara.
Tenemos los resultados:

SKU Profundidad
 A      7,48
 B      4,95
 C      2,86
*Las profundidades son en número de pallets.

b) Ahora, en caso de establecer solo una profundidad para todos los SKU, calculamos la
profundidad óptima de la siguiente forma:

                                                      7
                                             𝑎   1         𝑞%
                                𝑝𝑟𝑜𝑓 =
                                             2   𝑛         𝑧%
                                                     %89


En esta parte, como el ciclo de pedido es distinto para cada SKU, debemos encontrar un
mínimo común múltiplo para los ciclos, en este caso 60, y ponderar de acuerdo a eso. Si
todos tuviesen el mismo ciclo, se utiliza la fórmula y el n sería igual a 3 (porque tenemos 3
SKU).

                          3,5    1          32        28        14
             𝑝𝑟𝑜𝑓 =                  12 ∗      + 15 ∗    + 10 ∗    = 4,3227
                           2    60           1         2         3
Problema 2
Describa supuestos de las fórmulas de profundidad óptima global para varios SKU.

Respuesta:

-No considera restricciones físicas de la bodega.

-Considera un ancho único para el pasillo y la bodega.

-Hace cálculos basado en el número de pallets completos, no por unidades o pick.

-Asume que las tasas de ventas relativas de los distintos SKU son iguales.

(Bartholdi, Warehouse & Distribution Science, página 58)



Problema 3

Describa ventajas y desventajas del almacenamiento compartido sobre el dedicado.

Ventajas:

-Mayor aprovechamiento de espacio disponible: al no tener posiciones reservadas para cada
producto, al desocuparse una posición se puede reasignar a otro producto, sin tener que
esperar por el tiempo de reposición.

-Un producto puede estar en más de una posición, ocupando superficies menores en cada
posición. Permitiendo que se desocupen posiciones de forma más frecuente, las que son
reasignadas.

Desventajas:

-Las posiciones de los productos cambian: los trabajadores tienen mayores dificultades con
aprender las posiciones, por lo que deben ser guiados por el sistema informático de la
bodega.

-Mayor complejidad de administrar: ya que agrega otros factores a considerar, como: elegir
la posición a la que conviene ir a buscar un producto (el más cercano, el con menor
cantidad, entre otros), trade-off entre reducir tiempo o espacio, etc. Esto exige mejores
sistemas informáticos y mayor disciplina de los trabajadores para que funcione
correctamente. (Bartholdi, Warehouse & Distribution Science, página 15)

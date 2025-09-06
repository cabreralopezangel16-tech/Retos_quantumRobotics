# Retos_quantumRobotics

El algoritomo despues de quw se crean las cordenadas del aruco
empiza evaluendo si la distancia es menor a a 30 unidades 
despues de esto empieza a evaluar puntos que se generan en un radio 
de 30 unidades estos puntos se generan con un angulo de 45° hasta completar 
una circunferencia completa. estos puntos se evaluan busacando que punto
tiene la distancia mas corta hacia las coordenadas del objetivo al encontrar 
el punto mas cernano se desplaza hacia este y asi continua en un ciclo infinito
hasta que la distancia hacia las coordenas del aruco son menores a 30 unidades.

Despues de esto se genera un trayectoria ciruclar entorno a las cordenas del aruco
en busqueda de este y finaliza hasta completar una vuelta completa.

Nota: este algoritmo no esta optimizado para su funcionamiento final y dependiendo 
de las formas de control de un robot fisico real este algoritmo cambiarai ya que no se
puede generalizar para cualquier robot fisico.

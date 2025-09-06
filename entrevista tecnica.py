import turtle
import math
import random
wn = turtle.Screen()
Robot = turtle
ArUco_cords = [0,0]

points = []

Robot_cords = [0,0,0]   #x,y,theta

#ArUco_cords[0]= 300*random.random()
#ArUco_cords[1]= 300*random.random()

ArUco_cords[0]=random.randrange(-320,320)
ArUco_cords[1] = random.randrange(-320,320)
done = False

parte = math.pi/4

actual_pos = [0,0]

def encontrar_punto_optimo(start,obj):
    disntancias = []
    for i in range(0,8):
        puntocreado_a_analizar = [start[0]+(30*math.cos(i*parte)),start[1]+(30*math.sin(i*parte))]
        disntancias.append(math.dist(puntocreado_a_analizar,obj))
        #print(disntancias)

    a = disntancias.index(min(disntancias))
    return [start[0]+(30*math.cos(a*parte)),start[1]+(30*math.sin(a*parte)),math.degrees(a*parte)]
Robot.speed(2)
while math.dist(actual_pos,ArUco_cords)>30:
    a = encontrar_punto_optimo(actual_pos,ArUco_cords)
    actual_pos = [a[0],a[1]]
    Robot.left(a[2]-Robot.heading())
    Robot.forward(30)
    print(ArUco_cords,Robot.pos())

#busqueda de los aruco
R_debusqueda = 15
Robot.forward(R_debusqueda)
L = (2*math.pi*R_debusqueda)/360
Robot.left(90)

for i in range(0,360):
    Robot.speed(10)
    Robot.forward(L)
    Robot.left(1)
    print(ArUco_cords,Robot.pos())



#points.append()


turtle.done()
""" 
el algoritmo busca en pasos de 45° analisa que punto tiene la menor distancia
hacia el objetivo y lo añade a la trayectoria a seguir
"""

"""
para buscar los arco crear 
"""
import math
from shapes import draw_regular_polygon


def design_1():
    draw_regular_polygon(CX=240,
                         CY=240,
                         K=4,
                         R=480*0.45,
                         AD=math.pi/4,
                         NP=480)


def design_2():
    draw_regular_polygon(CX=240,
                         CY=240,
                         K=3,
                         R=480*0.45,
                         AD=0,
                         NP=480)



def design_3():
    draw_regular_polygon(CX=240,
                         CY=240,
                         K=3,
                         R=480*0.45,
                         AD=math.pi/2,
                         NP=480)

def design_4():
    draw_regular_polygon(CX=240,
                         CY=240,
                         K=5,
                         R=480*0.45,
                         AD=math.pi/2,
                         NP=480)


def design_5():
    draw_regular_polygon(CX=240,
                         CY=240,
                         K=8,
                         R=480*0.5,
                         AD=math.pi/8,
                         NP=480)


def design_6():
    draw_regular_polygon(CX=240,
                         CY=240,
                         K=20,
                         R=480*0.4,
                         AD=0,
                         NP=480)

import math
from shapes import draw_prettygon


def design_26():
    draw_prettygon(K=200, 
                   AN=15*(math.pi/31),
                   RA=0.98,
                   AA=0,
                   RR=480*0.80,
                   NP=480)


def design_27():
    draw_prettygon(K=120, 
                   AN=29*(math.pi/30),
                   RA=0.98,
                   initial_y=240,
                   NP=480)


def design_28():
    draw_prettygon(K=200, 
                   AN=math.pi/4,
                   RA=0.98,
                   AA=0.0,
                   RR=480*0.40,
                   NP=480)


def design_29():
    draw_prettygon(K=200, 
                   AN=math.pi/20,
                   RA=0.998,
                   AA=0.0,
                   RR=480*0.65,
                   NP=480)


def design_30():
    draw_prettygon(K=200, 
                   AN=4*(math.pi/5)+0.02,
                   RA=0.99,
                   RR=480*0.80,
                   initial_y=200,
                   NP=480)
    
    
def design_31():
    draw_prettygon(K=100,
                   AN=6*(math.pi/7),
                   RA=0.98,
                   initial_y=200,
                   NP=480)


def design_32():
    draw_prettygon(K=300, 
                   AN=2*(math.pi/5)+0.01,
                   RA=0.993,
                   AA=0.0,
                   RR=480*0.60,
                   initial_y=20,
                   NP=480)


def design_33():
    draw_prettygon(K=400, 
                   AN=19*(math.pi/60),
                   RA=0.996,
                   RR=480*0.60,
                   NP=480)
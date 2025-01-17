import turtle
import math


def draw_prettygon(K: int = 200, 
                   AN: float = 15*(math.pi/31), 
                   RA: float = 0.98,
                   AA: float = 0.0,
                   RR: float = 0.80 * 480,
                   NP: int = 480):
    AA = 0.0
    RR = 0.80 * NP
    
    X = (NP - RR) / 2
    Y = 0
    
    turtle.penup()
    turtle.goto(X, Y)
    turtle.pendown()
    
    for i in range(K + 1):
        X += RR * math.cos(AA)
        Y += RR * math.sin(AA)
        
        turtle.goto(X, Y)
        
        AA += AN
        RR *= RA
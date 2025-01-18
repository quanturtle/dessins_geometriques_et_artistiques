import math
import turtle


def draw_regular_polygon(K: int = 5, NP: int = 480):
    CX = NP / 2
    CY = NP / 2
    R  = NP * 0.45
    AD = math.pi / 4

    for i in range(K + 1):
        x = CX + R * math.cos((2 * math.pi * i / K) + AD)
        y = CY + R * math.sin((2 * math.pi * i / K) + AD)
        
        if i == 0:
            turtle.penup()
        else:
            turtle.pendown()
        
        turtle.goto(x, y)
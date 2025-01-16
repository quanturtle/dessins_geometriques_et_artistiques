import turtle
import math


def setup_canvas(NP: int = 480):
    """
    Sets a window of size NP x NP in 'turtle' coordinates.
    """
    turtle.setup(width=NP, height=NP)
    
    turtle.setworldcoordinates(0, 0, NP, NP)
    
    turtle.speed("fast")
    
    turtle.penup()
    turtle.home()
    turtle.pendown()


def draw_regular_polygon(K: int = 5, NP: int = 480):
    """
    Draw a K-sided regular polygon on an NP x NP square canvas,
    centered at (NP/2, NP/2).
    """
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
    
    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_regular_polygon()
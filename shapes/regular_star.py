import turtle
import math


def setup_canvas(NP=480):
    """
    Sets a window of size NP x NP in 'turtle' coordinates.
    """
    turtle.setup(width=NP, height=NP)
    
    turtle.setworldcoordinates(0, 0, NP, NP)
    
    turtle.speed("fast")
    
    turtle.penup()
    turtle.home()
    turtle.pendown()


def draw_regular_star(K=5, H=3, NP=480):
    """
    Draw a K-pointed star, skipping H points each time.
    angle = 2 * i * H * pi / K
    With a fixed angle offset AD = pi/2 here for demonstration.
    """
    CX = NP / 2
    CY = NP / 2
    R  = NP * 0.27
    AD = math.pi / 2

    for i in range(K + 1):
        x = CX + R * math.cos((2 * i * H * math.pi / K) + AD)
        y = CY + R * math.sin((2 * i * H * math.pi / K) + AD)
        
        if i == 0:
            turtle.penup()
        else:
            turtle.pendown()
        
        turtle.goto(x, y)
    
    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_regular_star()
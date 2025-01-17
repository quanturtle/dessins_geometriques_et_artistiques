import turtle
import math


def setup_canvas(width=750):
    """Sets up the turtle canvas with given width"""
    turtle.setup(width=width, height=width)
    turtle.setworldcoordinates(0, 0, width, width)
    turtle.speed(0)  # Fastest speed
    turtle.hideturtle()


def draw_linear_sticks():
    # Constants
    NP = 480
    PI = math.pi
    N = 100  # Number of sticks
    M = 1    # Number of iterations
    K = 5    # Multiplier for angle
    
    for i in range(1, M + 1):
        R1 = NP/4        # Outer radius
        R2 = NP * 5/24   # Inner radius
        
        for j in range(N):
            # Calculate angle
            AN = 2 * j * PI / N
            
            # Calculate start point of stick
            XD = NP/2 + R1*math.cos(AN) + R2*math.cos(K*AN)
            YD = NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN)
            
            # Calculate end point of stick
            XA = NP/2 + R1*math.cos(AN) + R2*math.cos(K*AN + PI)
            YA = NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN + PI)
            
            # Draw the stick
            turtle.penup()
            turtle.goto(XD, YD)
            turtle.pendown()
            turtle.goto(XA, YA)
    
    turtle.hideturtle()
    turtle.exitonclick()

setup_canvas()
draw_linear_sticks()
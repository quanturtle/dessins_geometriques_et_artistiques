import turtle
import math

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


def draw_joligones():
    # Interpreted constants based on the BASIC code
    NP = 480               # Drawing area size
    PI = math.pi
    K  = 200               # Number of steps
    AN = 15 * PI / 31      # Angle increment
    RA = 0.98              # Radius shrinking factor each step
    
    # Initial angle and radius
    AA = 0.0
    RR = 0.80 * NP         # e.g. 0.80 * 480 = 384
    
    # Starting point
    X = (NP - RR) / 2      # e.g. (480 - 384)/2 = 48
    Y = 0
    
    # Set up the turtle screen and speed
    turtle.setup(NP, NP)
    turtle.speed("fastest")
    
    # Move turtle to the starting position
    turtle.penup()
    turtle.goto(X, Y)
    turtle.pendown()
    
    # Main loop from the BASIC code: FOR I=0 TO K
    for i in range(K + 1):
        # Update X, Y
        X += RR * math.cos(AA)
        Y += RR * math.sin(AA)
        
        # Draw to new position
        turtle.goto(X, Y)
        
        # Update angle and radius
        AA += AN
        RR *= RA
    
    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_joligones()
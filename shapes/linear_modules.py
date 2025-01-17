import turtle
import math


def setup_canvas(width=750):
    """Sets up the turtle canvas with given width"""
    turtle.setup(width=width, height=width)
    turtle.setworldcoordinates(0, 0, width, width)
    turtle.speed("fastest")
    turtle.hideturtle()


def draw_linear_modulo(DESSIN=108):
    # Constants
    NP = 480
    PI = math.pi
    
    # Initialize parameters based on DESSIN value
    if DESSIN == 106:
        N = 500
        K1 = 11/7
        K2 = 7/3
        H = 3
    elif DESSIN == 107:
        N = 400
        K1 = 4
        K2 = 2
        H = 2
    elif DESSIN == 108:
        N = 300
        K1 = 5
        K2 = 3
        H = 2
    else:  # Default case (DESSIN == 105)
        N = 400
        K1 = 4
        K2 = 5
        H = 2
    
    M = N
    
    # Create coordinate arrays
    X = []
    Y = []
    
    # Calculate coordinates
    for i in range(N):
        x = int(NP * 0.5 * (1 + math.sin(K1 * i * PI / N)))
        y = int(NP * 0.75 * (1 + math.cos(K2 * i * PI / N)))
        X.append(x)
        Y.append(y)
    
    # Draw the pattern
    for i in range(M):
        i1 = i % N
        i2 = (H * i) % N
        
        # Move to first point
        turtle.penup()
        turtle.goto(X[i1], Y[i1])
        turtle.pendown()
        
        # Draw line to second point
        turtle.goto(X[i2], Y[i2])
    
    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_linear_modulo(DESSIN=108)
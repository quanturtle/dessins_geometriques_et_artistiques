import turtle
import math

def setup_canvas(width=800):
    """Sets up the turtle canvas with given width"""
    turtle.setup(width=width, height=width)
    turtle.setworldcoordinates(0, 0, width, width)
    turtle.speed("fastest")  # Fastest speed
    turtle.hideturtle()

def draw_dragon(DESSIN=50):
    # Constants
    NP = 480
    PI = math.pi
    
    # Set N based on DESSIN value
    if DESSIN == 51:
        N = 10
    elif DESSIN == 52:
        N = 14
    else:
        N = 6
    
    # Initialize arrays and variables
    A = [0] * (N + 1)
    X0 = NP/3
    Y0 = NP/2
    A0 = -PI/4 * (N-2)
    L0 = NP/math.pow(math.sqrt(2), N)
    
    X1 = X0
    Y1 = Y0
    X2 = X0
    Y2 = Y0
    
    def gosub():
        nonlocal X0, Y0, X1, Y1, X2, Y2
        X0 = X1
        Y0 = Y1
        X1 = X2
        Y1 = Y2
        X2 = X2 + L0 * math.cos(A0)
        Y2 = Y2 + L0 * math.sin(A0)
    
    # Start drawing
    turtle.penup()
    turtle.goto(X0, Y0)
    turtle.pendown()
    
    NN = pow(2, N) - 1
    for I in range(NN + 1):
        if I == 0:
            gosub()
        else:
            II = I
            J = 0
            while II % 2 == 0:
                II = II // 2
                J += 1
            AA = (A[N-J]*2-1) * (((II-1)//2)%2 * 2-1) * PI/2
            A0 += AA
            gosub()
        
        # Draw the curve segments
        mid_x1 = (X0 + 3*X1)/4
        mid_y1 = (Y0 + 3*Y1)/4
        mid_x2 = (X2 + 3*X1)/4
        mid_y2 = (Y2 + 3*Y1)/4
        
        turtle.goto(mid_x1, mid_y1)
        turtle.goto(mid_x2, mid_y2)

    turtle.hideturtle()
    turtle.exitonclick()

setup_canvas()
draw_dragon(DESSIN=51)
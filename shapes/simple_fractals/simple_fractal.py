import turtle
import math

def setup_canvas(NP=480):
    """
    Sets up the turtle window with a coordinate system [0,NP]x[0,NP]
    and speed set to fastest.
    """
    turtle.setup(width=NP, height=NP)
    turtle.setworldcoordinates(0, 0, NP, NP)
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def draw_fractales_simples():
    NP = 480
    M = 3
    N = 4
    K = 4

    # Initialize arrays based on BASIC dimensions
    X = [0]*(M+1)      # size M+1
    Y = [0]*(M+1)
    L_array = [0]*N    # size N
    A_array = [0]*N    # size N

    # Lines 120-130: Set initial points
    X[0] = 0
    X[1] = NP
    X[2] = NP * 0.5
    X[3] = 0

    Y[0] = 0
    Y[1] = 0
    Y[2] = math.sqrt(3)/2 * NP
    Y[3] = Y[0]

    # Line 140: Set all L_array values to 1/3
    for idx in range(N):
        L_array[idx] = 1/3

    # Line 150: Initialize A_array values
    A_array[0] = 0
    A_array[1] = math.pi / 3
    A_array[2] = -math.pi / 3
    A_array[3] = 0

    # Outer loop over segments defined by points in arrays X and Y
    for II in range(M):
        # Lines 210: Determine segment endpoints
        XD = X[II]
        YD = Y[II]
        XA = X[II+1]
        YA = Y[II+1]

        # Lines 250-270: Move to starting point of the segment
        X0 = XD
        Y0 = YD
        turtle.penup()
        turtle.goto(int(X0), int(Y0))
        turtle.pendown()

        # Lines 280-285: Compute angle and length of the segment
        A0 = math.atan2(YA - YD, XA - XD)  # atan2 handles division by zero and quadrant correction
        L0 = math.sqrt((XA - XD)**2 + (YA - YD)**2)

        # Lines 300-500: Fractal drawing along the current segment
        for I in range(0, N**K):
            LL = L0
            AA = A0
            T = I

            # Inner loop over J from K-1 down to 0
            for J in range(K-1, -1, -1):
                R_val = N**J
                T2 = T // R_val
                AA += A_array[T2]
                LL *= L_array[T2]
                T = T - T2 * R_val

            # Compute new point and draw line
            X0 = X0 + LL * math.cos(AA)
            Y0 = Y0 + LL * math.sin(AA)
            turtle.pendown()
            turtle.goto(int(X0), int(Y0))

    turtle.hideturtle()
    turtle.exitonclick()

setup_canvas()
draw_fractales_simples()
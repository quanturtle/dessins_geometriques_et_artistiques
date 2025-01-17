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


def draw_fractales_simples_deformees():
    NP = 480
    M = 3
    N = 4
    K = 4

    # Initialize arrays based on BASIC dimensions
    X = [0] * (M + 1)
    Y = [0] * (M + 1)
    L_array = [0] * N
    A_array = [0] * N

    # Lines 120-130: Set initial points
    for IJ in range(4):
        X[IJ] = NP / 2 * (1 + math.sin(2 * IJ * math.pi / 3))
        Y[IJ] = NP / 2 * (1 + math.cos(2 * IJ * math.pi / 3))

    # Line 140: Set L_array values
    for idx in range(N):
        L_array[idx] = 1 / 3

    # Line 150: Set A_array values
    A_array[0] = 0
    A_array[1] = math.pi / 3
    A_array[2] = -math.pi / 3
    A_array[3] = 0

    # Outer loop over segments defined by points in arrays X and Y
    for II in range(M):
        # Lines 210: Determine segment endpoints
        XD = X[II]
        YD = Y[II]
        XA = X[II + 1]
        YA = Y[II + 1]

        # Line 250: Initialize starting points
        X0 = XD
        Y0 = YD

        # Line 270: Deformation subroutine for initial point
        X1, Y1 = deformation_subroutine(X0, Y0, NP)
        turtle.penup()
        turtle.goto(X1, Y1)
        turtle.pendown()

        # Line 280-285: Compute angle and length of the segment
        if XA != XD:
            A0 = math.atan2(YA - YD, XA - XD)
        else:
            A0 = math.pi / 2 * math.copysign(1, YA - YD)
        if (XA - XD) < 0:
            A0 += math.pi

        L0 = math.sqrt((XA - XD)**2 + (YA - YD)**2)

        # Lines 300-500: Fractal drawing along the current segment
        for I in range(0, N**K):
            LL = L0
            AA = A0
            T = I

            # Inner loop over J from K-1 down to 0
            for J in range(K - 1, -1, -1):
                R = N**J
                T2 = T // R
                AA += A_array[T2]
                LL *= L_array[T2]
                T -= T2 * R

            # Compute new point
            X0 = X0 + LL * math.cos(AA)
            Y0 = Y0 + LL * math.sin(AA)

            # Line 485: Deformation subroutine for each point
            X1, Y1 = deformation_subroutine(X0, Y0, NP)
            turtle.goto(X1, Y1)

    turtle.hideturtle()
    turtle.exitonclick()


def deformation_subroutine(X0, Y0, NP):
    """
    Subroutine to apply deformation to the points.
    """
    XH = X0 / NP * 2 - 1
    YH = Y0 / NP * 2 - 1
    DH = math.sqrt(XH * XH + YH * YH)

    if XH != 0:
        AH = math.atan2(YH, XH)
    else:
        AH = math.pi / 2 * math.copysign(1, YH)

    DH = DH**2
    X1 = int((DH * math.cos(AH) + 1) * NP / 2)
    Y1 = int((DH * math.sin(AH) + 1) * NP / 2)

    return X1, Y1

setup_canvas()
draw_fractales_simples_deformees()
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


def draw_surfaces():
    NP = 480
    N = 6
    PA = NP / 16
    E1 = 2
    E2 = 1

    XA, YA = NP / 2, NP / 16
    XB, YB = NP * 7 / 8, NP / 4
    XC, YC = NP / 2, NP * 5 / 8
    XD, YD = NP / 8, NP * 7 / 16

    M = int(NP / PA)
    MAX = [-5 * NP] * (M + 1)
    MIN = [5 * NP] * (M + 1)

    for I in range(N + 1):
        XP = (I * XD + (N - I) * XA) / N
        YP = (I * YD + (N - I) * YA) / N
        XQ = (I * XC + (N - I) * XB) / N
        YQ = (I * YC + (N - I) * YB) / N

        I1 = int(XP / PA)
        I2 = int(XQ / PA)
        G = math.copysign(1, I2 - I1)

        for J in range(I1, I2 + 1, int(G)):
            X = (J - I1) / (I2 - I1)
            Y = (J - I1) / (I2 - I1)

            # Subroutine for Z = f(X, Y)
            Z = surface_subroutine(X, Y, NP)

            XF = int(J * PA)
            YF = int(((J - I1) * YQ + (I2 - J) * YP) / (I2 - I1) + Z)

            if J == I1:
                turtle.penup()
                turtle.goto(XF, YF)
                turtle.pendown()
            else:
                if E2 != 1:
                    if MIN[J] < YF < MAX[J]:
                        turtle.penup()
                        turtle.goto(XF, YF)
                        turtle.pendown()

                if YF > MAX[J]:
                    MAX[J] = YF
                if YF < MIN[J]:
                    MIN[J] = YF

                turtle.goto(XF, YF)

    turtle.hideturtle()
    turtle.exitonclick()


def surface_subroutine(X, Y, NP):
    """
    Subroutine for Z = f(X, Y).
    """
    return NP / 3 * math.sin(math.pi * Y) * math.sin(math.pi * X)

setup_canvas()
draw_surfaces()
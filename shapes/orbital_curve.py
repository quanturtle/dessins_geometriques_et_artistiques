import turtle
import math

def setup_canvas(NP: int = 480):
    """
    Sets a window of size NP x NP in 'turtle' coordinates.
    """
    turtle.setup(width=NP, height=NP)
    turtle.setworldcoordinates(0, 0, NP, NP)
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def draw_courbes_orbitales():
    """
    Python turtle version of the BASIC 'COURBES ORBITALES' program.
    Replicates the same orbit drawing logic.
    """

    NP = 480
    # From the BASIC code:
    N  = 2000
    T1 = 2
    T2 = 100
    K1 = 1
    K2 = 1
    R1 = NP * 0.25

    # Main loop: I from 0 to N
    for i in range(N + 1):
        # R2 = NP * 0.2 * (1 - i/N)
        R2 = NP * 0.2 * (1.0 - i / N)

        # A1 = 2*pi * i/N * K1
        # A2 = 2*pi * i/N * T2
        A1 = 2.0 * math.pi * i / N * K1
        A2 = 2.0 * math.pi * i / N * T2

        # X = INT(NP * 0.5 + R1 * COS(K1*A1) + R2*COS(A2))
        # Y = INT(NP * 0.5 + R1 * SIN(K2*A1) + R2*SIN(A2))
        X = int(NP * 0.5 + R1 * math.cos(K1 * A1) + R2 * math.cos(A2))
        Y = int(NP * 0.5 + R1 * math.sin(K2 * A1) + R2 * math.sin(A2))

        if i == 0:
            # "M" => pen up + move to first point
            turtle.penup()
            turtle.goto(X, Y)
            turtle.pendown()
        else:
            # "D" => draw line to next point
            turtle.goto(X, Y)

    turtle.hideturtle()
    turtle.exitonclick()

setup_canvas()
draw_courbes_orbitales()
import turtle
import math


def setup_canvas(NP=480):
    """
    Sets a window of size NP x NP in 'turtle' coordinates.
    """
    turtle.setup(width=NP, height=NP)
    turtle.setworldcoordinates(0, 0, NP, NP)
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def draw_lineaires_batons():
    """
    Python turtle version of the BASIC 'LINEAIRES BATONS' program.
    Replicates the original logic exactly (including the fact that
    the loop index 'J' is not used in the angle calculation).
    """

    NP = 480
    # From the BASIC code:
    N = 100
    M = 1
    K = 5

    for i in range(1, M + 1):
        # line 210: R1=NP/4, R2=NP*5/24
        R1 = NP / 4.0
        R2 = NP * 5.0 / 24.0

        # line 300: FOR J=0 TO N-1
        for j in range(N):
            # line 310: AN=2*K*PI/N (no 'j' in the formula)
            AN = 2.0 * K * math.pi / N

            # line 320-330: XD, YD
            XD = (NP / 2.0
                  + R1 * math.cos(AN)
                  + R2 * math.cos(K * AN))
            YD = (NP / 2.0
                  + R1 * math.sin(AN)
                  + R2 * math.sin(K * AN))

            # line 340-350: XA, YA
            #   +PI inside the cos/sin effectively flips the sign
            XA = (NP / 2.0
                  + R1 * math.cos(AN)
                  + R2 * math.cos(K * AN + math.pi))
            YA = (NP / 2.0
                  + R1 * math.sin(AN)
                  + R2 * math.sin(K * AN + math.pi))

            # line 400: "M" => penup + move
            turtle.penup()
            turtle.goto(int(XD), int(YD))

            # line 410: "D" => pendown + draw
            turtle.pendown()
            turtle.goto(int(XA), int(YA))

    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_lineaires_batons()
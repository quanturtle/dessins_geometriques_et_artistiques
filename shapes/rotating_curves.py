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


def draw_courbes_tournantes():
    """
    Python turtle version of the BASIC 'COURBES TOURNANTES' program.
    """

    NP = 480
    # From the BASIC code:
    N  = 2000
    T1 = 1
    T2 = 100
    K1 = 1
    K2 = 1
    H1 = 1
    H2 = 1
    R1 = NP / 6
    R2 = NP / 4

    for i in range(N + 1):
        # 210 S = COS(4*PI*i/N)*0.4 + 0.6
        S = math.cos(4 * math.pi * i / N) * 0.4 + 0.6

        # 220 AN = 2*PI*i/N
        AN = 2.0 * math.pi * i / N

        # 230 c1 = COS(H1*AN*T1), s1 = SIN(H2*AN*T1)
        c1 = math.cos(H1 * AN * T1)
        s1 = math.sin(H2 * AN * T1)

        # 240 c2 = S*COS(K1*AN*T2), s2 = S*SIN(K2*AN*T2)
        c2 = S * math.cos(K1 * AN * T2)
        s2 = S * math.sin(K2 * AN * T2)

        # 300-310 
        # X = NP/2 + R1*c1 + R2*(c1*c2 - s1*s2)
        # Y = NP/2 + R1*s1 + R2*(s1*c2 + c1*s2)
        X = (NP / 2.0) + R1 * c1 + R2 * (c1 * c2 - s1 * s2)
        Y = (NP / 2.0) + R1 * s1 + R2 * (s1 * c2 + c1 * s2)

        if i == 0:
            # "M" => Move (pen up + goto)
            turtle.penup()
            turtle.goto(int(X), int(Y))
            turtle.pendown()
        else:
            # "D" => Draw
            turtle.goto(int(X), int(Y))

    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_courbes_tournantes()
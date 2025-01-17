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


def draw_courbes_spirales():
    """
    Python turtle version of the BASIC 'COURBES SPIRALES' program.
    """

    NP = 480
    # From the BASIC code:
    N = 2000
    T = 40
    R = 0.8
    L = 0.1

    for i in range(N + 1):
        # 210: RR = L^(i/N)
        RR = (L ** (i / N))

        # 220: AN = 2*pi*(i/N)
        AN = 2.0 * math.pi * (i / N)

        # 230: X=RR*R*cos(T*AN), Y=RR*R*sin(T*AN)
        X = RR * R * math.cos(T * AN)
        Y = RR * R * math.sin(T * AN)

        # 240: CO=cos(AN), SI=sin(AN)
        CO = math.cos(AN)
        SI = math.sin(AN)

        # 250: XX=X*CO - Y*SI, YY=X*SI + Y*CO
        XX = X * CO - Y * SI
        YY = X * SI + Y * CO

        # 260, 270: X%=INT(NP/2*(1+XX)), Y%=INT(NP/2*(1+YY))
        xp = int(NP / 2 * (1 + XX))
        yp = int(NP / 2 * (1 + YY))

        # Move or draw
        if i == 0:
            # "M" => penup + goto
            turtle.penup()
            turtle.goto(xp, yp)
            turtle.pendown()
        else:
            # "D" => draw
            turtle.goto(xp, yp)

    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_courbes_spirales()
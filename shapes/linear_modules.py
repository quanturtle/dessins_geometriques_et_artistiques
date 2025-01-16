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


def draw_lineaires_modulo():
    """
    Python turtle version of the BASIC 'LINÉAIRES MODULO' program.
    """

    NP = 480

    # From the BASIC code:
    #  N=400, M=K1=4, K2=5, H=2
    N  = 400
    M  = 4
    K1 = 4
    K2 = 5
    H  = 2

    # We'll store X[i] and Y[i] for i=0..N
    Xvals = [0] * (N + 1)
    Yvals = [0] * (N + 1)

    # Lines 200-230: fill X%(i) and Y%(i)
    for i in range(N + 1):
        # X%(i)=INT(NP*.5*(1+SIN(K1*(i*PI/N))))
        Xvals[i] = int(NP * 0.5 * (1 + math.sin(K1 * (i * math.pi / N))))
        # Y%(i)=INT(NP*.75*(1+COS(K2*(i*PI/N))))
        Yvals[i] = int(NP * 0.75 * (1 + math.cos(K2 * (i * math.pi / N))))

    # Lines 300-400: loop i=0..M, draw lines
    for i in range(M + 1):
        # i1 = i mod N, i2 = H*i mod N
        i1 = i % N
        i2 = (H * i) % N

        # "M x(i1), y(i1)" => penup + move
        turtle.penup()
        turtle.goto(Xvals[i1], Yvals[i1])

        # "D x(i2), y(i2)" => pendown + draw
        turtle.pendown()
        turtle.goto(Xvals[i2], Yvals[i2])

    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_lineaires_modulo()
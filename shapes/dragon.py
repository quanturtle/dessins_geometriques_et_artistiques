import turtle
import math


def setup_canvas(NP=480):
    """
    Sets up a turtle window of size NP x NP, 
    with a coordinate system from (0,0) to (NP,NP).
    """
    turtle.setup(width=NP, height=NP)
    turtle.setworldcoordinates(0, 0, NP, NP)
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def draw_dragons():
    """
    Python turtle version of the BASIC 'DRAGONS' program.
    Because lines 230-240 in the original code are incomplete/mysterious,
    we make an educated guess that the angle changes by ±(pi/2).
    """

    NP = 480            # from line 50 (somewhat implied)
    N = 6               # line 100
    # A array is all zeros (line 110-120). 
    # We won't store them because they never change in your snippet.

    # line 130
    x0 = NP / 3.0
    y0 = NP / 2.0
    a0 = -math.pi / 4.0 * (N - 2)       # initial angle
    L0 = NP / math.sqrt(2) * N         # step length

    # line 140
    x1 = x0
    y1 = y0
    x2 = x0
    y2 = y0

    # BASIC line 150 => "M x0,y0" => pen up/move
    turtle.penup()
    turtle.goto(int(x0), int(y0))
    turtle.pendown()

    # line 160 => NN = 2^N - 1
    NN = 2**N - 1

    for i in range(NN + 1):    # 0..NN inclusive
        if i != 0:
            # lines 215..240
            II = i
            j = 0
            # line 220: count trailing zeros in II
            while (II % 2) == 0:
                II = II // 2
                j += 1

            # line 230: BASIC is unclear, so we guess:
            #   sign = ±1 depending on the next bit pattern
            #   sign = (((II - 1)//2) % 2)*2 - 1 will be +1 or -1
            #   so angle change is ±(pi/2)
            sign = (((II - 1) // 2) % 2) * 2 - 1
            # guessed angle change
            AA = sign * (math.pi / 2)
            a0 += AA

        # line 300
        # shift old points
        old_x0, old_y0 = x0, y0
        x0, y0 = x1, y1
        x1, y1 = x2, y2

        # line 300 => now compute next X2,Y2
        x2 = x2 + L0 * math.cos(a0)
        y2 = y2 + L0 * math.sin(a0)

        # lines 310, 315 => plot partial lines between points
        # first "D" => from the BASIC:
        #    INT((x0+3*x1)/4), INT((y0+3*y1)/4)
        turtle.goto(int((x0 + 3*x1)/4.0), int((y0 + 3*y1)/4.0))

        # second "D"
        turtle.goto(int((x2 + 3*x1)/4.0), int((y2 + 3*y1)/4.0))

    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas(480)
draw_dragons()
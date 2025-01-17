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
    turtle.home()
    turtle.pendown()


def draw_cheval():
    """
    Python turtle version of the BASIC 'CHEVAL' program.
    Replicates reading logic and draws lines accordingly.
    """

    data = [
        1000, 10,10, 8,12, 9,16, 12,17, 13,18, 14,20,
        1000, 13,18, 12,19, 9,21, 9,20, 10,19, 9, 17, 7,20, 8,22, 12,22,
        1000, 12,20, 12,22, 13,26, 16,31, 18,31, 19,32,
        1000, 16,31, 14,31, 14,32,
        1000, 14,31, 10,30, 12,31, 10,32, 10,34, 11,34, 11,33, 10,33,
        1000, 12,32, 13,31,
        1000, 10,34, 16,36,
        1000, 16,35, 16,37, 18,35, 17,34,
        1000, 17,36, 20,36, 22,32, 19,26,
        1000, 20,36, 22,36, 22,34, 24,32, 24,30, 19,26, 18,23, 21,22, 21,24,
        30,30, 34,31, 36,31, 33,26, 32,22, 28, 22, 27,20, 29,17, 30,19, 29,20,
        29,21, 32,19, 33,18, 32,17, 29,16, 28, 12, 30,10, 21,4, 21,2,
        18,3, 19,6, 24,10, 24,12, 22,14, 22,16, 23,17,
        1000, 22,16, 17,16, 16,17, 17,18,
        1000, 16,17, 16, 16, 10, 14, 10,12, 12,11, 10, 10,
        1000, 21,21, 22,24, 30,30,
        1000, 24,24, 34, 28,
        1000, 25,23, 33, 26,
        1000, 25,21, 27, 20,
        1000, 23,21, 24, 19,
        1000, 27,20, 22, 19, 22,21,
        1000, 22, 19, 21,20,
        1000, 13,34, 15,35, 16,34, 16,33,
        1000, 15,35, 15,34, 16,34, 15,34, 15,35,
        1000, 24, 12, 26, 10, 19,5, 19,3,
        1000, 28,22, 25, 22,
        2000
    ]

    NP = 480
    i  = 0           # index into data list
    B1 = 0           # in BASIC, used to track "move" vs "draw"
    
    while True:
        A = data[i]
        i += 1

        # If it's 2000 => stop reading
        if A == 2000:
            break

        # If it's 1000 => next pair is a move-to
        if A == 1000:
            B1 = 0
            A = data[i]; i += 1  # next X
            B = data[i]; i += 1  # next Y
        else:
            # otherwise, 'A' is the X coordinate, read next for Y
            B = data[i]
            i += 1

        # Scale as X% = NP*A/40, Y% = NP*B/40
        X = NP * A / 40.0
        Y = NP * B / 40.0

        if B1 == 0:
            # "TM" in BASIC => Pen up + Move
            turtle.penup()
            turtle.goto(X, Y)
            B1 = 1
        else:
            # "D" in BASIC => Pen down + Draw
            turtle.pendown()
            turtle.goto(X, Y)
    
    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_cheval()
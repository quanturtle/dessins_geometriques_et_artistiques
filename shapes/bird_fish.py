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


def draw_oiseaux_poissons():
    """
    Python turtle version of the BASIC 'OISEAUX-POISSONS' program.
    Follows the same reading logic and line drawing approach.
    """

    data = [
        # From 1000 DATA
        1000, 0,0, 2,0, 4,1, 4,2, 3,2, 2,3, 4,5, 4,6, 2,5, 2,6, -1,5, -2,3,
        # From 1010 DATA
        -1,2, -2,2, -3,3, -4,3, -5,2, -4,2, 0,0,

        # From 1020 DATA
        1000, -5,2, -5,1, -7,-1, -6,-2, -5,-2, -5,-3, -2,2, -2,-3, 0,-2,

        # From 1030 DATA
        1,-1, 2,-1, 3,-2, 4,-2, 3,-1, 4,1,

        # From 1040 DATA
        1000, 2,5, 0,4, 0,2,

        # From 1050 DATA
        1000, -2,1, -5,1, -4,-1, -3,0, -3,-1, -4,-1, -5,-2, 0,-2,

        # From 1060 DATA
        1000, -7,-1, -6,-1,

        # From 1070 DATA (appears partially corrupted with extra numbers)
        1000, -4,2.5, -4,2.8, -4,3,2.8, -4,3,2.5, -4,2.5,

        # From 1080 DATA (also appears corrupted with triple or extra numbers)
        1000, -5,0, -5,5,0, -5,5,0,5, 5,0,5, -5,0,

        # From 1200 DATA
        2000
    ]

    NP = 480
    i  = 0         # index into data list
    B1 = 0         # in BASIC, used to track "move" vs "draw"

    while True:
        A = data[i]
        i += 1

        # 2000 => end
        if A == 2000:
            break

        # 1000 => new path => next two tokens are move-to
        if A == 1000:
            B1 = 0
            A = data[i]; i += 1  # X
            B = data[i]; i += 1  # Y
        else:
            # otherwise A is X, next is Y
            B = data[i]
            i += 1

        X = int(NP * (A + 10) / 15)
        Y = int(NP * (B + 10) / 15)

        if B1 == 0:
            # pen up + move
            turtle.penup()
            turtle.goto(X, Y)
            B1 = 1
        else:
            # pen down + draw
            turtle.pendown()
            turtle.goto(X, Y)

    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_oiseaux_poissons()

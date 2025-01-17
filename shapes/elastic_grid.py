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


def draw_quadrillages_elastiques():
    NP = 480

    # Outer loop for L=0 and L=1
    for L in range(2):
        # Loop over grid points
        for I in range(21):
            for J in range(21):
                # Line 200: Compute X and Y
                X = I / 10 - 1
                Y = J / 10 - 1

                # Line 210: Swap X and Y if L=1
                if L == 1:
                    X, Y = Y, X

                # Line 300: Compute distance D
                D = math.sqrt(X * X + Y * Y)

                # Line 310: Compute angle AN
                if X != 0:
                    AN = math.atan2(Y, X)
                else:
                    AN = math.pi / 2 * math.copysign(1, Y)

                # Line 320: Adjust AN if X < 0
                if X < 0:
                    AN += math.pi

                # Line 400: Apply deformation if D < 1
                if D < 1:
                    D = D**3

                # Line 500: Transform X and Y
                X = D * math.cos(AN)
                Y = D * math.sin(AN)

                # Line 510: Scale to screen coordinates
                X_percent = int(NP / 2 * (1.95 * X))
                Y_percent = int(NP / 2 * (1.95 * Y))

                # Line 600-610: Draw the grid lines
                if J == 0:
                    turtle.penup()
                    turtle.goto(X_percent, Y_percent)
                    turtle.pendown()
                else:
                    turtle.goto(X_percent, Y_percent)

    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_quadrillages_elastiques()
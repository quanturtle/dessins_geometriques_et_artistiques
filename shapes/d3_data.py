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


def draw_d3_data():
    NP = 480
    DC = 2
    TC = 2

    OX, OY, OZ = 5, -2, 1.3
    AZ, AY, AX = 3 * math.pi / 4, 0, 0
    QX, QY, QZ = 0, 0, 0

    # Precompute cosines and sines
    C1, S1 = math.cos(AZ), -math.sin(AZ)
    C2, S2 = math.cos(AY), -math.sin(AY)
    C3, S3 = math.cos(AX), -math.sin(AX)

    data = [
        [0,0,0, 0,0,2, 1,0,3, 1,0,4, 2,0,4, 2,0,3, 3,0,2, 3,0,0, 3,1,0, 3,1,2],
        [2,1,3, 2,1,4, 2,0,4, 1.5,.5,5.5, 1,0,4, 1000],
        [0,0,0, 3,0,0, 1000],
        [1,0,0, 1,0,1, 1.25,0,1.3, 1.75,0,1.3, 2,0,1, 2,0,0, 1000],
        [3,0,2, 3,1,2, 1000],
        [2,0,3, 2,1,3, 1000],
        [2,1,4, 1.5,.5,5.5, 2000],
        [1,1,4, 1,1,3, 0,1,2, 0,1,0, 3,1,0, 1000],
        [0,0,0, 0,1,0, 1000],
        [0,0,2, 0,1,2, 1000],
        [1,0,3, 1,1,3, 1000],
        [1,0,4, 1,1,4, 2,1,4, 2000]
    ]


    for segment in data:
        B1 = 0
        for i in range(0, len(segment), 3):
            if segment[i] == 1000:
                B1 = 0
                continue
            if segment[i] == 2000:
                break

            MX, MY, MZ = segment[i], segment[i + 1], segment[i + 2]

            # Perspective transformation
            MX -= OX
            MY -= OY
            MZ -= OZ

            UU = MX
            MX = C1 * UU - S1 * MY
            MY = S1 * UU + C1 * MY

            UU = MX
            MX = C2 * UU - S2 * MZ
            MZ = S2 * UU + C2 * MZ

            UU = MY
            MY = C3 * UU - S3 * MZ
            MZ = S3 * UU + C3 * MZ

            MX -= QX
            MY -= QY
            MZ -= QZ

            KP = DC / MX
            XX = -KP * MY
            YY = KP * MZ

            X_percent = int(NP * (0.5 + XX / TC))
            Y_percent = int(NP * (0.5 + YY / TC))

            if B1 == 1:
                turtle.pendown()
                turtle.goto(X_percent, Y_percent)
            else:
                B1 = 1
                turtle.penup()
                turtle.goto(X_percent, Y_percent)
                turtle.pendown()

    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_d3_data()
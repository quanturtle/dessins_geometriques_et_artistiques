import math
import turtle


def draw_spiraling_curves(N: int = 2000,
                          T: float = 40,
                          R: float = 0.8,
                          L: float = 0.1,
                          NP: int = 480):
    for i in range(N):
        RR = L ** (i / N)
        AN = 2 * math.pi * i / N

        X = RR * math.cos(T * AN)
        Y = RR * R * math.sin(T * AN)

        CO = math.cos(AN)
        SI = math.sin(AN)

        XX = X * CO - Y * SI
        YY = X * SI + Y * CO

        X_ = int(NP / 2 * (1 + XX))
        Y_ = int(NP / 2 * (1 + YY))

        if i == 0:
            turtle.goto(X_, Y_)
            turtle.pendown()

        else:
            turtle.goto(X_, Y_)
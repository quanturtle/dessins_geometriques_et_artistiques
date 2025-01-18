import math
import turtle


def draw_spiraling_curves(N: int = 2000,
                          T: int = 40,
                          R: float = 0.8,
                          L: float = 0.1,
                          NP: int = 480):
    for i in range(N + 1):
        RR = (L ** (i / N))

        AN = 2.0 * math.pi * (i / N)

        X = RR * R * math.cos(T * AN)
        Y = RR * R * math.sin(T * AN)

        CO = math.cos(AN)
        SI = math.sin(AN)

        XX = X * CO - Y * SI
        YY = X * SI + Y * CO

        xp = int(NP / 2 * (1 + XX))
        yp = int(NP / 2 * (1 + YY))

        if i == 0:
            turtle.penup()
            turtle.goto(xp, yp)
            turtle.pendown()
        
        else:
            turtle.goto(xp, yp)
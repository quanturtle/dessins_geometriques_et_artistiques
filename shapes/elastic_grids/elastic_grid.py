import math
import turtle
from typing import Callable


# TODO: factor out these two functions
# DI_func
def default_deformation_subroutine(DI: float) -> float:
    if DI < 1:
        return DI ** 0.3
    
    return DI


# AN_func
# def default_AN_func()


# add L_range, I_range, J_range
# X_strecht, Y_strecht
def draw_elastic_grid(deformation_subroutine: Callable = default_deformation_subroutine, 
                      NP: int = 480):
    def sgn(x):
        return 1 if x > 0 else -1 if x < 0 else 0

    for L in range(2):
        for I in range(21):
            for J in range(21):
                X = I / 10 - 1
                Y = J / 10 - 1

                if L == 1:
                    X, Y = Y, X

                DI = math.sqrt(X * X + Y * Y)

                if abs(X) > 1e-12:
                    AN = math.atan(Y / X)

                else:
                    AN = (math.pi / 2) * sgn(Y)

                if X < 0:
                    AN += math.pi

                DI = deformation_subroutine(DI)

                X = DI * math.cos(AN)
                Y = DI * math.sin(AN)

                X_ = int(NP / 2 * (1 + 0.95 * X))
                Y_ = int(NP / 2 * (1 + 0.95 * Y))

                if J == 0:
                    turtle.penup()
                    turtle.goto(X_, Y_)

                else:
                    turtle.pendown()
                    turtle.goto(X_, Y_)
import math
import turtle
from typing import Callable, Tuple

# TODO: refactor elastic grids to compute a deformation subroutine
def default_deformation_subroutine(DI: float):
    if DI < 1:
        return DI ** 0.3
    
    return DI


def sgn(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def default_AN_func(X: float, Y: float, DI: float) -> float:
    if abs(X) > 1e-12:
        AN = math.atan(Y / X)

    else:
        AN = (math.pi / 2) * sgn(Y)

    if X < 0:
        AN += math.pi
    
    return AN


# X_strecht, Y_strecht
def draw_elastic_grid(deformation_subroutine: Callable = default_deformation_subroutine,
                      AN_func: Callable = default_AN_func,
                      L_range: int = 2,
                      I_range: int = 21,
                      J_range: int = 21,
                      NP: int = 480):
    for L in range(L_range):
        for I in range(I_range):
            for J in range(J_range):
                X = I / 10 - 1
                Y = J / 10 - 1

                if L == 1:
                    X, Y = Y, X

                DI = math.sqrt(X * X + Y * Y)

                AN = AN_func(X, Y, DI)
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
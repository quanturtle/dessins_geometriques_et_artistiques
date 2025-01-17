import math
import turtle


def draw_rotating_curves(
    NP: int = 480,
    N: int = 2000,
    T1: int = 1,
    T2: int = 100,
    K1: int = 1,
    K2: int = 1,
    H1: int = 1,
    H2: int = 1,
    R1_FACTOR: float = 1/6,
    R2_FACTOR: float = 1/4
):
    R1 = NP * R1_FACTOR
    R2 = NP * R2_FACTOR

    for i in range(N + 1):
        S = math.cos(4 * math.pi * i / N) * 0.4 + 0.6

        AN = 2.0 * math.pi * i / N

        c1 = math.cos(H1 * AN * T1)
        s1 = math.sin(H2 * AN * T1)

        c2 = S * math.cos(K1 * AN * T2)
        s2 = S * math.sin(K2 * AN * T2)

        X = (NP / 2.0) + R1 * c1 + R2 * (c1 * c2 - s1 * s2)
        Y = (NP / 2.0) + R1 * s1 + R2 * (s1 * c2 + c1 * s2)

        if i == 0:
            turtle.penup()
            turtle.goto(int(X), int(Y))
            turtle.pendown()
        
        else:
            turtle.goto(int(X), int(Y))

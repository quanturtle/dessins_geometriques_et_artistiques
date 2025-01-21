import math
import turtle
from typing import Callable, Optional

def default_compute_z(x: float, y: float) -> float:
    return math.sin(math.pi * x) * math.sin(math.pi * y) * 50  # arbitrary scale

def draw_surface(
    N: int = 6,
    PA: Optional[float] = None,
    E1: int = 2,
    E2: int = 1,
    E3: int = 1,
    NP: int = 480,
    XA: float = None, YA: float = None,
    XB: float = None, YB: float = None,
    XC: float = None, YC: float = None,
    XD: float = None, YD: float = None,
    compute_z: Callable[[float, float], float] = default_compute_z,
    translate_x: float = 0.0,
    translate_y: float = 0.0
):
    if PA is None:
        PA = NP / 16

    if XA is None: XA = NP / 2
    if YA is None: YA = NP / 16
    if XB is None: XB = NP * 7/8
    if YB is None: YB = NP / 4
    if XC is None: XC = NP / 2
    if YC is None: YC = NP * 5/8
    if XD is None: XD = NP / 8
    if YD is None: YD = NP * 7/16

    tx = translate_x
    ty = translate_y

    M = int(NP / PA)

    max_array = [-5 * NP] * (M + 1)
    min_array = [ 5 * NP] * (M + 1)

    passes_done = 0
    while True:
        for i in range(M + 1):
            max_array[i] = -5 * NP
            min_array[i] =  5 * NP

        for i in range(N + 1):
            if N == 0: 
                continue

            XP = (i * XD + (N - i) * XA) / N
            YP = (i * YD + (N - i) * YA) / N
            XQ = (i * XC + (N - i) * XB) / N
            YQ = (i * YC + (N - i) * YB) / N

            i1 = int(XP / PA)
            i2 = int(XQ / PA)

            G = 1 if i2 - i1 >= 0 else -1

            J = i1
            done = False

            while not done:
                skip = False

                fraction = 0.0
                denom = (i2 - i1)

                if denom != 0:
                    fraction = (J - i1) / denom

                if E3 == 1:
                    X = fraction
                    Y = i / N

                else:
                    Y = fraction
                    X = i / N

                Z = compute_z(X, Y)

                XF = int(J * PA)

                if denom != 0:
                    YF = int(((J - i1) * YQ + (i2 - J) * YP) / denom + Z)

                else:
                    YF = int(YP + Z)

                if J == i1:
                    turtle.penup()
                    turtle.goto(XF + tx, YF + ty)
                    turtle.pendown()

                if E2 == 1:
                    turtle.goto(XF + tx, YF + ty)
                    skip = True

                if not skip:
                    if min_array[J] < YF < max_array[J]:
                        turtle.penup()
                        turtle.goto(XF + tx, YF + ty)
                        turtle.pendown()

                    else:
                        if YF > max_array[J]:
                            max_array[J] = YF

                        if YF < min_array[J]:
                            min_array[J] = YF

                        turtle.goto(XF + tx, YF + ty)

                if J == i2:
                    done = True
                else:
                    J += G

        if E1 == 1:
            break

        E3 = 1
        E1 = 1

        XD, XB = XB, XD
        YD, YB = YB, YD

        passes_done += 1
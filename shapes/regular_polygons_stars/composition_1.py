import math
from regular_star import draw_regular_star

def draw_composition_1(
    K1: int = 99,
    R1_FACTOR: float = 0.25,
    K: int = 7,
    H: int = 3,
    R_FACTOR: float = 0.25,
    A1: float = 0,
    AD: float = math.pi / 2,
    NP: int = 480
):
    DX = NP / 2
    DY = NP / 2
    R1 = NP * R1_FACTOR
    R = NP * R_FACTOR
    
    for I1 in range(K1):
        CX = DX + R1 * math.cos(2 * math.pi * I1 / K1 + A1)
        CY = DY + R1 * math.sin(2 * math.pi * I1 / K1 + A1)

        draw_regular_star(CX, CY, K, H, R, AD)
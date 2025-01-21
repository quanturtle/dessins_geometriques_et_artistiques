import math
import turtle
from typing import Callable


def default_YD_func(NP, R1, R2, AN, K):
    return NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN) 


def default_YA_func(NP, R1, R2, AN, K):
    return NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN + math.pi)


def draw_linear_sticks(N: int = 100,
                       M: int = 1,
                       K: int = 5,
                       R1: float = 480/4,
                       R2: float = 480*5/24,
                       YD_func: Callable = default_YD_func,
                       YA_func: Callable = default_YA_func,
                       NP: int = 480):
    for i in range(1, M + 1):
        for j in range(N):
            AN = 2 * j * math.pi / N
            
            XD = NP/2 + R1*math.cos(AN) + R2*math.cos(K*AN)
            YD = YD_func(NP, R1, R2, AN, K)
            
            XA = NP/2 + R1*math.cos(AN) + R2*math.cos(K*AN + math.pi)
            YA = YA_func(NP, R1, R2, AN, K)
            
            turtle.penup()
            turtle.goto(XD, YD)
            turtle.pendown()
            
            turtle.goto(XA, YA)
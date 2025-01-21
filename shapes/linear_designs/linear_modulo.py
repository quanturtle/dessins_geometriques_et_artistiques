import math
import turtle
from typing import Callable, Tuple

def default_I1_func(i, H, N) -> float:
    return i % N

def default_I2_func(i, H, N) -> float:
    return (H * i) % N


def draw_linear_modulo(N: int = 400,
                       M: int = 400,
                       K1: float = 4,
                       K2: float = 5,
                       H: int = 2,
                       I1_func: Callable = default_I1_func,
                       I2_func: Callable = default_I2_func,
                       NP: int = 480):    
    X = []
    Y = []
    
    for i in range(N):
        x = int(NP * 0.5 * (1 + math.sin(K1 * i * math.pi / N)))
        y = int(NP * 0.75 * (1 + math.cos(K2 * i * math.pi / N)))
        
        X.append(x)
        Y.append(y)
    
    for i in range(M):
        I1 = I1_func(i, H, N)
        I2 = I2_func(i, H, N)
        
        turtle.penup()
        turtle.goto(X[I1], Y[I1])
        turtle.pendown()
        
        turtle.goto(X[I2], Y[I2])
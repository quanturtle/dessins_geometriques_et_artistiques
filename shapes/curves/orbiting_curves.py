import math
import turtle


def draw_orbiting_curves(N: int = 2000,
                         T1: int = 2,
                         T2: int = 100,
                         K1: int = 1,
                         K2: int = 1,
                         R1: float = 480*0.25,
                         NP: int = 480):
    for i in range(N):
        R2 = NP * 0.2 * (1 - i/N)
        
        A1 = 2 * math.pi * i/N * T1
        A2 = 2 * math.pi * i/N * T2
        
        X = int(NP * 0.5 + R1 * math.cos(K1 * A1) + R2 * math.cos(A2))
        Y = int(NP * 0.5 + R1 * math.sin(K2 * A1) + R2 * math.sin(A2))
        
        if i == 0:
            turtle.penup()
            turtle.goto(X, Y)
            turtle.pendown()
        
        else:
            turtle.goto(X, Y)
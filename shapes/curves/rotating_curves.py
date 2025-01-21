import math
import turtle


def draw_rotating_curves(N: int = 2000,
                         T1: int = 1,
                         T2: int = 100,
                         K1: int = 1,
                         K2: int = 1,
                         H1: int = 1,
                         H2: int = 1,
                         R1: float = 480/6,
                         R2: float = 480/4,
                         use_scale: bool = True,
                         NP: int = 480):
    for i in range(N):
        S_ = math.cos(4 * math.pi * i/N) * 0.4 + 0.6 if use_scale else 1
        AN = 2 * math.pi * i/N
        
        C1 = math.cos(H1 * AN * T1)
        S1 = math.sin(H2 * AN * T1)
        
        C2 = S_ * math.cos(K1 * AN * T2)
        S2 = S_ * math.sin(K2 * AN * T2)
        
        X = NP/2 + R1*C1 + R2*(C1*C2 - S1*S2)
        Y = NP/2 + R1*S1 + R2*(S1*C2 + C1*S2)
        
        if i == 0:
            turtle.penup()
            turtle.goto(int(X), int(Y))
            turtle.pendown()
        
        else:
            turtle.goto(int(X), int(Y))

import math
import turtle


def draw_linear_modulo(N: int = 400,
                       M: int = 400,
                       K1: float = 4,
                       K2: float = 5,
                       H: int = 2,
                       NP: int = 480):    
    X = []
    Y = []
    
    for i in range(N):
        x = int(NP * 0.5 * (1 + math.sin(K1 * i * math.pi / N)))
        y = int(NP * 0.75 * (1 + math.cos(K2 * i * math.pi / N)))
        
        X.append(x)
        Y.append(y)
    
    for i in range(M):
        i1 = i % N
        i2 = (H * i) % N
        
        turtle.penup()
        turtle.goto(X[i1], Y[i1])
        turtle.pendown()
        
        turtle.goto(X[i2], Y[i2])
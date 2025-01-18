import math
import turtle


def draw_linear_modulo(NP: int = 480):
    N = 500
    K1 = 11/7
    K2 = 7/3
    H = 3
    
    M = N
    
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
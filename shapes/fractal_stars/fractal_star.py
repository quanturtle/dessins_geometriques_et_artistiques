import turtle
import math


def draw_etoiles_fractales(NP: int = 480):
    N = 5
    K = 5
    RA = 0.35
    LL = NP * 0.6
    AA = 4 * math.pi / 5
    
    X0 = NP/2
    Y0 = NP/2
    A0 = -AA
    
    turtle.penup()
    turtle.goto(int(X0), int(Y0))
    turtle.pendown()
    
    NN = N * (N - 1)**(K - 1) - 1
    
    for I in range(NN + 1):
        II = I
        H = 0
        
        while (II % (N - 1) == 0) and (H < K - 1):
            II //= (N - 1)
            H += 1
        
        L0 = LL * (RA ** (K - 1 - H))
        A0 += AA
        
        X0 = X0 + L0 * math.cos(A0)
        Y0 = Y0 + L0 * math.sin(A0)
        
        turtle.goto(int(X0), int(Y0))
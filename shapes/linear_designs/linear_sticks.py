import math
import turtle


def draw_linear_sticks(N: int = 100,
                       M: int = 1,
                       K: int = 5,
                       NP: int = 480):
    for i in range(1, M + 1):
        R1 = NP/4
        R2 = NP * 5/24
        
        for j in range(N):
            AN = 2 * j * math.pi / N
            
            XD = NP/2 + R1*math.cos(AN) + R2*math.cos(K*AN)
            YD = NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN)
            
            XA = NP/2 + R1*math.cos(AN) + R2*math.cos(K*AN + math.pi)
            YA = NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN + math.pi)
            
            turtle.penup()
            turtle.goto(XD, YD)
            turtle.pendown()
            turtle.goto(XA, YA)
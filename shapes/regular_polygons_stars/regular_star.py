import math
import turtle


def draw_regular_star(CX: float, CY: float, K: int, H: int, R: float, AD: float):
    for I in range(K):
        X = int(CX + R * math.cos(2 * I * H * math.pi / K + AD))
        Y = int(CY + R * math.sin(2 * I * H * math.pi / K + AD))
        
        if I == 0:
            turtle.penup()
        
        else:
            turtle.pendown()
        
        turtle.goto(X, Y)
    
    X = int(CX + R * math.cos(0 + AD))
    Y = int(CY + R * math.sin(0 + AD))
    
    turtle.pendown()
    turtle.goto(X, Y)
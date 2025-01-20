import math
import turtle


def draw_regular_star(CX: float = 240, 
                      CY: float = 240, 
                      K: int = 8, 
                      H: int = 3, 
                      R: float = 130, 
                      AD: float = math.pi / 2):
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
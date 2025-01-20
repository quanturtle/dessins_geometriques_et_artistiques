import math
import turtle


def draw_regular_polygon(CX: float = 240, 
                         CY: float = 240, 
                         K: int = 5, 
                         R = 240*0.45,
                         AD = math.pi/4,
                         NP: int = 480):
    for i in range(K + 1):
        x = CX + R * math.cos((2 * math.pi * i / K) + AD)
        y = CY + R * math.sin((2 * math.pi * i / K) + AD)
        
        if i == 0:
            turtle.penup()
        else:
            turtle.pendown()
        
        turtle.goto(x, y)
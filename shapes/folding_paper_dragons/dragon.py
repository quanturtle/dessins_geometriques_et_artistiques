import math
import turtle


def draw_dragon(N: int = 10, NP: int = 480):    
    A = [0] * (N + 1)
    X0 = NP/5
    Y0 = NP/5
    A0 = -math.pi/4 * (N-2)
    L0 = NP/math.pow(math.sqrt(2), N)
    
    X1 = X0
    Y1 = Y0
    X2 = X0
    Y2 = Y0
    
    def gosub():
        nonlocal X0, Y0, X1, Y1, X2, Y2
        X0 = X1
        Y0 = Y1
        X1 = X2
        Y1 = Y2
        X2 = X2 + L0 * math.cos(A0)
        Y2 = Y2 + L0 * math.sin(A0)
    
    turtle.penup()
    turtle.goto(X0, Y0)
    turtle.pendown()
    
    NN = pow(2, N) - 1
    
    for I in range(NN + 1):
        if I == 0:
            gosub()
    
        else:
            II = I
            J = 0
    
            while II % 2 == 0:
                II = II // 2
                J += 1
    
            AA = (A[N-J]*2-1) * (((II-1)//2)%2 * 2-1) * math.pi/2
            A0 += AA
    
            gosub()
        
        mid_x1 = (X0 + 3*X1)/4
        mid_y1 = (Y0 + 3*Y1)/4
        mid_x2 = (X2 + 3*X1)/4
        mid_y2 = (Y2 + 3*Y1)/4
        
        turtle.goto(mid_x1, mid_y1)
        turtle.goto(mid_x2, mid_y2)
import math
import turtle
from shapes import draw_horse


DATA = [
    1000, 10,10, 8,12, 9,16, 12,17, 13,18, 14,20,
    1000, 13,18, 12,19, 9,21, 9,20, 10,19, 9,17, 7,20, 8,22, 12,22,
    1000, 12,20, 12,22, 13,26, 16,31, 18,31, 19,32,
    1000, 16,31, 14,31, 14,32,
    1000, 14,31, 10,30, 12,31, 10,32, 10,34, 11,34, 11,33, 10,33,
    1000, 12,32, 13,31,
    1000, 10,34, 16,36,
    1000, 16,35, 16,37, 18,35, 17,34,
    1000, 17,36, 20,36, 22,32, 19,26,
    1000, 20,36, 22,36, 22,34, 24,32, 24,30, 19,26, 18,23, 21,22, 21,24,
    30,30, 34,31, 36,31, 33,26, 32,22, 28, 22, 27,20, 29,17, 30,19, 29,20,
    29,21, 32,19, 33,18, 32,17, 29,16, 28, 12, 30,10, 21,4, 21,2,
    18,3, 19,6, 24,10, 24,12, 22,14, 22,16, 23,17,
    1000, 22,16, 17,16, 16,17, 17,18,
    1000, 16,17, 16,16, 10,14, 10,12, 12,11, 10,10,
    1000, 21,21, 22,24, 30,30,
    1000, 24,24, 34,28,
    1000, 25,23, 33,26,
    1000, 25,21, 27,20,
    1000, 23,21, 24,19,
    1000, 27,20, 22,19, 22,21,
    1000, 22,19, 21,20,
    1000, 13,34, 15,35, 16,34, 16,33,
    1000, 15,35, 15,34, 16,34, 15,34, 15,35,
    1000, 24,12, 26,10, 19,5, 19,3,
    1000, 28,22, 25,22,
    2000
]


def sgn(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def design_34():
    draw_horse()
                

def design_35(NP: int = 480):
    i = 0
    B1 = 0

    for I in range(6):
        AN = 2 * I * math.pi / 6 + math.pi / 12
        CO = math.cos(AN)
        SI = math.sin(AN)

        while True:
            A = DATA[i % len(DATA)]
            i += 1

            if A == 2000:
                break

            if A == 1000:
                B1 = 0
                A = DATA[i % len(DATA)]
                i += 1
                B = DATA[i % len(DATA)]
                i += 1
            
            else:
                B = DATA[i % len(DATA)]
                i += 1

            X = int(NP * (0.5 + CO * A/90.0 - SI * B/90.0))
            Y = int(NP * (0.5 + SI * A/90.0 + CO * B/90.0))

            if B1 == 0:
                turtle.penup()
                turtle.goto(X - NP // 2, Y - NP // 2)
                B1 = 1
            
            else:
                turtle.pendown()
                turtle.goto(X - NP // 2, Y - NP // 2)    


def design_36(NP: int = 480):
    i = 0
    B1 = 0

    for I in range(6):
        for J in range(2):
            while True:
                A = DATA[i % len(DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = DATA[i % len(DATA)]
                    i += 1
                    B = DATA[i % len(DATA)]
                    i += 1
                
                else:
                    B = DATA[i % len(DATA)]
                    i += 1

                X = int(NP/2 + (1-2*J) * NP*A/80 * (0.5**I))
                Y = int(NP - NP*0.5**I + NP*B/80 * (0.5**I))

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1
                
                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)


# TODO: bug here
def design_37(NP: int = 480):
    i = 0
    B1 = 0
    
    for I in range(16):
        AN = 2 *I * math.pi/6 + math.pi/12
        CO = math.cos(AN)
        SI = math.sin(AN)
        
        R = 0.87 ** I
        
        while True:
            A = DATA[i % len(DATA)]
            i += 1

            if A == 2000:
                break

            if A == 1000:
                B1 = 0
            
                A = DATA[i % len(DATA)]
                i += 1
            
                B = DATA[i % len(DATA)]
                i += 1
            
            else:
                B = DATA[i % len(DATA)]
                i += 1

            X_coord = 0.5 + R * ((CO * 0.15 + A / 110.0) - (SI * 0.15 + B / 110.0))
            Y_coord = 0.5 + R * ((SI * 0.15 + A / 110.0) + (CO * 0.15 + B / 110.0))
            
            X = int(NP * X_coord)
            Y = int(NP * Y_coord)
            
            if B1 == 0:
                turtle.penup()
                turtle.goto(X - NP // 2, Y - NP // 2)
                B1 = 1
            
            else:
                turtle.pendown()
                turtle.goto(X - NP // 2, Y - NP // 2)
    
    
def design_38(NP: int = 480):
    i = 0
    B1 = 0

    for I in range(6):
        for J in range(2**I-1):
            while True:
                A = DATA[i % len(DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = DATA[i % len(DATA)]
                    i += 1
                    B = DATA[i % len(DATA)]
                    i += 1
                
                else:
                    B = DATA[i % len(DATA)]
                    i += 1

                X = int((J+A/20) * NP*(0.5**I))
                Y = int((2-2*.5**I) * NP+B/40 * NP*(0.5**I))

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1
                
                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)
    
    
def design_39(NP: int = 480):
    i = 0
    B1 = 0

    for I in range(3):
        for J in range(3):
            while True:
                A = DATA[i % len(DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = DATA[i % len(DATA)]
                    i += 1
                    B = DATA[i % len(DATA)]
                    i += 1
                
                else:
                    B = DATA[i % len(DATA)]
                    i += 1

                X = int(NP * (A+J*20) / 80)
                Y = int(NP * (B+I*20) / 80)

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1
                
                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)
    
    
def design_40(NP: int = 480):
    i = 0
    B1 = 0

    N = 4
    for I in range(-N, N+1):
        for J in range(-abs(I), abs(I)+1):
            while True:
                A = DATA[i % len(DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = DATA[i % len(DATA)]
                    i += 1
                    B = DATA[i % len(DATA)]
                    i += 1
                
                else:
                    B = DATA[i % len(DATA)]
                    i += 1

                XX = (A+ J*20 -20) / 100
                YY = (B+ I*20 -20) / 100
                
                X = int(NP/2 * (XX+1))
                Y = int(NP/2 * (YY+1))

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1
                
                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)
    

# TODO: fix here
def design_41(NP: int = 480):
    i = 0
    B1 = 0

    N = 4
    for I in range(-N, N+1):
        for J in range(-I, I+1):
            while True:
                A = DATA[i % len(DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = DATA[i % len(DATA)]
                    i += 1
                    B = DATA[i % len(DATA)]
                    i += 1
                
                else:
                    B = DATA[i % len(DATA)]
                    i += 1

                XX = (A+ J*20 -20) / 100
                YY = (B+ I*20 -20) / 100
                
                X = int(NP/2 * (XX+1) * abs(XX+1))
                Y = int(NP/2 * (YY+1) * abs(YY+1))

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1
                
                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)
    

# TODO: fix here
def design_42(NP: int = 480):
    i = 0
    B1 = 0

    N = 4
    for I in range(-N, N+1):
        for J in range(-I, I+1):
            while True:
                A = DATA[i % len(DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = DATA[i % len(DATA)]
                    i += 1
                    B = DATA[i % len(DATA)]
                    i += 1
                
                else:
                    B = DATA[i % len(DATA)]
                    i += 1
                
                X = NP * A+J*20 -20 / 80
                Y = NP * B+I*20 -20 / 80
                
                DI = math.sqrt(X * X + Y * Y)
                
                if X != 0:
                    AN = math.atan(Y / X) + math.pi * (1 - sgn(X)) / 2
                
                else:
                    AN = math.pi/2 * sgn(Y)

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1
                
                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)
    
    
def design_43(NP: int = 480):
    i = 0
    B1 = 0

    N = 4
    for I in range(-N, N+1):
        for J in range(-N, N+1):
            while True:
                A = DATA[i % len(DATA)]
                i += 1

                if A == 2000:
                    break

                if A == 1000:
                    B1 = 0
                    A = DATA[i % len(DATA)]
                    i += 1
                    B = DATA[i % len(DATA)]
                    i += 1
                
                else:
                    B = DATA[i % len(DATA)]
                    i += 1
                
                XX = A+J*20 -20 / 1000
                YY = B+I*20 -20 / 1000
                
                X = int((abs(XX)**0.7*sgn(XX)+1) * NP/2)
                Y = int((abs(YY)**0.7*sgn(YY)+1) * NP/2)

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X - NP // 2, Y - NP // 2)
                    B1 = 1
                
                else:
                    turtle.pendown()
                    turtle.goto(X - NP // 2, Y - NP // 2)
import math
import turtle


def draw_lion(NP: int = 480):
    DATA = [
        1000, -2.5,0, -2,1, - 1,2, 0,7, 1,7, 2,8, 2,11, 3,14, 3.5,13.5,2.5,11, 2.5,9,
        1000, 3.5,13.5, 4,13, 3,11, 3,9, 3,11, 4,13, 5,12, 3.5,11, 3.5,9,3.5,11, 5,12, 5,11, 4,10, 4,9,8,9, 7,11, 8,13, 10,14, 12,13, 13, 11, 12, 11,11,10, 12,8, 13,7, 14,2,15,2, 16,1, 16,0, 12,0, 12,2, 11,5, 11.5,6, 11,5, 9,3, 9,2, 10,1,10,0, 6,0, 7,2, 8,6, 7,2, 6,4, 4,5, 5,7, 4,8,5,7, 4,5, 2,4, 1,2, 2,2, 3,1, 2.5,0, -2.5,0,
        1000, 6,4, 7.5,3.5,
        1000, 12,11, 10,10.5, 9,10.5,
        1000, 12.5,12, 12,12, 11,11.5,12,12, 12,12.5, 11.5,12.5, 10.5,13,10, 13, 10,13.5, 10.5,13.5, 10.5,13, 11.5,12.5,12,12.5, 12,13,
        1000,7.5,12, 8.5,12, 8.5,11.5,
        2000
    ]
    i  = 0
    B1 = 0

    while True:
        A = DATA[i]
        i += 1
        
        if A == 2000:
            break

        if A == 1000:
            B1 = 0
            A = DATA[i]; i += 1
            B = DATA[i]; i += 1

        else:
            B = DATA[i]
            i += 1

        X = int(NP * (A + 5) / 25)
        Y = int(NP * (B + 5) / 25)

        if B1 == 0:
            turtle.penup()
            turtle.goto(X, Y)
            B1 = 1
        
        else:
            turtle.pendown()
            turtle.goto(X, Y)
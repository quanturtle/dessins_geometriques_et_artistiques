import turtle


def draw_bird_fish(NP: int = 480):
    DATA = [
        1000,0,0, 2,0, 4,1, 4,2, 3,2, 2,3, 4,5, 4,6, 2,5, 2,6, -1,5, -2,3, -1,2, -2,2, -3,3, -4,3, -5,2, -4,2, 0,0,
        1000,-5,2, -5,1, -7,-1, -6,-2, -5,-2, -5,-3, -2,-2, -2,-3, 0,-2, 1,-1, 2, -1, 3,-2, 4,-2, 3,-1, 4,1,
        1000, 2,5, 0,4, 0,2,
        1000, -2,1, -5,1, -4,-1, -3,0, -3,-1, -4,-1, -5,-2, 0,-2,
        1000, -7,-1, -6,-1,
        1000,-4,2.5, -4,2.8, -4.3,2.8, -4.3,2.5, -4,2.5,
        1000, -5,0, -5.5,0, -5.5,0.5, -5,0.5,  -5,0,
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

        X = int(NP * (A + 10) / 15)
        Y = int(NP * (B + 10) / 15)

        if B1 == 0:
            turtle.penup()
            turtle.goto(X, Y)
            B1 = 1
        
        else:
            turtle.pendown()
            turtle.goto(X, Y)
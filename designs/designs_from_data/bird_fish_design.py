import turtle
from shapes.designs_from_data import draw_bird_fish


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


def design_46():
    draw_bird_fish()
    

def design_47(NP: int = 480):
    i  = 0
    B1 = 0

    for I in range(5):
        for J in range(5):
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

                X = int(NP*(B+4*I+4*J)/45)
                Y = int(NP*(A+15-5*I+9*J)/45)

                if B1 == 0:
                    turtle.penup()
                    turtle.goto(X, Y)
                    B1 = 1
                
                else:
                    turtle.pendown()
                    turtle.goto(X, Y)
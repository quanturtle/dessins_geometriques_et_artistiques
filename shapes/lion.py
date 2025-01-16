import turtle
import math

def setup_canvas(NP: int = 480):
    """
    Sets a window of size NP x NP in 'turtle' coordinates.
    """
    turtle.setup(width=NP, height=NP)
    turtle.setworldcoordinates(0, 0, NP, NP)
    turtle.speed("fastest")
    turtle.penup()
    turtle.home()
    turtle.pendown()

def draw_lion():
    """
    Python turtle version of the BASIC 'LION' program.
    Replicates reading logic and draws lines accordingly.
    The data below matches the BASIC listing for LION.
    """

    data = [
        # From 1000 DATA
        1000, -2.5,0,  -2,1,  -1,2,  0,7,  1,7,  2,8,  2,11, 3,14, 3.5,13.5,
        # From 1010 DATA
        2.5,11, 2.5,9,
        
        # From 1020 DATA
        1000, 3.5,13.5, 4,13, 3,11, 3,9, 3,11, 4,13, 5,12, 3.5,11, 3,5,9, 
        # (The above line has a slight ambiguity with `3,5,9`; 
        #  you may need to verify these last pairs if you see odd results.)
        
        # From 1030 DATA
        3.5,11, 5,12, 5,11, 4,10, 4,9, 8,9, 7,11, 8,13, 10,14, 12,13, 13,11,
        
        # From 1040 DATA
        12,11, 11,10, 12,8, 13,7, 14,2, 15,2, 16,1, 16,0, 12,0, 12,2, 11,5,
        
        # From 1050 DATA
        11.5,6, 11.5,9, 3,9, 9,2, 10,1, 10,0, 6,0, 7,2, 8,6, 7,2, 6,4, 4,5,
        
        # From 1060 DATA
        5,7, 4,8.5, 7, 4,5, 2,4, 1,2, 2,2, 3,1, 2,5,0, -2.5,0,
        
        # From 1070 DATA
        1000, 6,4, 7.5,3.5,
        
        # From 1080 DATA
        1000, 12,11, 10,10.5, 9,10.5,
        
        # From 1090 DATA
        1000, 12.5,12, 12,12, 11,11.5, 12,12, 12,12.5, 11.5,12.5, 10.5,13,
        10,13, 10,13.5, 10,5,13.5, 10,5,13, 11.5,12.5, 12,12.5, 12,13,
        
        # From 1110 DATA
        1000, 7.5,12, 8.5,12, 8.5,11.5,
        
        # From 1200 DATA
        2000
    ]

    NP = 480
    i  = 0           # index into data list
    B1 = 0           # BASIC's "B1" to track "move vs draw"

    while True:
        A = data[i]
        i += 1
        
        # 2000 => stop reading
        if A == 2000:
            break

        # If it's 1000 => next pair is a move-to
        if A == 1000:
            B1 = 0
            A = data[i]; i += 1  # read next X
            B = data[i]; i += 1  # read next Y
        else:
            # Otherwise, 'A' is X, read next for Y
            B = data[i]
            i += 1

        X = int(NP * (A + 5) / 25)
        Y = int(NP * (B + 5) / 25)

        # B1=0 => pen up + goto => then B1=1
        # B1=1 => pen down + goto
        if B1 == 0:
            turtle.penup()
            turtle.goto(X, Y)
            B1 = 1
        else:
            turtle.pendown()
            turtle.goto(X, Y)

    turtle.hideturtle()
    turtle.exitonclick()

setup_canvas()
draw_lion()

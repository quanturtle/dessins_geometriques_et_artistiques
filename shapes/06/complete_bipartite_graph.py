import turtle


def setup_canvas(NP=480):
    """
    Sets a window of size NP x NP in 'turtle' coordinates.
    """
    turtle.setup(width=NP, height=NP)
    turtle.setworldcoordinates(0, 0, NP, NP)
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def draw_biparti_complet():
    """
    Python turtle version of the BASIC 'BIPARTI COMPLET' program.
    """

    NP = 480
    N  = 10

    # From the BASIC code:
    #   A = (XA, YA) = (0,   0)
    #   B = (XB, YB) = (0,   NP)
    #   C = (XC, YC) = (NP, 0)
    #   D = (XD, YD) = (NP, NP)

    XA, YA = 0, 0
    XB, YB = 0, NP
    XC, YC = NP, 0
    XD, YD = NP, NP

    # Outer loop: i = 0..N
    for i in range(N + 1):
        # Compute a point X1, Y1 on the segment A->B
        #   X1 = (i*XA + (N-i)*XB)/N
        #   Y1 = (i*YA + (N-i)*YB)/N
        X1 = (i * XA + (N - i) * XB) / N
        Y1 = (i * YA + (N - i) * YB) / N
        
        # Convert to int for drawing
        x_start = int(X1)
        y_start = int(Y1)

        # Inner loop: j = 0..N
        for j in range(N + 1):
            # "M x_start, y_start" => pen up & move
            turtle.penup()
            turtle.goto(x_start, y_start)
            
            # Then compute X2, Y2 on the segment C->D
            #   X2 = (j*XC + (N-j)*XD)/N
            #   Y2 = (j*YC + (N-j)*YD)/N
            X2 = (j * XC + (N - j) * XD) / N
            Y2 = (j * YC + (N - j) * YD) / N

            x_end = int(X2)
            y_end = int(Y2)

            # "D x_end, y_end" => pen down & draw
            turtle.pendown()
            turtle.goto(x_end, y_end)

    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas()
draw_biparti_complet()
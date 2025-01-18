import turtle

def draw_complete_bipartite_graph(N: int = 10, NP: int = 480):
    XA, YA = 0, 0
    XB, YB = 0, NP
    XC, YC = NP, 0
    XD, YD = NP, NP

    for i in range(N + 1):
        X1 = (i * XA + (N - i) * XB) / N
        Y1 = (i * YA + (N - i) * YB) / N
        
        x_start = int(X1)
        y_start = int(Y1)

        for j in range(N + 1):
            turtle.penup()
            turtle.goto(x_start, y_start)
            
            X2 = (j * XC + (N - j) * XD) / N
            Y2 = (j * YC + (N - j) * YD) / N

            x_end = int(X2)
            y_end = int(Y2)

            turtle.pendown()
            turtle.goto(x_end, y_end)
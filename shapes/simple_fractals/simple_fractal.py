import math
import turtle


def draw_simple_fractal():
    NP = 480
    M = 3
    N = 4
    K = 4

    X = [0]*(M+1)
    Y = [0]*(M+1)
    L_array = [0]*N
    A_array = [0]*N

    X[0] = 0
    X[1] = NP
    X[2] = NP * 0.5
    X[3] = 0

    Y[0] = 0
    Y[1] = 0
    Y[2] = math.sqrt(3)/2 * NP
    Y[3] = Y[0]

    for idx in range(N):
        L_array[idx] = 1/3

    A_array[0] = 0
    A_array[1] = math.pi / 3
    A_array[2] = -math.pi / 3
    A_array[3] = 0

    for II in range(M):
        XD = X[II]
        YD = Y[II]
        XA = X[II+1]
        YA = Y[II+1]

        X0 = XD
        Y0 = YD
        
        turtle.penup()
        turtle.goto(int(X0), int(Y0))
        turtle.pendown()

        A0 = math.atan2(YA - YD, XA - XD)
        L0 = math.sqrt((XA - XD)**2 + (YA - YD)**2)

        for I in range(0, N**K):
            LL = L0
            AA = A0
            T = I

            for J in range(K-1, -1, -1):
                R_val = N**J
                T2 = T // R_val
                AA += A_array[T2]
                LL *= L_array[T2]
                T = T - T2 * R_val

            X0 = X0 + LL * math.cos(AA)
            Y0 = Y0 + LL * math.sin(AA)
            
            turtle.pendown()
            turtle.goto(int(X0), int(Y0))
import math
import turtle


def draw_rounded_corner(X0, Y0, X1, Y1, X2, Y2, S, I):
    UX = X1 - X0
    UY = Y1 - Y0
    WX = X2 - X1
    WY = Y2 - Y1

    for K4 in range(S + 1):
        AN = math.pi / 2 * K4 / S
        CO = math.cos(AN)
        SI = math.sin(AN)
        X = (X0 + X2 + CO * (-WX) + SI * UX) / 2
        Y = (Y0 + Y2 + CO * (-WY) + SI * UY) / 2

        if I == 0 and K4 == 0:
            turtle.penup()
            turtle.goto(int(X), int(Y))
            turtle.pendown()

        else:
            turtle.goto(int(X), int(Y))


def draw_fractales_simples_arrondies():
    NP = 480
    M = 1
    N = 7
    K = 2
    S = 5

    X = [0] * (M + 1)
    Y = [0] * (M + 1)
    L_array = [0] * N
    A_array = [0] * N

    X[0] = 0
    X[1] = 0
    Y[0] = NP
    Y[1] = -NP

    L_array[0] = 1 / 2
    L_array[1] = 1 / 4
    L_array[2] = 1 / 4
    L_array[3] = 1 / 4
    L_array[4] = 1 / 4
    L_array[5] = 1 / 2
    L_array[6] = 1 / 2

    A_array[0] = 0
    A_array[1] = math.pi / 2
    A_array[2] = -math.pi
    A_array[3] = 0
    A_array[4] = math.pi / 2
    A_array[5] = -math.pi / 2
    A_array[6] = 0

    for II in range(M):
        XD = X[II]
        YD = Y[II]
        XA = X[II + 1]
        YA = Y[II + 1]

        X0 = XD
        X1 = X0
        X2 = X0
        Y0 = YD
        Y1 = Y0
        Y2 = Y0

        if XA != XD:
            A0 = math.atan2(YA - YD, XA - XD)

        else:
            A0 = math.pi / 2 * math.copysign(1, YA - YD)

        if (XA - XD) < 0:
            A0 += math.pi

        L0 = math.sqrt((XA - XD)**2 + (YA - YD)**2)

        for I in range(0, N**K):
            LL = L0
            AA = A0
            T = I

            for J in range(K - 1, -1, -1):
                R = N**J
                T2 = T // R
                AA += A_array[T2]
                LL *= L_array[T2]
                T -= T2 * R

            X0 = X1
            X1 = X2
            X2 = X2 + LL * math.cos(AA)
            Y0 = Y1
            Y1 = Y2
            Y2 = Y2 + LL * math.sin(AA)

            draw_rounded_corner(X0, Y0, X1, Y1, X2, Y2, S, I)
import math
import turtle


def deformation_subroutine(X0: int, Y0: int, NP: int = 480):
    XH = X0 / NP * 2 - 1
    YH = Y0 / NP * 2 - 1
    DH = math.sqrt(XH * XH + YH * YH)

    if XH != 0:
        AH = math.atan2(YH, XH)
    else:
        AH = math.pi / 2 * math.copysign(1, YH)

    DH = DH**2
    X1 = int((DH * math.cos(AH) + 1) * NP / 2)
    Y1 = int((DH * math.sin(AH) + 1) * NP / 2)

    return X1, Y1


def draw_fractales_simples_deformees(NP: int = 480):
    M = 3
    N = 4
    K = 4

    X = [0] * (M + 1)
    Y = [0] * (M + 1)
    L_array = [0] * N
    A_array = [0] * N

    for IJ in range(4):
        X[IJ] = NP / 2 * (1 + math.sin(2 * IJ * math.pi / 3))
        Y[IJ] = NP / 2 * (1 + math.cos(2 * IJ * math.pi / 3))

    for idx in range(N):
        L_array[idx] = 1 / 3

    A_array[0] = 0
    A_array[1] = math.pi / 3
    A_array[2] = -math.pi / 3
    A_array[3] = 0

    for II in range(M):
        XD = X[II]
        YD = Y[II]
        XA = X[II + 1]
        YA = Y[II + 1]

        X0 = XD
        Y0 = YD

        X1, Y1 = deformation_subroutine(X0, Y0, NP)
        turtle.penup()
        turtle.goto(X1, Y1)
        turtle.pendown()

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

            X0 = X0 + LL * math.cos(AA)
            Y0 = Y0 + LL * math.sin(AA)

            X1, Y1 = deformation_subroutine(X0, Y0, NP)
            turtle.goto(X1, Y1)
import math
import turtle


def draw_simple_fractal(M: int = 3,
                        N: int = 4,
                        K: int = 4,
                        NP: int = 480,
                        X: list = None,
                        Y: list = None,
                        L_array: list = None,
                        A_array: list = None,
                        translateX: float = 0.0,
                        translateY: float = 0.0):
    if X is None:
        X = [0, NP, NP*0.5, 0]
    
    if Y is None:
        Y = [math.sqrt(3)/2 * NP, math.sqrt(3)/2 * NP, 0, math.sqrt(3)/2 * NP]
    
    if L_array is None:
        L_array = [1/3] * N

    if A_array is None:
        A_array = [0, math.pi/3, -math.pi/3, 0]

    for II in range(M):
        XD = X[II]
        YD = Y[II]
        XA = X[II + 1]
        YA = Y[II + 1]

        X0 = XD
        Y0 = YD

        turtle.goto(int(X0 + translateX), int(Y0 + translateY))
        turtle.pendown()

        A0 = math.atan2(YA - YD, XA - XD)
        L0 = math.sqrt((XA - XD)**2 + (YA - YD)**2)

        for I in range(N**K):
            LL = L0
            AA = A0

            T1 = I

            if K == 0:
                X0 += LL * math.cos(AA)
                Y0 += LL * math.sin(AA)
                turtle.goto(int(X0 + translateX), int(Y0 + translateY))

            else:
                for J in range(K - 1, -1, -1):
                    R_val = N**J
                    T2 = T1 // R_val
                    AA += A_array[T2]
                    LL *= L_array[T2]
                    T1 -= T2 * R_val

                X0 += LL * math.cos(AA)
                Y0 += LL * math.sin(AA)
                turtle.goto(int(X0 + translateX), int(Y0 + translateY))


#
# Example usage:
#
# Suppose we want the classic Koch-like fractal (DESSIN=115). That means:
# M=3, 
# N=4, 
# K=1, 
# X=[0, NP, NP/2, 0], 
# Y=[√3/2 NP, √3/2 NP, 0, √3/2 NP],
# L=[1/3, 1/3, 1/3, 1/3], 
# A=[0, π/3, -π/3, 0]
#
#   draw_simple_fractal()
#
# or define your own parameters to replicate other fractals from the JS code.
#
if __name__ == "__main__":
    # Clear the screen, set a coordinate system, and draw the default fractal:
    turtle.reset()
    # Optionally: turtle.setworldcoordinates(0, 0, 480, 480)
    draw_simple_fractal()
    turtle.done()

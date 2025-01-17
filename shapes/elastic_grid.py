import turtle
import math

def setup_canvas(width=750):
    """Sets up the turtle canvas with given width"""
    turtle.setup(width=width, height=width)
    turtle.setworldcoordinates(0, 0, width, width)
    turtle.speed(0)  # Fastest speed

def draw_elastic_grid(DESSIN=164):
    NP = 480
    PI = math.pi
    
    def sgn(x):
        return 1 if x > 0 else -1 if x < 0 else 0
    
    turtle.clear()
    turtle.speed(0)
    
    for L in range(2):  # 0 to 1
        for I in range(21):  # 0 to 20
            for J in range(21):  # 0 to 20
                X = I/10 - 1
                Y = J/10 - 1
                
                if L == 1:
                    X, Y = Y, X  # Swap X and Y
                    
                DI = math.sqrt(X*X + Y*Y)
                
                if X != 0:
                    AN = math.atan(Y/X)
                else:
                    AN = PI/2 * sgn(Y)
                    
                if X < 0:
                    AN = AN + PI
                    
                # Apply transformations based on DESSIN value
                if DESSIN == 164:
                    if DI < 1:
                        DI = math.pow(DI, 0.3)
                elif DESSIN == 165:
                    if DI < 1:
                        DI = math.pow(DI, 3)
                elif DESSIN == 166:
                    if DI < 1:
                        AN = AN + PI/2*(1-DI)
                elif DESSIN == 167:
                    if DI < 1:
                        AN = AN + 3.5*(1-DI)
                        DI = math.pow(DI, 0.3)
                elif DESSIN == 168:
                    if DI < 1:
                        AN = AN + 2*PI*(1-DI)
                elif DESSIN == 169:
                    if DI < 1:
                        AN = AN + PI*(1-DI)
                        DI = math.pow(DI, 3)
                elif DESSIN == 170:
                    if DI < 1:
                        AN = AN + PI/2*math.sin(PI*(1-DI))
                        DI = math.pow(DI, 0.2)
                elif DESSIN == 171:
                    if DI < 1:
                        AN = AN + PI/4*math.sin(2*PI*(1-DI))
                elif DESSIN == 172:
                    if DI < 1:
                        AN = AN + PI/4*math.sin(2*PI*(1-DI))
                        DI = math.pow(DI, 2)
                elif DESSIN == 173:
                    if DI < 1:
                        AN = AN + PI/4*math.sin(2*PI*(1-DI))
                
                X = DI * math.cos(AN)
                Y = DI * math.sin(AN)
                
                X_ = int(NP/2 * (1 + 0.95*X))
                Y_ = int(NP/2 * (1 + 0.95*Y))
                
                if J == 0:
                    turtle.penup()
                    turtle.goto(X_, Y_)
                else:
                    turtle.pendown()
                    turtle.goto(X_, Y_)

    turtle.hideturtle()
    turtle.exitonclick()

setup_canvas()
draw_elastic_grid(DESSIN=164)
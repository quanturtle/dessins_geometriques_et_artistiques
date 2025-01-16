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
    turtle.goto(0, 0)
    turtle.pendown()


def draw_etoiles_fractales():
    """
    Python turtle version of the BASIC 'ÉTOILES FRACTALES' program.
    """

    NP = 480
    PI = math.pi

    # From line 100 in BASIC
    N  = 5
    K  = 5
    RA = 0.35
    LL = NP
    AA = 4 * PI / 5  # 144 degrees

    # From line 110
    X0 = (NP - LL) / 2    # => (480 - 480)/2 = 0, effectively
    Y0 = NP / 4           # => 480/4 = 120
    A0 = -AA              # => start angle: -144 degrees

    # "Move" to (X0,Y0)
    turtle.penup()
    turtle.goto(int(X0), int(Y0))
    turtle.pendown()

    # From line 190: NN = N*(N-1)^(K-1) - 1
    NN = N * (N - 1)**(K - 1) - 1

    # Main loop: line 200 FOR I=0 TO NN
    for I in range(NN + 1):
        # line 210: II = I, H=0
        II = I
        H  = 0
        
        # line 300: 
        #   while (II mod (N-1))=0 and H<(K-1) => II=II/(N-1), H++
        while (II % (N - 1) == 0) and (H < K - 1):
            II //= (N - 1)
            H  += 1

        # line 310: L0 = LL * RA^(K-1-H)
        L0 = LL * (RA ** (K - 1 - H))

        # line 320: A0 = A0 + AA
        A0 += AA

        # lines 330-340: X0,Y0 = X0 + L0*cos(A0), Y0 + L0*sin(A0)
        X0 = X0 + L0 * math.cos(A0)
        Y0 = Y0 + L0 * math.sin(A0)

        # line 350: "D" => draw line to (X0, Y0)
        turtle.goto(int(X0), int(Y0))

    # End
    turtle.hideturtle()
    turtle.exitonclick()


setup_canvas(700)
draw_etoiles_fractales()
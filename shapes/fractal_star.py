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
    Centered on the canvas.
    """
    NP = 480
    PI = math.pi
    
    # Basic parameters
    N = 5
    K = 5
    RA = 0.35
    LL = NP * 0.6  # Reduced size to ensure it fits in center
    AA = 4 * PI / 5  # 144 degrees
    
    # Centered starting position
    X0 = NP/2  # Center X
    Y0 = NP/2  # Center Y
    A0 = -AA   # Start angle: -144 degrees
    
    # Move to starting position
    turtle.penup()
    turtle.goto(int(X0), int(Y0))
    turtle.pendown()
    
    # Calculate number of iterations
    NN = N * (N - 1)**(K - 1) - 1
    
    # Main drawing loop
    for I in range(NN + 1):
        II = I
        H = 0
        
        # Calculate depth
        while (II % (N - 1) == 0) and (H < K - 1):
            II //= (N - 1)
            H += 1
        
        # Calculate length and angle
        L0 = LL * (RA ** (K - 1 - H))
        A0 += AA
        
        # Calculate new position
        X0 = X0 + L0 * math.cos(A0)
        Y0 = Y0 + L0 * math.sin(A0)
        
        # Draw line to new position
        turtle.goto(int(X0), int(Y0))

    turtle.hideturtle()
    turtle.exitonclick()

setup_canvas(600)
draw_etoiles_fractales()
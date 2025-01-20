import turtle
import math


def draw_d3data(DESSIN=201):
    NP = 480
    PI = math.pi
    DC = 2
    TC = 2
    
    OX, OY, OZ = 5, -2, 1.3
    AZ, AY, AX = 3*PI/4, 0, 0
    QX, QY, QZ = 0, 0, 0
    
    if DESSIN == 202:
        OX, OY, OZ = 5, -2, 6
        AZ, AY, AX = 3*PI/4, -PI/4, 4
    elif DESSIN == 203:
        OX, OY, OZ = 5, -3, 0
        AZ, AY, AX = 3*PI/4, PI/4, 4
    elif DESSIN == 205:
        OX, OY, OZ = 0, 0, 0
        AZ, AY, AX = -PI/4, 0, 0
        QX, QY, QZ = 0, 1, 0
    
    C1, S1 = math.cos(AZ), -math.sin(AZ)
    C2, S2 = math.cos(AY), -math.sin(AY)
    C3, S3 = math.cos(AX), -math.sin(AX)
    
    DATA = [
        0,0,0, 0,0,2, 1,0,3, 1,0,4, 2,0,4,
        2,0,3, 3,0,2, 3,0,0, 3,1,0, 3,1,2,
        2,1,3, 2,1,4, 2,0,4, 1.5,.5,5.5, 1,0,4, 1000,
        0,0,0, 3,0,0, 1000,
        1,0,0, 1,0,1, 1.25,0,1.3, 1.75,0,1.3, 2,0,1, 2,0,0, 1000,
        3,0,2, 3,1,2, 1000,
        2,0,3, 2,1,3, 1000,
        2,1,4, 1.5,.5,5.5, 2000,
        1,1,4, 1,1,3, 0,1,2, 0,1,0, 3,1,0, 1000,
        0,0,0, 0,1,0, 1000,
        0,0,2, 0,1,2, 1000,
        1,0,3, 1,1,3, 1000,
        1,0,4, 1,1,4, 2,1,4, 2000
    ]
    
    data_index = 0
    B1 = 0
    
    def read_data():
        nonlocal data_index
        value = DATA[data_index]
        data_index += 1
        return value
    
    def perspective_transform(MX, MY, MZ):
        nonlocal B1
        MX, MY, MZ = MX-OX, MY-OY, MZ-OZ
        
        UU = MX
        MX = C1*UU - S1*MY
        MY = S1*UU + C1*MY
        
        UU = MX
        MX = C2*UU - S2*MZ
        MZ = S2*UU + C2*MZ
        
        UU = MY
        MY = C3*UU - S3*MZ
        MZ = S3*UU + C3*MZ
        
        MX, MY, MZ = MX-QX, MY-QY, MZ-QZ
        
        KP = DC/MX
        XX, YY = -KP*MY, KP*MZ
        X_ = int(NP * (0.5 + XX/TC))
        Y_ = int(NP * (0.5 + YY/TC))
        
        if B1 == 1:
            turtle.pendown()

        else:
            turtle.penup()
            B1 = 1
        
        turtle.goto(X_, Y_)
    
    turtle.clear()

    while True:
        MX = read_data()

        if MX == 2000:
            break

        if MX == 1000:
            B1 = 0
            MX = read_data()

        MY = read_data()
        MZ = read_data()
        perspective_transform(MX, MY, MZ)
    
    if DESSIN == 202:
        turtle.penup()
        turtle.setworldcoordinates(0, -NP*1.25, 750, 750-NP*1.25)

    elif DESSIN == 203:
        turtle.penup()
        turtle.setworldcoordinates(0, 100, 750, 850)
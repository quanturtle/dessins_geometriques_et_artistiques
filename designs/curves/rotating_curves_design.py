import math
from shapes import draw_rotating_curves


def design_87():
    draw_rotating_curves()
    
    
def design_88():
    draw_rotating_curves(N=3000, 
                         T1=1, 
                         T2=100, 
                         K1=1, 
                         K2=2, 
                         H1=1, 
                         H2=1, 
                         R1=480/3, 
                         R2=480/7,
                         S_func=lambda i, N: 1,
                         NP=480)
    
    
def design_89():
    draw_rotating_curves(N=3000, 
                         T1=0.5, 
                         T2=30, 
                         K1=1, 
                         K2=3, 
                         H1=1, 
                         H2=1, 
                         R1=480/8, 
                         R2=480*0.27,
                         S_func=lambda i, N: 1,
                         NP=480)    


def design_90():
    draw_rotating_curves(N=2000, 
                         T1=0.5, 
                         T2=50, 
                         K1=1, 
                         K2=2, 
                         H1=1, 
                         H2=2, 
                         R1=480/7, 
                         R2=480/4,
                         S_func=lambda i, N: 1,
                         NP=480)    


def design_91():
    draw_rotating_curves(N=4000, 
                         T1=1, 
                         T2=800, 
                         K1=1, 
                         K2=2, 
                         H1=3, 
                         H2=5, 
                         R1=480*5/12, 
                         R2=480/24,
                         S_func=lambda i, N: 1,
                         NP=480)    


def design_92():
    draw_rotating_curves(N=4000, 
                         T1=1, 
                         T2=100, 
                         K1=1, 
                         K2=2, 
                         H1=1, 
                         H2=1, 
                         R1=480/6, 
                         R2=480/4,
                         S_func=lambda i, N: math.cos(3*math.pi*i/N)*0.5+0.5,
                         Y_func=lambda NP, C1, C2, R1, R2, S1, S2: 1.6*(NP/2 + R1*S1 + R2*(S1*C2 + C1*S2)),
                         NP=480)


def design_93():
    draw_rotating_curves(N=3000, 
                         T1=1, 
                         T2=100, 
                         K1=1, 
                         K2=2, 
                         H1=1, 
                         H2=2, 
                         R1=480/3,
                         R2=480/8,
                         S_func=lambda i, N: math.cos(8*math.pi*i/N)*0.4+0.6,
                         Y_func=lambda NP, C1, C2, R1, R2, S1, S2: 1.3*(NP/2 + R1*S1 + R2*(S1*C2 + C1*S2)),
                         NP=480)    


def design_94():
    draw_rotating_curves(N=5000, 
                         T1=1, 
                         T2=200, 
                         K1=1, 
                         K2=2, 
                         H1=1, 
                         H2=2, 
                         R1=480*3/8, 
                         R2=480/12,
                         S_func=lambda i, N: math.cos(18*math.pi*i/N)*0.4+0.6,
                         Y_func=lambda NP, C1, C2, R1, R2, S1, S2: 1.5*(NP/2 + R1*S1 + R2*(S1*C2 + C1*S2)),
                         NP=480)    


def design_95():
    draw_rotating_curves(N=4000, 
                         T1=1, 
                         T2=100, 
                         K1=1, 
                         K2=2, 
                         H1=1, 
                         H2=1, 
                         R1=480/6, 
                         R2=480/4,
                         S_func=lambda i, N: math.cos(4*math.pi*i/N)*0.4+0.6,
                         NP=480)    


def design_96():
    draw_rotating_curves(N=4000, 
                         T1=1, 
                         T2=100, 
                         K1=1, 
                         K2=2, 
                         H1=1, 
                         H2=1, 
                         R1=480/6, 
                         R2=480/4,
                         S_func=lambda i, N: math.cos(6*math.pi*i/N)*0.4+0.6,
                         Y_func=lambda NP, C1, C2, R1, R2, S1, S2: 1.7*(NP/2 + R1*S1 + R2*(S1*C2 + C1*S2)),
                         NP=480)
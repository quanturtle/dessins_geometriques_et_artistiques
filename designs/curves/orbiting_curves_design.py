import math
from shapes import draw_orbiting_curves

#TODO
def design_78():
    draw_orbiting_curves(N=2000,
                         T1=2,
                         T2=100,
                         K1=1,
                         K2=1,
                         R1=480*0.25,
                         NP=480)
    

def design_79():
    draw_orbiting_curves(N=4000,
                         T1=1,
                         T2=200,
                         K1=1,
                         K2=1,
                         R1=480*0.2,
                         R2_func=lambda N, i, NP: NP * 0.3 * (0.4*math.cos(2*i*math.pi/N*5)+0.6),
                         NP=480)
    
    
def design_80():
    draw_orbiting_curves(N=6000,
                         T1=1,
                         T2=300,
                         K1=1,
                         K2=2,
                         R1=480*0.3,
                         R2_func=lambda N, i, NP: NP*0.2*(0.5+0.5*math.cos(2*i*math.pi/10)),
                         X_func=lambda NP, A1, A2, R1, R2, K1, K2: int(NP*0.5 + R1*math.sin(K2*A1) + R2*math.sin(A2)),
                         Y_func=lambda NP, A1, A2, R1, R2, K1, K2: int(1.5*(NP*0.5 + R1*math.cos(K1*A1) + R2*math.cos(A2))),
                         NP=480)
    
    
def design_81():
    draw_orbiting_curves(N=2000,
                         T1=2,
                         T2=100,
                         K1=1,
                         K2=1,
                         R1=480*0.25,
                         NP=480)
    
    
def design_82():
    draw_orbiting_curves(N=2000,
                         T1=2,
                         T2=100,
                         K1=1,
                         K2=1,
                         R1=480*0.25,
                         NP=480)
    
    
def design_83():
    draw_orbiting_curves(N=2000,
                         T1=2,
                         T2=100,
                         K1=1,
                         K2=1,
                         R1=480*0.25,
                         NP=480)
    
    
def design_84():
    draw_orbiting_curves(N=2000,
                         T1=2,
                         T2=100,
                         K1=1,
                         K2=1,
                         R1=480*0.25,
                         NP=480)
    
    
def design_85():
    draw_orbiting_curves(N=2000,
                         T1=2,
                         T2=100,
                         K1=1,
                         K2=1,
                         R1=480*0.25,
                         NP=480)
    
    
def design_86():
    draw_orbiting_curves(N=2000,
                         T1=2,
                         T2=100,
                         K1=1,
                         K2=1,
                         R1=480*0.25,
                         NP=480)
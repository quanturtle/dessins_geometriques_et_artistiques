import math
from shapes import draw_spiraling_curves
    

def design_97():
    draw_spiraling_curves()
    
    
def design_98():
    draw_spiraling_curves(N=3000, 
                          T=60, 
                          R=0.1, 
                          L=0.1,
                          Y_func=lambda NP, YY: int(1.3*NP/2*(1+YY)),
                          NP=480)
    
    
def design_99():
    draw_spiraling_curves(N=2000, 
                          T=40, 
                          R=0.8, 
                          L=0.1,
                          Y_func=lambda NP, YY: int(1.7*NP/2*(1+YY)),
                          NP=480)    
    
def design_100():
    draw_spiraling_curves(N=9000, 
                          T=50, 
                          R=0.7, 
                          L=0.05,
                          AN_func=lambda i, N: 8 * math.pi * i / N,
                          Y_func=lambda NP, YY: int(1.4*NP/2*(1+YY)),
                          NP=480)
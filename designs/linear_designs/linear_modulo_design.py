import math
from shapes import draw_linear_modulo


def design_105():
    draw_linear_modulo()
    

def design_106():
    draw_linear_modulo(N=500, M=500, K1=11/7, K2=7/3, H=3)
    

def design_107():
    draw_linear_modulo(N=400, M=400, K1=4, K2=2, H=2)
    
    
def design_108():
    draw_linear_modulo(N=300, M=300, K1=5, K2=3, H=2)

    
def design_109():
    def compute_Y_109(NP: int, K2: float, i: int , N: int) -> int:
        return int(NP * 0.5 * (1 + math.cos(K2 * i * math.pi / N)))
    
    def I1_func_109(i: int, H: int, N: int) -> float:
        return 8 * i % N
    
    draw_linear_modulo(N=400, M=200, K1=2, K2=2, H=9, 
                       compute_Y=compute_Y_109,
                       I1_func=I1_func_109)
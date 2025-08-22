import math
from shapes import draw_linear_sticks


def design_110():
    draw_linear_sticks()


def design_111():
    def compute_R1_111(i: int, NP: int) -> float:
        return NP / 4

    def compute_R2_111(i: int, NP: int) -> float:
        return NP * 5 / 24

    draw_linear_sticks(
        N=600,
        M=1,
        K=5,
        compute_R1=compute_R1_111,
        compute_R2=compute_R2_111,
    )

    
def design_112():
    def compute_R1_112(i: int, NP: int) -> float:
        return NP / 3 * 0.7**(i - 1)
    
    def compute_R2_112(i: int, NP: int) -> float:
        return NP / 8 * 0.9**(i - 1)
    
    def compute_YD_112(NP, R1, R2, AN, K):
        return 1.2 * (NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN))
    
    def compute_YA_112(NP, R1, R2, AN, K):
        return 1.2 * (NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN + math.pi))

    draw_linear_sticks(N=100, M=6, K=6, 
					   compute_R1=compute_R1_112,
					   compute_R2=compute_R2_112,
					   compute_YD=compute_YD_112,
					   compute_YA=compute_YA_112)


def design_113():
    def compute_R1_113(i: int, NP: int) -> float:
        return NP / 3 * 0.6**(i - 1)
    
    def compute_R2_113(i: int, NP: int) -> float:
        return NP / 8 * 0.6**(i - 1)

    draw_linear_sticks(N=300, M=4, K=3, 
					   compute_R1=compute_R1_113,
					   compute_R2=compute_R2_113)


def design_114():
    def compute_R1_114(i: int, NP: int) -> float:
        return (NP / 3) * (0.8 ** (i - 1))
    
    def compute_R2_114(i: int, NP: int) -> float:
        return (NP / 12) * (0.8 ** (i - 1))
    
    def compute_YD_114(NP, R1, R2, AN, K):
        return 1.3 * (NP/2 + R1*math.sin(AN) + R2*math.sin(K*AN))
    
    def compute_YA_114(NP, R1, R2, AN, K):
        return 1.3 * compute_YD_114(NP, R1, R2, AN, K)

    draw_linear_sticks(N=300, M=7, K=7, 
					   compute_R1=compute_R1_114,
					   compute_R2=compute_R2_114,
					   compute_YD=compute_YD_114,
					   compute_YA=compute_YA_114)

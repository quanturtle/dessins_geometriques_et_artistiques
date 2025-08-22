import math
from shapes import draw_dragon


def design_50():
    draw_dragon(N=6)
    

def design_51():
    draw_dragon(N=10)
    

def design_52():
    draw_dragon(N=14)
    

def design_53():
    def A_initializer_53(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 3):
            A[i] = 1
        
        return A

    draw_dragon(N=10,
                A_initializer=A_initializer_53,
                initial_values=[480*0.25, 0, -math.pi/2, 480/math.sqrt(2)**10*0.9])
    

def design_54():
    def A_initializer_54(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 3):
            A[i] = 1
        
        return A
    
    draw_dragon(N=14,
                A_initializer=A_initializer_54,
                initial_values=[480*0.25, 0, -math.pi, 480/math.sqrt(2)**14*0.9])
    

def design_55():
    def A_initializer_55(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 4):
            A[i] = 1
        
        return A
    
    draw_dragon(N=10,
                A_initializer=A_initializer_55,
                initial_values=[480*0.62, 0, 0, 480/math.sqrt(2)**10*0.9])
    

def design_56():
    def A_initializer_56(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 4):
            A[i] = 1
        
        return A
    
    draw_dragon(N=14,
                A_initializer=A_initializer_56,
                initial_values=[480*0.62, 0, -math.pi/2, 480/math.sqrt(2)**14*0.9])
    

def design_57():
    def A_initializer_57(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 4):
            A[i] = 1
            A[i + 1] = 1
        
        return A
    
    draw_dragon(N=10,
                A_initializer=A_initializer_57,
                initial_values=[480*0.7, 480/2, math.pi/2, 480/math.sqrt(2)**10*0.8])
    

def design_58():
    def A_initializer_58(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 4):
            A[i] = 1
            A[i + 1] = 1
        
        return A
    
    draw_dragon(N=14,
                A_initializer=A_initializer_58,
                initial_values=[480*0.7, 480/2, math.pi/2, 480/math.sqrt(2)**14*0.8])
    

def design_59():
    def A_initializer_59(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 5):
            A[i] = 1
        
        return A
    
    draw_dragon(N=10,
                A_initializer=A_initializer_59,
                initial_values=[480*0.4, 480/2, math.pi, 480/math.sqrt(2)**10*0.9])
    

def design_60():
    def A_initializer_60(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 5):
            A[i] = 1
        
        return A
    
    draw_dragon(N=14,
                A_initializer=A_initializer_60,
                initial_values=[480*0.4, 480/2, 0, 480/math.sqrt(2)**14*0.9])
    

def design_61():
    def A_initializer_61(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 5):
            A[i] = 1
            
        for i in range(1, N, 5):
            A[i + 1] = 1
        
        return A
    
    draw_dragon(N=10,
                A_initializer=A_initializer_61,
                initial_values=[480*0.55, 480/2, 0, 480/math.sqrt(2)**10*0.96])


def design_62():
    def A_initializer_62(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 5):
            A[i] = 1
            
        for i in range(1, N, 5):
            A[i + 1] = 1
        
        return A
    
    draw_dragon(N=14,
                A_initializer=A_initializer_62,
                initial_values=[480*0.55, 480/2, 3*math.pi/2, 480/math.sqrt(2)**14*0.96])
    
    
def design_63():
    def A_initializer_63(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 5):
            A[i] = 1
            
        for i in range(1, N - 1, 5):
            A[i + 2] = 1
            
        return A
    
    draw_dragon(N=10,
                A_initializer=A_initializer_63,
                initial_values=[480*0.15, 480/2, 0, 480/math.sqrt(2)**10*0.9])
    
    
def design_64():
    def A_initializer_64(N: int):
        A = [0] * (N + 1)
        
        for i in range(0, N + 1, 5):
            A[i] = 1
            
        for i in range(1, N - 1, 5):
            A[i + 2] = 1
            
        return A
    
    draw_dragon(N=14,
                A_initializer=A_initializer_64,
                initial_values=[480*0.15, 480/2, 0, 480/math.sqrt(2)**14*0.9])
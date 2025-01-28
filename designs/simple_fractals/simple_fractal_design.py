import math
from shapes import draw_simple_fractal


def design_115():
    draw_simple_fractal(M=3,
                        N=4,
                        K=1)
    

def design_116():
    draw_simple_fractal(M=3, 
                        N=4, 
                        K=2)
    

def design_117():
    draw_simple_fractal(M=3,
                        N=4,
                        K=3)
    

def design_118():
    draw_simple_fractal(M=3,
                        N=4,
                        K=4)
    

def design_119():
    draw_simple_fractal(M=3,
                        N=4,
                        K=5)
    

def design_120():
    draw_simple_fractal(M=3,
                        N=4,
                        K=2,
                        X=[480, 0, 480*0.5, 480])
    

def design_121():
    draw_simple_fractal(M=3,
                        N=4,
                        K=3,
                        X=[480, 0, 480*0.5, 480])
    

def design_122():
    draw_simple_fractal(M=3,
                        N=4,
                        K=4,
                        X=[480, 0, 480*0.5, 480])
    

def design_123():
    draw_simple_fractal(M=3,
                        N=4,
                        K=5,
                        X=[480, 0, 480*0.5, 480])
    

def design_124():
    draw_simple_fractal(M=1,
                        N=3,
                        K=1,
                        X=[480*0.5, 480*0.5],
                        Y=[480, 0],
                        L=[math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
                        A=[math.pi/4, math.atan(-2), math.pi/4])


def design_125():
    draw_simple_fractal(M=1,
                        N=3,
                        K=2,
                        X=[480*0.5, 480*0.5],
                        Y=[480, 0],
                        L=[math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
                        A=[math.pi/4, math.atan(-2), math.pi/4])

    

def design_126():
    draw_simple_fractal(M=1,
                        N=3,
                        K=3,
                        X=[480*0.5, 480*0.5],
                        Y=[480, 0],
                        L=[math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
                        A=[math.pi/4, math.atan(-2), math.pi/4])

    

def design_127():
    draw_simple_fractal(M=1,
                        N=3,
                        K=4,
                        X=[480*0.5, 480*0.5],
                        Y=[480, 0],
                        L=[math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
                        A=[math.pi/4, math.atan(-2), math.pi/4])

    

def design_128():
    draw_simple_fractal(M=1,
                        N=3,
                        K=5,
                        X=[480*0.5, 480*0.5],
                        Y=[480, 0],
                        L=[math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
                        A=[math.pi/4, math.atan(-2), math.pi/4])

    

def design_129():
    draw_simple_fractal(M=1,
                        N=3,
                        K=6,
                        X=[480*0.5, 480*0.5],
                        Y=[480, 0],
                        L=[math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
                        A=[math.pi/4, math.atan(-2), math.pi/4])

    

def design_130():
    draw_simple_fractal(M=1,
                        N=3,
                        K=7,
                        X=[480*0.5, 480*0.5],
                        Y=[480, 0],
                        L=[math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
                        A=[math.pi/4, math.atan(-2), math.pi/4])

    

def design_131():
    draw_simple_fractal(M=1,
                        N=3,
                        K=8,
                        X=[480*0.5, 480*0.5],
                        Y=[480, 0],
                        L=[math.sqrt(2)/3, math.sqrt(5)/3, math.sqrt(2)/3],
                        A=[math.pi/4, math.atan(-2), math.pi/4])
    

def design_132():
    draw_simple_fractal(M=4,
                        N=4,
                        K=5,
                        X=[0, 480, 480, 0, 0],
                        Y=[0, 0, 480, 480, 0],
                        L=[1/(2+ 2 * math.cos(0.45 * math.pi))]*4,
                        A=[0, 0.45*math.pi, -0.45*math.pi, 0])
    

def design_133():
    draw_simple_fractal(M=4,
                        N=4,
                        K=6,
                        X=[0, 480, 480, 0, 0],
                        Y=[0, 0, 480, 480, 0],
                        L=[1/(2+ 2 * math.cos(.48*math.pi))]*4,
                        A=[0, 0.48*math.pi, -0.48*math.pi, 0])


def design_134():
    draw_simple_fractal(M=1,
                        N=4,
                        K=6,
                        X=[0, 0],
                        Y=[480, -480],
                        L=[1/3, 1/3, math.sqrt(10)/9, 5/9],
                        A=[0, math.pi/2, -math.atan(3), 0])


def design_135():
    draw_simple_fractal(M=2,
                        N=2,
                        K=12,
                        X=[480/2, 480/2, 480/2],
                        Y=[480*.25, 480*.75, 480*.25],
                        L=[1/math.sqrt(2), 1/math.sqrt(2)],
                        A=[math.pi/4, -math.pi/4])
import math
from typing import Tuple
from shapes import draw_simple_fractal_deformed


def design_152():
    draw_simple_fractal_deformed()


def design_153():
    def deformation_subroutine_153(X0: int, Y0: int, NP: int = 480) -> Tuple[int, int]:
        XH = X0/NP*2 - 1
        YH = Y0/NP*2 - 1
        DH = math.sqrt(XH*XH + YH*YH)
        
        if XH != 0:
            AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)
        else:
            AH = math.pi/2*math.copysign(1, YH)
            
        AH = AH + math.pi * DH
        DH = pow(DH, 4)
        
        X1 = int((DH*math.cos(AH) + 1)*NP/2)
        Y1 = int((DH*math.sin(AH) + 1)*NP/2)

        return X1, Y1

    draw_simple_fractal_deformed(M=3,
                                 N=4,
                                 K=5,
                                 deformation_func=deformation_subroutine_153)


def design_154():
    def deformation_subroutine_154(X0: int, Y0: int, NP: int = 480) -> Tuple[int, int]:
        XH = X0/NP*2 - 1
        YH = Y0/NP*2 - 1
        DH = math.sqrt(XH*XH + YH*YH)
        
        if XH != 0:
            AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)
        else:
            AH = math.pi/2*math.copysign(1, YH)
            
        DH = pow(DH, 5)
        AH = AH + math.pi/4 * math.sin(2*math.pi*DH)
        
        X1 = int((DH*math.cos(AH) + 1)*NP/2)
        Y1 = int((DH*math.sin(AH) + 1)*NP/2)

        return X1, Y1
    
    draw_simple_fractal_deformed(M=3,
                                 N=4,
                                 K=4,
                                 deformation_func=deformation_subroutine_154)


def design_155():
    def deformation_subroutine_155(X0: int, Y0: int, NP: int = 480) -> Tuple[int, int]:
        XH = X0/NP*2 - 1
        YH = Y0/NP*2 - 1
        DH = math.sqrt(XH*XH + YH*YH)
        
        if XH != 0:
            AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)
        
        else:
            AH = math.pi/2*math.copysign(1, YH)
            
        DH = pow(DH, 6)
        AH = pow(AH, 3)/(math.pi*math.pi)
        
        X1 = int((DH*math.cos(AH) + 1)*NP/2)
        Y1 = int((DH*math.sin(AH) + 1)*NP/2)
        
        return X1, Y1
    
    draw_simple_fractal_deformed(M=3,
                                 N=4,
                                 K=5,
                                 deformation_func=deformation_subroutine_155)


def design_156():
    def deformation_subroutine_156(X0: int, Y0: int, NP: int = 480) -> Tuple[int, int]:
        XH = X0/NP*2 - 1
        YH = Y0/NP*2 - 1
        DH = math.sqrt(XH*XH + YH*YH)

        if XH != 0:
            AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

        else:
            AH = math.pi/2*math.copysign(1, YH)
            
        DH = pow(DH, 6)
        AH = 4*AH*AH*AH/(math.pi*math.pi)

        X1 = int((DH*math.cos(AH) + 1)*NP/2)
        Y1 = int((DH*math.sin(AH) + 1)*NP/2)

        return X1, Y1
    
    draw_simple_fractal_deformed(M=3,
                                 N=4,
                                 K=5,
                                 deformation_func=deformation_subroutine_156)


def design_157():
    def deformation_subroutine_157(X0: int, Y0: int, NP: int = 480) -> Tuple[int, int]:
        XH = X0/NP*2 - 1
        YH = Y0/NP*2 - 1
        DH = math.sqrt(XH*XH + YH*YH)

        if XH != 0:
            AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)

        else:
            AH = math.pi/2*math.copysign(1, YH)
            
        DH = pow(DH, 5)
        AH = 10*AH

        X1 = int((DH*math.cos(AH) + 1)*NP/2)
        Y1 = int((DH*math.sin(AH) + 1)*NP/2)

        return X1, Y1
    
    draw_simple_fractal_deformed(M=3,
                                 N=4,
                                 K=5,
                                 deformation_func=deformation_subroutine_157)


def design_158():
    def deformation_subroutine_158(X0: int, Y0: int, NP: int = 480) -> Tuple[int, int]:
        XH = X0/NP*2 - 1
        YH = Y0/NP*2 - 1
        DH = math.sqrt(XH*XH + YH*YH)
        
        if XH != 0:
            AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)
        
        else:
            AH = math.pi/2*math.copysign(1, YH)
            
        DH = pow(DH, 5)
        AH = AH + math.pi/18*math.sin(6*math.pi*DH)
        
        X1 = int((DH*math.cos(AH) + 1)*NP/2)
        Y1 = int((DH*math.sin(AH) + 1)*NP/2)
        
        return X1, Y1
    
    draw_simple_fractal_deformed(M=3,
                                 N=4,
                                 K=5,
                                 deformation_func=deformation_subroutine_158)


def design_159():
    def deformation_subroutine_159(X0: int, Y0: int, NP: int = 480) -> Tuple[int, int]:
        XH = X0/NP*2 - 1
        YH = Y0/NP*2 - 1
        DH = math.sqrt(XH*XH + YH*YH)
        
        if XH != 0:
            AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)
        
        else:
            AH = math.pi/2*math.copysign(1, YH)
            
        DH = pow(DH, 5)
        AH = 20*AH
        
        X1 = int((DH*math.cos(AH) + 1)*NP/2)
        Y1 = int((DH*math.sin(AH) + 1)*NP/2)
        
        return X1, Y1

    draw_simple_fractal_deformed(M=3,
                                 N=4,
                                 K=5,
                                 deformation_func=deformation_subroutine_159)


def design_160():
    draw_simple_fractal_deformed(M=4,
                                 N=4,
                                 K=4)


def design_161():
    draw_simple_fractal_deformed(M=4,
                                 N=4,
                                 K=4)


def design_162():
    draw_simple_fractal_deformed(M=4,
                                 N=4,
                                 K=4)


def design_163():
    draw_simple_fractal_deformed(M=4,
                                 N=4,
                                 K=4)
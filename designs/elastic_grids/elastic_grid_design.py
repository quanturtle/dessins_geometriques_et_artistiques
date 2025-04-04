from typing import Tuple
import math
from shapes import draw_elastic_grid


def design_164():
	draw_elastic_grid()


def design_165():
	def deformation_subroutine_165(DI: float, AN: float) -> Tuple[float, float]:
		if DI < 1:
			DI = DI ** 3
			
		return DI, AN

	draw_elastic_grid(deformation_subroutine=deformation_subroutine_165)


def design_166():
	def deformation_subroutine_166(DI: float, AN: float) -> Tuple[float, float]:
		if DI < 1:
			AN = AN + math.pi/2*(1 - DI)
		
		return DI, AN
	
	draw_elastic_grid(deformation_subroutine=deformation_subroutine_166)


def design_167():
    def deformation_subroutine_167(DI: float, AN: float) -> Tuple[float, float]:
        if DI < 1:
            AN += 3.5 * (1 - DI)
            DI = DI ** 0.3
        
        return DI, AN
    
    draw_elastic_grid(deformation_subroutine=deformation_subroutine_167)


def design_168():
    def deformation_subroutine_168(DI: float, AN: float) -> Tuple[float, float]:
        if DI < 1:
            AN += 2 * math.pi * (1 - DI)
        
        return DI, AN
    
    draw_elastic_grid(deformation_subroutine=deformation_subroutine_168)


def design_169():
    def deformation_subroutine_169(DI: float, AN: float) -> Tuple[float, float]:
        if DI < 1:
            AN += math.pi * (1 - DI)
            DI = DI ** 3
        
        return DI, AN
            
    draw_elastic_grid(deformation_subroutine=deformation_subroutine_169)


def design_170():
    def deformation_subroutine_170(DI: float, AN: float) -> Tuple[float, float]:
        if DI < 1:
            AN += (math.pi/2) * math.sin(math.pi*(1-DI))
            DI = DI ** 0.2
            
        return DI, AN
    
    draw_elastic_grid(deformation_subroutine=deformation_subroutine_170)


def design_171():
    def deformation_subroutine_171(DI: float, AN: float) -> Tuple[float, float]:
        if DI < 1:
            AN += (math.pi/4) * math.sin(2 * math.pi * (1-DI))
            
        return DI, AN
    
    draw_elastic_grid(deformation_subroutine=deformation_subroutine_171)


def design_172():
    def deformation_subroutine_172(DI: float, AN: float) -> Tuple[float, float]:
        if DI < 1:
            AN += (math.pi/2) * math.sin(math.pi * (1-DI))
            DI = DI ** 2
            
        return DI, AN
    
    draw_elastic_grid(deformation_subroutine=deformation_subroutine_172)


def design_173():
    def deformation_subroutine_173(DI: float, AN: float) -> Tuple[float, float]:
        if DI < 1:
            AN += (math.pi/2) * math.sin(math.pi * (1-DI))
            
        return DI, AN
    
    draw_elastic_grid(deformation_subroutine=deformation_subroutine_173)


def design_174():
    def xy_transform_174(I: float, J: float) -> Tuple[float, float]:
        return I / 20 - 1, J / 20 - 1
    
    def deformation_subroutine_174(DI: float, AN: float) -> Tuple[float, float]:
        if DI < 1:
            AN += math.pi * (1-DI)
            DI = DI ** .3
            
        return DI, AN
    
    draw_elastic_grid(xy_transform=xy_transform_174, 
                      deformation_subroutine=deformation_subroutine_174,
                      L_range=1,
                      I_range=41,
                      J_range=41,)


def design_175():
    def xy_transform_175(I: float, J: float) -> Tuple[float, float]:
        return I / 10 - 1, J / 20 - 1
    
    def deformation_subroutine_175(DI: float, AN: float) -> Tuple[float, float]:
        if DI < 1:
            AN += math.pi * 2 * (1-DI)
            
        return DI, AN
    
    draw_elastic_grid(xy_transform=xy_transform_175, 
                      deformation_subroutine=deformation_subroutine_175,
                      L_range=1,
                      I_range=21,
                      J_range=41,)


def design_176():
    def xy_transform_176(I: float, J: float) -> Tuple[float, float]:
        return I / 20 - 1, J / 20 - 1
    
    def deformation_subroutine_176(DI: float, AN: float) -> Tuple[float, float]:
        if DI < 1:
            AN += math.pi * 2* (1-DI)
            
        return DI, AN
    
    draw_elastic_grid(xy_transform=xy_transform_176, 
                      deformation_subroutine=deformation_subroutine_176,
                      L_range=1,
                      I_range=21,
                      J_range=41,)
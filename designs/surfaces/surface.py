import math
from shapes import draw_surface


def design_177():
	draw_surface()
	

def design_178():
	draw_surface(N=60,
			  	 PA=480/160,
				 E1=1,
				 E2=0)
	

def design_179():
	draw_surface(N=60,
			  	 PA=480/160,
				 E1=1,
				 E2=1)
	

def design_180():
	draw_surface(N=60,
			  	 PA=480/160,
				 E1=2,
				 E2=0)
	

def design_181():
	draw_surface(N=60,
			  	 PA=480/160,
				 E1=2,
				 E2=1)
	

def design_182():
	def compute_z_182(x, y, NP: int) -> float:
		return NP / 5 * math.sin(3 * math.pi * y) * math.sin(4 * math.pi * x)
	
	draw_surface(N=60,
			  	 PA=480/240,
				 E1=1,
				 E2=0,
				 XA=0,
				 YA=0,
				 XB=3/4*480,
				 YB=0,
				 XC=480,
				 YC=5/4*480,
				 XD=480/4,
				 YD=5/4*480,
				 compute_z=compute_z_182)
	

def design_183():
	def compute_z_183(x, y, NP: int) -> float:
		return NP / 4 * math.sin(2 * math.pi * y) * math.sin(3 * math.pi * x)
	
	draw_surface(N=60,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480/2,
				 YA=0,
				 XB=480,
				 YB=5/12*480,
				 XC=480/2,
				 YC=5/6*480,
				 XD=0,
				 YD=5/12*480,
				 compute_z=compute_z_183)
	

def design_184():
	def compute_z_184(x, y, NP: int) -> float:
		DI = 7 * math.sqrt((x - 0.5) * (x - 0.5) + (y - 0.5) * (y - 0.5))
		return math.cos(DI) * NP / 5
	
	draw_surface(N=30,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480/2,
				 YA=0,
				 XB=480,
				 YB=5/12*480,
				 XC=480/2,
				 YC=5/6*480,
				 XD=0,
				 YD=5/12*480,
				 compute_z=compute_z_184)
	

def design_185():	
	def compute_z_185(x, y, NP: int) -> float:
		X7 = 2 * x - 1
		Y7 = 2 * y - 1
		
		if X7*Y7 != 0:
			z = 3 * NP/4 * X7 * Y7 * (X7 * Y7 - Y7 * Y7)
		else:
			z = 0
		
		return z
	
	draw_surface(N=40,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480/2,
				 YA=0,
				 XB=480,
				 YB=480/2,
				 XC=480/2,
				 YC=480,
				 XD=0,
				 YD=480/2,
				 compute_z=compute_z_185)
	

def design_186():	
	def compute_z_186(x, y, NP: int) -> float:
		X7 = (3 * x - int(3 * x)) * 2 - 1
		Y7 = (2 * y - int(2 * y)) * 2 - 1
		DI = X7 * X7 + Y7 * Y7
		
		return NP / 4 * (1 - DI**0.2)
	
	draw_surface(N=30,
			  	 PA=480/160,
				 E1=2,
				 E2=0,
				 XA=480/2,
				 YA=0,
				 XB=480,
				 YB=480/3,
				 XC=480/2,
				 YC=2/3*480,
				 XD=0,
				 YD=480/3,
				 compute_z=compute_z_186)
	

def design_187():
	def compute_z_187(x, y, NP: int) -> float:
		X7 = (5 * x - int(5 * x)) * 2 - 1
		Y7 = (5 * y - int(5 * y)) * 2 - 1
		DI = X7 * X7 + Y7 * Y7
		
		return NP / 4 * (1 - DI) * (0.6 - abs(y - 0.5))
	
	draw_surface(N=50,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480/2,
				 YA=0,
				 XB=480,
				 YB=480/3,
				 XC=480/2,
				 YC=2/3*480,
				 XD=0,
				 YD=480/3,
				 compute_z=compute_z_187)
	

def design_188():	
	def compute_z_188(x, y, NP: int) -> float:
		X7 = 2 * x - 1
		Y7 = 2 * y - 1
		if X7*Y7 != 0:
			z = 3 * NP/4 * X7 * Y7 * (X7 * X7 - Y7 * Y7) / (X7 * X7 + Y7 * Y7)
		else:
			z = 0
		
		return z
	
	draw_surface(N=40,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480/2,
				 YA=0,
				 XB=480,
				 YB=480/2,
				 XC=480/2,
				 YC=480,
				 XD=0,
				 YD=480/2,
				 compute_z=compute_z_188)
	

def design_189():	
	def compute_z_189(x, y, NP: int) -> float:
		X7 = 3 * y - 1.5
		Y7 = 2 * x - 1.5
		if X7*Y7 != 0:
			z = NP/4 * Y7 * X7**2 / (Y7**2 + X7**4)
		else:
			z = 0
		
		return z
	
	draw_surface(N=80,
              	 PA=480/480,
				 E1=1,
				 E2=0,
				 XA=480/2, 
     			 YA=0,
				 XB=480, 
     			 YB=480/3,
				 XC=480/2, 
     			 YC=2*480/3,
				 XD=0, 
     			 YD=480/3,
				 compute_z=compute_z_189,
				 translate_y=-60)
	

def design_190():
	def compute_z_190(x, y, NP: int) -> float:
		DI = 16 * ((x - 0.5) * (x - 0.5) + (y - 0.5) * (y - 0.5))
		return NP * 5 / 12 * math.cos(4 * DI) * math.exp(-DI)
	
	draw_surface(N=80,
			  	 PA=480/240,
				 E1=1,
				 E2=0,
				 XA=480/2,
				 YA=0,
				 XB=480,
				 YB=480/3,
				 XC=480/2,
				 YC=2*480/3,
				 XD=0,
				 YD=480/3,
				 compute_z=compute_z_190)
	

def design_191():	
	draw_surface()
	

def design_192():
	draw_surface()
	

def design_193():
	draw_surface()
	

def design_194():
	draw_surface()
	

def design_195():
	draw_surface()
	

def design_196():
	draw_surface()
	

def design_197():
	draw_surface()
	

def design_198():
	draw_surface()
	

def design_199():
	draw_surface()
	

def design_200():
	draw_surface()
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
	draw_surface()
	

def design_185():	
	draw_surface()
	

def design_186():	
	draw_surface()
	

def design_187():
	draw_surface()
	

def design_188():	
	draw_surface()
	

def design_189():	
	draw_surface()
	

def design_190():
	draw_surface()
	

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
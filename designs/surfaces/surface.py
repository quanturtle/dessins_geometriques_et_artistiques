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
		DI = X7**2 + Y7**2
		
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
		DI = X7**2 + Y7**2
		
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
	def compute_z_191(x, y, NP: int) -> float:
		X7 = 2 * abs(x - 0.5)
		Y7 = 2 * abs(y - 0.5)
		M7 = max(X7, Y7)
		M8 = int(5 * M7)
		M9 = 5 * M7 - M8
		Z = 0
		
		if M9 > 0.8:
			Z = (M9 - 0.8) * 5
		
		return -NP * 5/48 * (Z + M8)
	
	draw_surface(N=40,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480/2,
				 YA=0,
				 XB=480,
				 YB=480/3,
				 XC=480/2,
				 YC=2*480/3,
				 XD=0,
				 YD=480/3,
				 compute_z=compute_z_191)
	

def design_192():
	def compute_z_192(x, y, NP: int) -> float:
		X7 = 2 * abs(x - 0.5)
		Y7 = 2 * abs(y - 0.5)
		M7 = X7 + Y7
		M8 = int(4 * M7)
		M9 = 4 * M7 - M8
		Z = 0
		
		if M9 > 0.8:
			Z = (M9 - 0.8) * 5
		
		return -NP * 5/48 * (Z + M8)
	
	draw_surface(N=40,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480/3,
				 YA=0,
				 XB=480,
				 YB=480/4,
				 XC=2*480/3,
				 YC=3*480/4,
				 XD=0,
				 YD=480/2,
				 compute_z=compute_z_192)
	

def design_193():
	def compute_z_193(x, y, NP: int) -> float:
		AA = 1.5 - 6 * abs(x - 0.5)
		BB = 1.5 - 6 * abs(y - 0.5)
		if BB < AA:
			AA = BB
		
		CC = 0.5 - 2 * abs(x - 0.5)
		DD = 0.25 - 2 * abs(y - 0.5)
		
		if CC > AA:
			AA = CC
		
		if DD > AA:
			AA = DD
		
		return NP * 5/8 * AA
	
	draw_surface(N=40,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480*5/12,
				 YA=0,
				 XB=480,
				 YB=480*5/12,
				 XC=480*7/12,
				 YC=480*5/6,
				 XD=0,
				 YD=480*5/12,
				 compute_z=compute_z_193)
	

def design_194():
	def compute_z_194(x, y, NP: int) -> float:
		X7 = 2 * x - int(2 * x)
		Y7 = 3 * y - int(3 * y)
		AA = 1.5 - 6 * abs(X7 - 0.5)
		BB = 1.5 - 6 * abs(Y7 - 0.5)
		
		if BB < AA:
			AA = BB
		
		CC = 0.5 - 2 * abs(X7 - 0.5)
		DD = 0.25 - 2 * abs(Y7 - 0.5)
		
		if CC > AA:
			AA = CC
		
		if DD > AA:
			AA = DD
		
		return NP * 13/48 * AA
	
	draw_surface(N=60,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480*3/8,
				 YA=0,
				 XB=480,
				 YB=480*3/8,
				 XC=480*5/8,
				 YC=480*3/4,
				 XD=0,
				 YD=480*3/8,
				 compute_z=compute_z_194)
	

def design_195():
	def compute_z_195(x, y, NP: int) -> float:
		AA = 0.5 - abs(x - 0.5)
		BB = 0.5 - abs(y - 0.5)
		CC = 0.5 - abs(x + y - 1)
		DD = 0.5 - abs(x - y) / math.sqrt(2)
		
		if BB < AA:
			AA = BB
		
		if CC < AA:
			AA = CC
		
		if DD < AA:
			AA = DD
		
		return NP * 5/2 * AA
	
	draw_surface(N=40,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480*5/12,
				 YA=0,
				 XB=480,
				 YB=480/4,
				 XC=480*7/12,
				 YC=480/2,
				 XD=0,
				 YD=480/4,
				 compute_z=compute_z_195)
	

def design_196():
	def compute_z_196(x, y, NP: int) -> float:
		X7 = (7 * x - int(7 * x)) * 2 - 1
		Y7 = (7 * y - int(7 * y)) * 2 - 1
  
		DI = X7**2 + Y7**2
		return NP * (1/16 * (1 - DI) + 5/4 * (1 - abs(x - 0.5)) * (1 - abs(y - 0.5)))
	
	draw_surface(N=80,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480/4,
				 YA=0,
				 XB=480,
				 YB=0,
				 XC=480*3/4,
				 YC=480*3/4,
				 XD=0,
				 YD=480*3/4,
				 compute_z=compute_z_196)
	

def design_197():
	def compute_z_197(x, y, NP: int) -> float:
		XH = x + 0.4755 + y
		YH = y + 0.23771 - x
    
		X6 = 2 * abs(3 * XH - int(3 * XH) - 0.5)
		Y6 = 2 * abs(4 * YH - int(4 * YH) - 0.5)
		Z6 = X6 * Y6
    
		X7 = 2 * abs(5 * XH - int(5 * XH) - 0.5)
		Y7 = 2 * abs(5 * YH - int(5 * YH) - 0.5)
		Z7 = X7 * Y7
    
		X8 = 2 * abs(10 * XH - int(10 * XH) - 0.5)
		Y8 = 2 * abs(13 * YH - int(13 * YH) - 0.5)
		Z8 = X8 * Y8
    
		Z = (5 * Z6 + 3 * Z7 + 2 * Z8) * NP / 48
		Z = Z * (0.6 - abs(x - 0.5)) * (0.6 - abs(y - 0.5)) * 4
    
		return Z
	
	draw_surface(N=80,
			  	 PA=480/480,
				 E1=1,
				 E2=0,
				 XA=480/3,
				 YA=0,
				 XB=480,
				 YB=480/4,
				 XC=480*2/3,
				 YC=480*3/4,
				 XD=0,
				 YD=480/2,
				 compute_z=compute_z_197)	


def design_198():
	def compute_z_198(x, y, NP: int) -> float:
		X7 = x
		Y7 = y
		K7 = 0
		
		while True:
			K7 += 1
			if K7 > 4:
				return 0
			
			U7 = int(2 * X7)
			X7 = 2 * X7 - U7
			
			V7 = int(2 * Y7)
			Y7 = 2 * Y7 - V7
			
			if U7 == V7:
				break
		
		X9 = 2 * X7 - 1
		Y9 = 2 * Y7 - 1
		Z = (1 - abs(X9)) * (1 - abs(Y9))
		Z = NP * 5/24 * Z**3
		
		return Z
  	
	draw_surface(N=64,
			  	 PA=480/240,
				 E1=1,
				 E2=0,
				 XA=480/3,
				 YA=0,
				 XB=480,
				 YB=480*4/15,
				 XC=480*2/3,
				 YC=480*4/5,
				 XD=0,
				 YD=480*8/15,
				 compute_z=compute_z_198)
	

def design_199():
	def compute_z_199(x, y, NP: int) -> float:
		X7 = x
		Y7 = y
		K7 = 0
		
		while True:
			K7 += 1
			if K7 > 6:
				return 0
			
			U7 = int(2 * X7)
			X7 = 2 * X7 - U7
			
			V7 = int(2 * Y7)
			Y7 = 2 * Y7 - V7
			
			if U7 == V7:
				break
		
		X9 = 2 * X7 - 1
		Y9 = 2 * Y7 - 1
		
		Z = 1 - X9*X9 - Y9*Y9
		if Z > 0:
			Z = NP * 5/16 / (K7**2) * math.sqrt(Z)
		
		else:
			Z = 0
		
		return Z
	
	draw_surface(N=64,
			  	 PA=480/240,
				 E1=1,
				 E2=0,
				 XA=480/3,
				 YA=0,
				 XB=480,
				 YB=480*4/15,
				 XC=480*2/3,
				 YC=480*4/5,
				 XD=0,
				 YD=480*8/15,
				 compute_z=compute_z_199)
	

def design_200():
	def compute_z_200(x, y, NP: int) -> float:
		X7 = x
		Y7 = y
		K7 = 0
		U7 = 0
		V7 = 0
        
		while True:
			K7 = K7 + 1
			if K7 > 5:
				return 0
            
			U7 = int(2 * X7)
			X7 = 2 * X7 - U7
            
			V7 = int(2 * Y7)
			Y7 = 2 * Y7 - V7
            
			if U7 == 0 or V7 == 0:
				continue
			else:
				break
        
		Z1 = 0.5 - abs(X7 - 0.5)
		Z = 0.5 - abs(Y7 - 0.5)
        
		if Z1 < Z:
			Z = Z1
            
		Z = NP * 2.5 / (K7 ** 2) * Z
		return Z
	
	draw_surface(N=64,
			  	 PA=480/240,
				 E1=2,
				 E2=0,
				 XA=480*2/3,
				 YA=0,
				 XB=480,
				 YB=480*8/15,
				 XC=480/3,
				 YC=480*8/15,
				 XD=0,
				 YD=0,
				 compute_z=compute_z_200)
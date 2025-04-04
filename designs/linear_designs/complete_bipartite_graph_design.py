from shapes import draw_complete_bipartite_graph


def design_101():
    draw_complete_bipartite_graph()
    
    
def design_102():
    draw_complete_bipartite_graph(N=15,
                                  XA=480/2,
                                  YA=480/15,
                                  XB=480/2,
								  YB=1.2*480,
								  XC=0, 
          						  YC=0, 
                  				  XD=480, 
                        		  YD=0)
    

def design_103():
    draw_complete_bipartite_graph(N=19, 
                                  XA=0, 
                                  YA=0, 
                                  XB=480, 
                                  YB=1.4*480, 
                                  XC=0, 
                                  YC=1.4*480, 
                                  XD=480, 
                                  YD=0)
    

def design_104():
    draw_complete_bipartite_graph(N=16, 
                                  XA=0, 
                                  YA=0, 
                                  XB=480/2, 
                                  YB=480, 
                                  XC=480, 
                                  YC=0, 
                                  XD=480/2, 
                                  YD=480)
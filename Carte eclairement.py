# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:35:27 2025

@author: routin
"""

import numpy as np
from Surface_library import Surface_plane
from Source_library import Source

source1=Source(0, 0, 5, 10, 1, 0, 0, [0,0,-1])
source2=Source(2, 2, 5, 10, 1, 0, 0, [0,0,-1])
liste_sources=[source1,source2]

surface=Surface_plane(point_def=[0,0,0],v_normal=[0,0,1])
carte_coord_surface=surface.get_carte_coord(0.05)

a,b=np.shape(carte_coord_surface)


for i in liste_sources:
    copy_carte_coord=carte_coord_surface.copy()
    for i in range(a):
        for j in range(b):
            point_P=carte_coord_surface[i,j]
            point_S=[i.x,i.y,i.z]
            SP=point_P-point_S
            norme_SP=np.linalg.norm(SP)
            
            if norme_SP==0:
                raise Exception('la source est comprise dans le plan')
                
            SP_normé/=norme_SP
            
            
            
            
            
            
            
    
    
    
    
    



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
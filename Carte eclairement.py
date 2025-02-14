# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:35:27 2025

@author: routin
"""

import numpy as np
from Surface_library import Surface_plane
from Source_library import Source_blanche
import matplotlib.pyplot as plt

source1=Source_blanche(0, 0, 5, 5, 1,  [0,0,-1])
source2=Source_blanche(0, 8, 5, 5, 1,  [0,0,-1])
source5=Source_blanche(2, 4, 5, 30, 1,  [-7,0,-1])

liste_sources=[source1 , source2,  source5]

surface=Surface_plane(point_def=[0,0,0],v_normal=[0,0,1])
carte_coord_surface=surface.get_carte_coord(0.5,100)

a,b,rest=np.shape(carte_coord_surface)


carte_eclairement=np.zeros([a,b])

for k in liste_sources:
    carte_E=carte_coord_surface.copy()
    for i in range(a):
        for j in range(b):
            point_P=carte_E[i,j]
            point_S=[k.x,k.y,k.z]
            SP=point_P-point_S
            norme_SP=np.linalg.norm(SP)
            
            if norme_SP==0:
                raise Exception('la source est comprise dans le plan')
                
            SP_norme=SP/ norme_SP
            
            alpha=np.abs(np.arccos(np.dot(SP_norme,np.transpose(k.vecteur_direction))))
            I=k.intensity(alpha)
            
            psi=np.abs(np.arccos(np.dot(SP_norme,np.transpose(surface.vecteur_normal))))
            
            E=np.abs(I*np.cos(psi)/(norme_SP**2))
            
            carte_E[i,j]=E
            
            
    carte_eclairement=np.array(carte_eclairement)+np.array(carte_E)[...,0]
    
print(carte_eclairement)

plt.imshow(carte_eclairement, cmap='jet') #, interpolation='nearest'
plt.axis('off')  # Masquer les axes
plt.show()
            
            
    
    
    
    
    



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
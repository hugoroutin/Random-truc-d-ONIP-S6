# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:29:51 2025

@author: routi
"""

import numpy as np

class Source:
    def __init__(self, x, y, z, I0, delta, theta, zeta, name='René'):
        """
        PARAMS:
        x, y, z : floats 
                coordonnées de position de la source
        I0 : float
                Intensité de la source (de base)
        delta: float
                 je sais pas encore
        theta: float
                je sais pas encore
        zeta: float
                je sais pas encore   
        """
        self.x=x
        self.y=y
        self.z=z
        self.I0=I0
        self.delta=delta
        self.theta=theta
        self.zeta=zeta
        self.name=name
        
    def intensity(self, angle):
        """
        PARAMS:
        I0 : float
                Intensité de la source (de base)
        delta: float
                 je sais pas encore
        angle: float
                je sais pas encore
                
        RETURNS:
        intensity: float
                l'intensité (scoop)
        """
        intensity=self.I0 * np.exp(- (4 * np.log(2)) * (angle / self.delta) ** 2)
        return intensity
    
    def illumination(self, angle, distance):
        return None
        
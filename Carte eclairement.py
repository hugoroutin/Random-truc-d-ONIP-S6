# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:35:27 2025

@author: routin
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
        
    def intensity(self, angle, delta, I0):
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
        intensity=I0 * np.exp(- (4 * np.log(2)) * (angle / Delta) ** 2)
        return intensity
    
    def illumination(self, angle, distance):
        
        
        
class Surface:
    def __init__(self, plan, nom='Gazon'):
        """
        PARAMS:
        plan : Tuples de tuples de 3 floats
                coordonnées de 3 points sur lesquels seront défini la surface de travail
        SORTIE:
        vecteur_normal: array
                vecteur normal au plan de norme 1
        """
        A, B, C = map(np.array, plan)
        
        AB = B - A
        AC = C - A
        
        normal = np.cross(AB, AC)
        
        norme = np.linalg.norm(normal)
        if norme != 0:
            normal = normal / norme
        else: 
            raise Exception('Les points donnés ne forment pas un plan')
        self.vecteur_normal=normal
        
    
        
        
        
        
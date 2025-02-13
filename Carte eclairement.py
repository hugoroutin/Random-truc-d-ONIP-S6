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
        
        
        
class Surface:
    def __init__(self, point_def=None, v_normal=None, coord_points_plan= None, nom='Gazon'):
        """
        PARAMS:
        plan : Tuples de tuples de 3 floats
                coordonnées de 3 points sur lesquels seront défini la surface de travail 
                mettre None si on utilise la définition par vecteur normal
        v_normal: array
                vecteur normal au plan passant par point_def
                mettre None si on utilise la définitions 3 points
        point_def: array
                coord du point sur lequel se base le vecteur normal
                mettre None si on utilise la définitions 3 points
        SORTIE:
        vecteur_normal: array
                vecteur normal au plan de norme 1
        vecteur1, vecteur2: arrays
                deux vecteurs normés appartenant au plan
        """
        if coord_points_plan is not None:
            A, B, C = map(np.array, coord_points_plan)
            
            AB = B - A
            AC = C - A
            BC = C - B
            
            
            normal = np.cross(AB, AC)
            norme_normal = np.linalg.norm(normal)
            norme_AB=np.linalg.norm(AB)
            norme_AC=np.linalg.norm(AC)
            norme_BC=np.linalg.norm(BC)
            
            if norme_normal==0 or norme_AB==0 or norme_AC==0 or norme_BC==0 :
                raise Exception('Les points donnés ne forment pas un plan')
            normal = normal / norme_normal
            self.vecteur_normal=normal
            self.vecteur1=norme_AB
            self.vecteur2=norme_AC
            
        if (v_normal is not None) and (point_def is not None):
            normal=v_normal+point_def
            
            u = np.array([1, 0, 0]) if abs(normal[0]) < abs(normal[1]) else np.array([0, 1, 0])
            v = np.cross(normal, u)
            u = np.cross(v, normal)
            
            #on norme
            u /= np.linalg.norm(u)
            v /= np.linalg.norm(v)
            self.vecteur1=u
            self.vecteur2=v
            
        
        
        
            
        
        self.vecteur_normal=normal
        
    def get_carte_coord(self, intervalle, taille=100):
        """
        Parameters
        ----------
        taille : int
            taille du array carré renvoyé
        intervalle : float
            intervalle entre chaque point considéré

        Returns
        carte_coord: array
            arrray contenant les coord dans l'espace des points du plan

        """
    
        
        # u et v deux vecteurs normés du plan
        u=self.vecteur1
        v=self.vecteur2
        
        # Création des points du plan
        indices = np.linspace(-taille//2, taille//2, taille) * intervalle
        x, y = np.meshgrid(indices, indices)
        points = np.zeros((taille, taille, 3))
        
        for i in range(taille):
            for j in range(taille):
                points[i, j] = point_ancrage + x[i, j] * u + y[i, j] * v
        
        return carte_coord
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
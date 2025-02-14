# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:29:29 2025

@author: routi
"""
import numpy as np
        
class Surface_plane:
    def __init__(self, point_def=None, v_normal=None, coord_points_plan= None, nom='Platal'):
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
            print('normal eqg: '+str(normal))
            
            
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
            
            normal=np.array(v_normal) + np.array(point_def)
            print('normal'+str(normal))
            
            
            u = np.array([1, 0, 0]) if abs(normal[0]) < abs(normal[1]) else np.array([0, 1, 0])
            
            
            v = np.cross(normal, u)
            u = np.cross(v, normal)
            
            #on norme
            u = u/np.linalg.norm(u)
            v =v/ np.linalg.norm(v)
            self.vecteur1=u
            self.vecteur2=v
            
            
            norme_normal = np.linalg.norm(normal)
            if norme_normal==0:
                raise Exception('Les points donnés ne forment pas un plan')
            normal = normal / norme_normal
            self.vecteur_normal=normal
        self.point_def=point_def
            
        
        
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
                points[i, j] = self.point_def + x[i, j] * u + y[i, j] * v
        
        return points
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
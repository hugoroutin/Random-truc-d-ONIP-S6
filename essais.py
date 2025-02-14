# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:58:22 2025

@author: routi
"""

import numpy as np

# def vecteur_normal(plan: tuple) -> np.ndarray:
#     """
#     Calcule le vecteur normal au plan défini par trois points.
    
#     :param plan: Un tuple contenant trois tuples de trois floats chacun (coordonnées des points A, B et C)
#     :return: Un array numpy représentant le vecteur normal au plan
#     """
#     A, B, C = map(np.array, plan)
    
#     # Vecteurs directeurs du plan
#     AB = B - A
#     AC = C - A
    
#     # Produit vectoriel pour obtenir le vecteur normal
#     normal = np.cross(AB, AC)
#     # Normalisation du vecteur normal
#     norme = np.linalg.norm(normal)
#     if norme != 0:
#         normal = normal / norme
    
    
#     return normal


# print(vecteur_normal(((1,1,1),(2,2,2),(3,3,-3))))

v=np.array([0,0,1])
print(np.linalg.norm(v))
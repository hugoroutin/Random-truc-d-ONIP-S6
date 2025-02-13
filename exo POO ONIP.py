# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:22:36 2025

@author: routi
"""
import numpy as np

class Point:
    def __init__(self,x:float,y:float, name:str='ddddhd'):
        """class constructor point
        x= position selon l'axe x
        y= position selon l'axe y"""
        self.x=x
        self.y=y
        
    
        
    def move(self, x_add=float,y_add=float):
        """ajoute x_add, y_add aux coord du point"""
        self.x+=x_add
        self.y+=y_add
        
    def display(self):
        """affiche la position de l'objet"""
        print('position selon laxe x'+str(self.x))
        print('position selon laxe y'+str(self.y))
        
    def distance_abs(self):
        "return la distance au point (0,0)"
        print(np.sqrt((self.x)**2 + (self.y)**2))
        return np.sqrt((self.x)**2 + (self.y)**2)

point=Point(10,10)

point.display()
point.distance_abs()
point.move(5,-5)
point.display()
point.distance_abs()
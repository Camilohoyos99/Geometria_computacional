# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:04:28 2022

@author: Camilo Hoyos
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.tri import Triangulation
from scipy.spatial import Delaunay
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.interpolate import LinearNDInterpolator
from functions import compute_triangle_area, compute_triangle_angles
from scipy.sparse import csr_matrix


class TIN:
    def __init__(self, terrain):
        self.triangulation = Delaunay(terrain[:, :2])
        self.elevations = terrain[:,2]


    def graph_terrain_3d(self):
        fig, ax = plt.subplots(subplot_kw =dict(projection="3d"))
       
        plot_tria =Triangulation(self.triangulation.points[:, 0], 
                                 self.triangulation.points[:, 1], 
                                 triangles=self.triangulation.simplices)
        
        ax.plot_trisurf(plot_tria, self.elevations)
        
        plt.title("Terrain 3D")
       
        ax.set_zlabel("Elevation")
        plt.get_cmap('coolwarm')
        plt.show()
        
     
        
        
        
        
        
        
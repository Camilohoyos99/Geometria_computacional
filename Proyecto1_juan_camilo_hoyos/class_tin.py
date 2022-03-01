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
from scipy.sparse import csr_matrix
#from functions import compute_triangle_area, compute_triangle_angles

class TIN:
    def __init__(self, terrain):
        self.triangulation = Delaunay(terrain[:, :2])
        self.elevations = terrain[:,2]


    def graph_terrain_3d(self):
        fig, ax = plt.subplots(subplot_kw =dict(projection="3d"))
       
        plot_tria =Triangulation(self.triangulation.points[:, 0], 
                                 self.triangulation.points[:, 1], 
                                 triangles=self.triangulation.simplices)
        
        ax.plot_trisurf(plot_tria, self.elevations,cmap = 'coolwarm')
        
        plt.title("Terrain 3D")
       
        ax.set_zlabel("Elevation")
        #plt.get_cmap('coolwarm')
        plt.show()
        
        
    def interpolate_elevation(self, point):
       
        #terrain, triangle with the poiint, vertex
        terrain = np.concatenate((self.triangulation.points,
                                  np.array([self.elevations]).T),axis=1)
       
        triangle= self.triangulation.find_simplex(point)
        
        vertex= terrain[self.triangulation.simplices[triangle]] 
        
        #interpolation 
        interpolation = LinearNDInterpolator(vertex[:, :2], vertex[:, 2] ) 
        elevation= interpolation(point)[0]
        
        fig = plt.figure()
        plt.triplot(terrain[:, 0], terrain[:, 1], self.triangulation.simplices) # Grafica los triángulos
        
        
        # organizo los puntos para obtener la elevacion
        for p in vertex:
                
            plt.annotate(p[2], (p[0], p[1]))
        
        plt.plot(terrain[:, 0], terrain[:, 1], "o")
        plt.plot(point[0], point[1], "o", "r")
        plt.annotate(elevation,(point[0], point[1]))
        
        plt.xlim(min(vertex[:,0]) - 1, max(vertex[:,0]) + 1 )
        plt.ylim(min(vertex[:,1]) - 1, max(vertex[:,1]))
        plt.show()
        
        
        return 1
    
     
        

        
        
        
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



class TIN:
    def __init__(self, terrain):
        self.terrain_tri = Delaunay(terrain[:, :2])
        self.elevations = terrain[:,2]


    def graph_terrain_3d(self):
        fig, ax = plt.subplots(subplot_kw =dict(projection="3d"))
       
        plot_tria =Triangulation(self.terrain_tri.points[:, 0], 
                                 self.terrain_tri.points[:, 1], 
                                 triangles=self.terrain_tri.simplices)
        
        ax.plot_trisurf(plot_tria, self.elevations,cmap = 'coolwarm')
        
        plt.title("Terrain 3D")
       
        ax.set_zlabel("Elevation")
        #plt.get_cmap('coolwarm')
        plt.show()
        
        
    def interpolate_elevation(self, point, ):
       
        #terrain, triangle with the poiint, vertex
        terrain = np.concatenate((self.terrain_tri.points,
                                  np.array([self.elevations]).T),axis=1)
       
        triangle= self.terrain_tri.find_simplex(point)
        
        vertex= terrain[self.terrain_tri.simplices[triangle]] 
        
        #interpolation 
        interpolation = LinearNDInterpolator(vertex[:, :2], vertex[:, 2] ) 
        elevation= interpolation(point)[0]
        
        fig = plt.figure()
        plt.triplot(terrain[:, 0], terrain[:, 1], self.terrain_tri.simplices) # Grafica los triángulos
        
        
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
    
        

    def find_neighbors(pindex, triang):
        neighbors = list()
        for simplex in triang.vertices:
            if pindex in simplex:
                neighbors.extend([simplex[i] for i in range(len(simplex)) if simplex[i] != pindex])
        '''
        this is a one liner for if a simplex contains the point we`re interested in,
        extend the neighbors list by appending all the *other* point indices in the simplex
        '''
        #now we just have to strip out all the dulicate indices and return the neighbors list:
        return list(set(neighbors))
    
        
    def water_source(self,point):
        neighbors = []
      
        #for point in self.terrain_tri:
            
        terrain = np.concatenate((self.terrain_tri.points,
                                  np.array([self.elevations]).T),axis=1)
       
        
        triangle= self.terrain_tri.find_simplex(point)
        
        vertex= terrain[self.terrain_tri.simplices[triangle]] 
        
        interpolation = LinearNDInterpolator(vertex[:, :2], vertex[:, 2] ) 
        elevation= interpolation(point)[0]
        
        #neig = find_neighbors(point,)
        return interpolation



        
        
        
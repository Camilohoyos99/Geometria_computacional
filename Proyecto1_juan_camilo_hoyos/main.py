# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:41:54 2022

@author: Camilo Hoyos
"""
import numpy as np
from class_tin import TIN
import matplotlib.pyplot as plt


# charge the data

terrain = np.loadtxt("pts1000c.dat", unpack = True)
terrain = np.transpose(terrain)
tin = TIN(terrain)

# punto 1 graph of the terrain in 3D

tin.graph_terrain_3d()


# Punto 2
p = [-8,5]

elevacion_punto = tin.interpolate_elevation(p)

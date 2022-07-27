# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:16:25 2022

@author: ldpc8
"""
# Suma de matriz diagonal
import random
import numpy as np 

n = int(input("Ingrese el tamaño de la matriz: "))

matriz =[[0 for x in range(n)]for y in range(n)]
for i in range(0, n):
    for j in range(0, n):
        matriz[i][j] = random.randint(1, 100)
print(matriz)
trace = np.trace(matriz) 
print("La suma de la diagonal es:",trace) 
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 23:11:38 2022

@author: ldpc8
"""

"""
Dado un arreglo (flotantes) de n temperaturas, ingresar los 
valores y calcular la desviación estándar de los datos ingresados
"""
import statistics

def validar():
    n = int(input("Ingrese tamaño para el arreglo de las temperaturas: "))
    while n <= 0:
        n = int(input("Ingrese tamaño para el arreglo de las temperaturas: "))
    #Endwhile
    return n
#Enddef

n = validar()
q=[]
for x in range(n):
    x+=1
    z = float(input(f"Ingrese la temperatura {x}: "))
    while z <1:
        z = float(input(f"Ingrese la temperatura {x}: "))
    #Endwhile
    q.append(z)
#Endfor  
g = st_dev = statistics.pstdev(q)
print(f"La desviacion estandar de {q} es: {g}")




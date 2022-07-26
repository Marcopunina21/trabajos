# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:13:48 2022

@author: ldpc8
"""
import math
from math import factorial
    
def grados(g):
    r = g*(math.pi/180)
    return r
#Enddef

def cos(g):
    i=2
    k=1
    x=0  
    for i in range(1,(math.fabs(x)<= 0.000006)):
        i*=2
        x += ((-1)**k)*(pow(grados(g),i)/(factorial(i))) 
        k+=1
        if math.fabs(x)<= 0.000006:
            return x
    print(f"El coseno de {grados(g)} radianes es {1+x}")

g = float(input("Angulo en grados: "))
cos(g)
    


    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 09:25:43 2022

@author: ldpc8
"""

# Tabla de multiplicar

print("Tabla de multiplicar \n")

n = int(input("Ingrese el tamaño de la tabla: "))
while (n <= 0):
        n = int(input("Ingrese el tamaño de la tabla: ")) 
if n>0 :
            for h in range (1,n+1):
                print("")
                for i in range (1,n+1):
                    print(i*h,end=" ")
else:
            print("\nIngrese un numero positivo")
   
    
    
    
    
    
    
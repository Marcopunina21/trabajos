# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:03:47 2022

@author: ldpc8
"""

# Realizar un algoritmo para calcular todos los números 
# primos comprendidos entre 1 y n(entero positivo).

def primos():
    for i in range(1, x+1): # Rango
      if i>1: 
        for j in range(2,i): 
            if(i % j==0): # Calculo de los numeros primos
                break
            #Endif
        else: 
            print(i)
        #Endif
        #Endfor
    #Endfor
#Enddef
x = int(input("Digite un numero: "))
primos()

  

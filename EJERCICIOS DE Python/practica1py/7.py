# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:57:53 2021

@author: lab
"""

"""
Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la 
fórmula es: num_pulsaciones = (220 - edad) /10
"""
edad = int(input("Ingrese la edad de la persona: "))
num_pulsaciones = (220 - edad) /10
print(f"El numero de pulsaciones es de: {num_pulsaciones}")



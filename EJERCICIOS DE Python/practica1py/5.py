# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:57:52 2021

@author: lab
"""

"""
Cinco personas quieren conocer el total que pagarán por viajar a la ciudad de
Guayaquil, dos de ellas viajarán en camión de primera y las otras tres en uno de segunda, el camión de 
segunda cobra el 30% menos que el de primera.
A continuación se visualizan los resultados de una posible salida del programa:
Entrada: Valor a pagar en camión de primera.
Salida: Total a pagar por el viaje
"""
print(" -- Viaje Guayaquil --")

vpa = float(input("Ingrese el valor a pagar en camión de primera por cada persona: "))
x = vpa * 2
y = (vpa * 30)/100
h = vpa - y
u = h * 3
z = x + u
print(f"Total a pagar por el viaje: {z} dólares")










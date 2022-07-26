# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:57:52 2021

@author: lab
"""

"""
Un arquitecto desea decorar la entrada de un edificio con tres figuras geométricas 
Cuadrado, triángulo y circulo para ello necesita saber el área de cada figura para comprar el material, 
pero solo posee un dato que el dueño del edificio debe decidir.
Se sabe que la altura del triángulo siempre será de 55 cm y que el dato que debe darle el dueño también 
será en centímetros, además sabe que por cada centímetro cuadrado debe gastar 1 dólar con 25 
centavos. Visualizar el área de cada figura geométrica y el total a gastar en material.
A continuación, se visualizan los resultados de una posible salida del programa:
Entrada: Valor en centímetros que el dueño proporciona.
Salida: Área del cuadrado, área del triángulo, área del circulo, total a gastar.
"""
import math

print(" -- Medidas arquitecto --")

due = int(input("Ingrese el dato del dueño para las figuras: "))
ac = due*due
at = (due*55)/2
aci = math.pi * pow(due,2)
print(f"Área Cuadrado: {ac} cm^2")
print(f"Área Triangulo: {at} cm^2")
print(f"Área Circulo: {aci} cm^2")

x = (ac*1.25)+(at*1.25)+(aci*1.25)
print(f"Total a gastar en material: {x}")























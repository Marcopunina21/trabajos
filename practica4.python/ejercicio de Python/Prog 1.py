
# -*- coding: utf-8 -*-

"""
Escribir un programa que lea el monto de compra de cada tipo de producto y calcule el descuento
total y la cantidad a pagar.
"""
print("Digite 4 numeros flotantes")
Dol_A = float(input("Producto A: "))
Dol_B = float(input("Producto B: "))
Dol_C = float(input("Producto C: "))
Dol_X = float(input("Producto X: "))
y = (Dol_B * 0.05 ) + (Dol_C * 0.08) + (Dol_X * 0.10)
x = (Dol_X+Dol_A+Dol_B+Dol_C) - y
print("Descuento: ", y)
print("Pago: ", x)

# -- coding: utf-8 --
"""
Created on Thu Dec 16 19:05:32 2021

@author: ldpc8
"""

# En un supermercado de Quito, todo se vende por kilos, realiza un programa que 
# permita ingresar los kilos de carne, pan, azúcar, arroz, pescado, papas, queso y que calcule el total a 
# cancelar por todas las compras. La tabla de precios que exhibe el supermercado es la siguiente:

print(" -- Total de Compras -- ")
carne = float(input("Ingrese los kilos de carne comprada: "))
pan = float(input("Ingrese los kilos de pan comprada: "))
azúcar = float(input("Ingrese los kilos de azúcar comprada: "))
arroz = float(input("Ingrese los kilos de arroz comprada: "))
pescado = float(input("Ingrese los kilos de pescado comprada: "))
papas = float(input("Ingrese los kilos de papas comprada: "))
queso = float(input("Ingrese los kilos de queso comprada: "))
x = (carne*3.50)+(pan*1.65)+(azúcar*2.55)+(arroz*3)+(pescado*2.45)+(papas*2.25)+(queso*1.55)
print(f"El total de la compra es: {x}")
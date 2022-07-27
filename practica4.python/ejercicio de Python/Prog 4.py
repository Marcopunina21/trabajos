
# -*- coding: utf-8 -*-

"""
El índice de masa corporal es una medida de asociación entre la masa y la talla de una persona.
Específicamente: imc = masa/estatura²
Tu misión es escribir un programa que reciba masa y estatura de una persona, y que imprima su
índice de masa corporal en kg/m^2, incluyendo la unidad de medida y la observación sobre el nivel
de peso.
"""
a = input("Nombre: ")
b = float(input("Ingrese su peso (Kg): "))
c = float(input("Ingrese su altura (m): "))
d = pow(c,2)
e = b/d
if e < 18.5:
    print(f"{a} tiene un IMC de {round(e,2)} kg/m^2")
    print("Observación sobre peso: Bajo peso")
else:
    if 18.5 <= e <= 24.9:
        print(f"{a} tiene un IMC de {round(e,2)} kg/m^2")
        print("Observación sobre peso: Normal")
    else:
        if 25 <= e <= 29.9:
            print(f"{a} tiene un IMC de {round(e,2)} kg/m^2")
            print(f"Observación sobre peso: Sobrepeso")
        else:
            print(f"{a} tiene un IMC de {round(e,2)} kg/m^2")
            print(f"Observación sobre peso: Obeso")
   




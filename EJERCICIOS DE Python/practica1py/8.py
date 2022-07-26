# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:33:02 2021

@author: lab
"""

"""
La masa de aire de un airbag depende de la presión, el volumen y su temperatura de funcionamiento. 
La fórmula es: masa = (presión * volumen) / (0.37 * (temperatura + 460)). Obtener la masa de un airbag 
solicitando los valores respectivos al usuario.
"""

presion = float(input("Digite la presion: "))
volumen = float(input("Digite la volumen: "))
temperatura = float(input("Digite la temperatura: "))
masa = (presion * volumen) / (0.37 * (temperatura + 460))
print(f"LA masa del airbag es de {masa}")




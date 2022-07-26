# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 12:12:40 2022

@author: ldpc8
"""

"""
Dado el valor de X para N elementos, realice un algoritmo 
para obtener el resultado de la siguiente serie:
Ser= X + X2/3 + X3/5 + X4 /7 + X5/9+.....Xn/Y
"""

def pali(t):
    t = t.lower()
    t = t.replace(' ', '')
    l = len(t)
    if l % 2 == 0:
        i = t[:l // 2]
        d = t[l // 2:]
    else:
        i = t[:l // 2]
        d = t[l // 2 + 1:]
    #Endif
    return i == d[::-1]
#Enddef

x = input("Digite una frase: ")
print(pali(x))









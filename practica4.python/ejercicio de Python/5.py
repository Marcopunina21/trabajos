# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 12:12:38 2022

@author: ldpc8
"""
"""
Dado el valor de X para N elementos, realice un algoritmo 
para obtener el resultado de la siguiente serie:
Ser= X + X^2/3 + X^3/5 + X^4 /7 + X^5/9+.....Xn/Y
"""
def y():
    t=0
    h=0
    for k in range(4,n):
        k+1
        for i in range(0,n+k,2):
            i+=1  
            t+=1
            h+=(x**t)/i 
    print(round(h, 2))
x = int(input("Digite una base 'x': "))          
n = int(input("Digite un exponente 'n': "))
y()






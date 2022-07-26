# -*- coding: utf-8 -*-
"""
Created on Sun May 22 09:01:40 2022

@author: USER
"""

n = int(input('Ingrese un numero: '))
print('')
for i in range(n+0, 0, -1):
    for j in range(1, i+1):
        print(i, end='')
    print('')
for i in range(2, n+1):
     for j in range(1, i+1):
        print(i, end='')
print('')
    

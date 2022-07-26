# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 09:25:46 2022

@author: ldpc8
"""
# Primos
def primo(a):
    b=0
    x=a+1 
    for a in range(1,x):
        for i in range(1,x):
            if a % i==0:
                b+=1
        if b==2:
            print(a)
        b=0
    return a
a = int(input("Ingrese un numero: "))
while  a>1000 or a<1:
    a = int(input("Ingrese un numero: "))
primo(a)
    
    
    
    
    
    
    
    
    
    
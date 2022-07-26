# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:34:11 2022

@author: USER
"""
#numeros primos 
def isPrime(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return isPrime(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False
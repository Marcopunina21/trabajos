# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:12:39 2022

@author: USER
"""

def isPrime(num):
    
    
    
    
    
    
    for i in range(1, 20):
        if isPrime(i + 1):
            print(i + 1, end=" ")
            print("No es primo", i, "es divisor")
            return False
    print("Es primo")
    return True

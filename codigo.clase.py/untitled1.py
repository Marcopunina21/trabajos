# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:16:04 2022

@author: USER
"""

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True
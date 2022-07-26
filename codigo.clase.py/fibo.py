# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 12:02:06 2022

@author: USER
"""

def fib(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        """c=a+b
        a=b
        b=c"""
        a, b = b, a+b

#print()
fib(8)

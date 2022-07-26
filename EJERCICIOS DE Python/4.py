# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 09:25:45 2022

@author: ldpc8
"""

# Triángulo de números

comprobar = True
while comprobar:
        n = int(input("Ingrese un número: "))
        if n>0 :
            comprobar = False
            for i in range (1,n+1):
                print("")
                for h in range (1,i+1):
                    print(h,end=" ")
            for i in range (n-1,0,-1):
                print("")
                for h in range(1,i+1):
                    print(h,end=" ")   
        else:
            print("\nIngrese un numero positivo")
            
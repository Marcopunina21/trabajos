
 
import math
def factorial (n ):
    factorial = 1 ; 
    for i in range(1,n):
        factorial=factorial*i
    return factorial
pos = 1 
acumulador = 0
n=int(input("Ingrese n : "))

for i in range(1,n+1,2):
    print('i: ',i)
    if ( i == 1 ):
          acumulador=n
    else:
       if ( ( pos % 2 ) == 0 ):
        acumulador = acumulador - (math.pow( i , i ) / ( factorial ( i ) * 1.0 ) )
       else:
        acumulador=acumulador + ( math.pow ( i , i ) / ( factorial ( i ) * 1.0 ) )
             
    pos+=1       
print('y:',acumulador) 
    









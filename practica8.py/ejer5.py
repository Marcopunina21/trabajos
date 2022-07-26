#NUMERO PALÍNDROMO

def numero_palin(num):
    n=str(num)
    inverso=n[::-1]

    if inverso==n and num>=10:
    
        return True
    else:
        return False

A=int(input('Ingrese un numero: '))
if numero_palin(A):
    print(F'{A} palindromo ')
else:
    print(F'{A} no palíndromo')






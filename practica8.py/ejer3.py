#NUMERO MAYOR DE TRES NÚMEROS
def numeroMayor(A,B,C):

    mayor=0
    
    if A>B:
        mayor=A
    if A>C:
        mayor=A
    if C>mayor:
        mayor=C
    if B>mayor:
        mayor=B
    return mayor

A=int(input('Ingrese A: '))
B=int(input('Ingrese B: '))
C=int(input('Ingrese C: '))
print()
print(f'Numero mayor:{numeroMayor(A,B,C)}')
print()

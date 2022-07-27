#practica 6 ejercicio 4
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
    
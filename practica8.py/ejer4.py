# NUMERO PRIMO
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


numero_primos = []
for i in range(2, 150):
    if es_primo(i):
        numero_primos.append(i)

# inprimir tabla
filas = 5
columnas = 7
contador = 0
numero_primos.reverse()
for i in range(filas):
    print(' ', end=' ')

    for j in range(columnas):
        print(f'{numero_primos[contador]} \t ', end='  ')
        contador += 1
    print('\n')

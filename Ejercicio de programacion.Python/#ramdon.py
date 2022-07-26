

n=int(input("Ingrese cuantos numeros aleatorios desea obtener: "))
# Numeros randomicos 
import random
def listaAleatorios(n):
    lista = [1] * n
    for i in range(n):
        lista[i] = random.random()
    return lista

aleatorios=listaAleatorios(n)
print(aleatorios)


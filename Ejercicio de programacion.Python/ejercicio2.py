partida1 = int(input('Ingrese el puntaje de la primera partida: '))
partida2 = int(input('Ingrese el puntaje de la segunda partida: '))
partida3 = int(input('Ingrese el puntaje de la tercera partida: '))

numeros = [partida1, partida2, partida3]
numeros.sort()

mejor_puntaje1 = numeros[1]
mejor_puntaje2 = numeros[2]

suma_total = mejor_puntaje1+mejor_puntaje2
print('puntaje final es: ', suma_total)


"""
mejor_puntaje1 = 0
mejor_puntaje2 = 0
suma_total = 0


# suponemos que la partida 1 es la mejor
if(partida1 > partida2 and partida1 > partida3):
    mejor_puntaje1 = partida1

# supenemos que la partdi2 es mejor que la partida3
if(partida2 > partida3 or partida2 > partida1):
    mejor_puntaje1 = partida2
    mejor_puntaje2 = partida3


suma_total = mejor_puntaje1+mejor_puntaje2
print("el puntaje final es: ", suma_total)
"""

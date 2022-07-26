import random
seguir=True
while seguir:
    filas=int(input('Ingrese las filas:'))
    columnas=int(input('Ingrese las columnas: '))

    if filas<4 or filas>30 or columnas<4 or columnas>30:

       print('Infrese un numero mayor que 4 y menor que 30: ')
    else:
        seguir=False

def mostrar_matriz(matrix):
    for fila in matrix:
        print(fila)
        

matrix = [ [ int ( ) for i in range ( filas) ] for j in range ( columnas ) ] 
# SE USA DOS FOR UNA PARA LAS FILAS Y OTRO PARA LAS COLUMNAS 
for i in range ( filas ) : 
    for j in range (columnas ) : 
     # LLENAR LA MATRIZ CON LOS VALORES INGRESADOS 
        valor = random.randrange(1,100) 
        matrix [ i] [ j ] = valor 

for i in range ( filas ) : 
    print ( " " , end = " " ) 
    for j in range ( columnas ) : 
        print ( matrix [ i ] [ j ] , " | " , end = " " ) 
    print ( " \n " ) 





mostrar_matriz(matrix)

filas=len(matrix)
columnas=len(matrix[0])


for i in range(filas):
    suma=sum(matrix[i])
    matrix[i].appendc(suma) 

print()

print(matrix)


  # Para sumar simplemente recorremos la matrix y aumentamos el valor
suma = 0
for valor in matrix:
    for numero in valor:
        suma = suma + numero

print(f"La suma es {suma}")

# Y el promedio se obtiene dividiendo la suma entre la cantidad de elementos
cantidad_elementos = len(matrix)
promedio = suma / cantidad_elementos
print(f"El promedio es {promedio}")

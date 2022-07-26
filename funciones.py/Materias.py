import random
seguir = True
while seguir:
    filas = int(input('Ingrese las filas:'))
    columnas = int(input('Ingrese las columnas: '))

    if filas > 10 or columnas > 7:

        print('el maximo de filas es 10 y columnas es 7:')
    else:
        seguir = False

matrix = [[0 for x in range(columnas)]for j in range(filas)]

lista_materias = ['Quimica', 'Calculo', 'Programacion', 'Mecanica', 'Dinamica',
                  'Estatica', 'Dibujo', 'Algebra', 'Ecuaciones', 'Comunicacion']

# SE USA DOS FOR UNA PARA LAS FILAS Y OTRO PARA LAS COLUMNAS
for i in range(filas):
    for j in range(columnas):
     # LLENAR LA MATRIZ CON LOS VALORES INGRESADOS
        valor = random.randrange(1, 10)
        matrix[i][j] = valor
# Aqui imprimimos la matrix\
for i in range(filas):
    
    print(lista_materias[i], "   \t|", end=" ")
    for j in range(columnas):
        print(matrix[i][j], "|\t", end=" ")
    print(" \n ")

#recorremos la fila, sumamos la fila y dividimos para el tamanio
def promedio_materia(matrix):
    lista_promedio = []
    for i in range(filas):
        promedio = sum(matrix[i])/len(matrix[i])
        lista_promedio.append(promedio)
    print('===========================================')
    print('Materia |\t Promedio')
    for i in range(filas):
        print(f'{lista_materias[i]} |\t {lista_promedio[i]}')

#calculamos el promedio de la nota
def promedio_nota(matrix):
    promedio_notas = []   # lista pa promedio
    for i in range(columnas):   # este for recoore las columnas
        notas = [filas[i] for filas in matrix]    # aqui recorre las filas
        promedio = sum(notas)/len(notas) 
        promedio_notas.append(promedio) # el append rellena la lista
    print('===========================================')
    print('Nota |\t Promedio')
    for i in range(columnas):
        print(f'Notas {i+1} |\t {promedio_notas[i]}')

#metodo en donde el usuario escogera una opcion especifica de una mteria que quiera saver
def materia_especif(materia, matrix):
    pro_mate = sum(matrix[materia-1])/len(matrix[materia-1])
    print('===========================================')
    print('Materia |\t Promedio')
    print(f'{lista_materias[materia-1]} |\t {pro_mate}')


def promedi_notaespecifi(nota, matrix):
    nota1 = [filas[nota-1] for filas in matrix]
    promedio = sum(nota1)/len(nota1)
    print('===========================================')
    print('Nota |\t Promedio')
    print(f'Nota {nota} |\t {promedio}')


salir = False
while not salir:
    print('====================Menu=================')
    print('1.- Promedio por materia')
    print('2.- Promedio por nota')
    print('3.- Promedio por materia especifica: ')
    print('4.- Promedio por nota especifica: ')

    print('5.- Salir ')
    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:
        promedio_materia(matrix)
    if opcion == 2:
        promedio_nota(matrix)

    if opcion == 3:
        print('selecione la materia')
        for i in range(filas):
            print(f'{i+1}.- {lista_materias[i]}') # imprimos las notas
        materia = int(input('Ingrese opcion: '))
        materia_especif(materia, matrix)

    if opcion == 4:
        print('selccione la nota')
        for i in range(columnas):
            print(f'{i+1}.- nota {i+1}')
        nota = int(input('Ingrese una opcion: '))
        promedi_notaespecifi(nota, matrix)

    if opcion == 5:
        print('Gracias por usar el programa')
        salir = True

import math
import matplotlib.pyplot as plt
import numpy as np


RANGO = 4
bandera = True


def calculo_fuerza_x(fuerza, angulo):
    fuerza_x = fuerza * math.cos(math.radians(angulo))
    return fuerza_x


def calculo_fuerza_y(fuerza, angulo):
    fuerza_y = fuerza * math.sin(math.radians(angulo))
    return fuerza_y


def grafica_fuerzas(angulos, fuerzas):
    angulo1, angulo2, angulo3, angulo4 = angulos
    fuerza1, fuerza2, fuerza3, fuerza4 = fuerzas
    xmin, xmax, ymin, ymax = -5, 5, -5, 5
    ticks_frequency = 1
    fig, ax = plt.subplots(figsize=(10, 10))
    fig.patch.set_facecolor('#ffffff')

    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
    ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)
    plt.text(0.49, 0.49, r"$O$", ha='right', va='top',
             transform=ax.transAxes,
             horizontalalignment='center', fontsize=14)

    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])
    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # graficamos un punto

    x = np.linspace(0, angulo1, 50)
    y = np.linspace(0, angulo1, 50)

    plt.plot(x, y, 'b', linewidth=2)
    plt.show()


print("============================== BIENVENIDO =============================")
print("========== Calculadora de fuerzas ==========")

fuerzas_libras = []
print("Ingrese la fuerza en libras:")
for i in range(RANGO):
    correcto = True
    while correcto:
        fuerza = input("Fuerza " + str(i+1) + ": ")
        if fuerza.isnumeric() and int(fuerza) > 0:
            fuerzas_libras.append(int(fuerza))
            correcto = False
        else:
            print('Ingrese una fuerza mayor o igual a 1 ')


angulos = []
print("Ingrese los angulos en grados para cada fuerza:")
for i in range(RANGO):

    correcto = True
    while correcto:
        angulo = input("Angulo " + str(i+1) + ": ")
        if angulo.isnumeric() and int(angulo) > 0:
            angulos.append(int(angulo))
            correcto = False
        else:
            print('Ingrese un angulo mayor o igual a 1')
    # calcular las fuerzas en X
fuerzas_x = []
for i in range(RANGO):
    fuerzas_x.append(calculo_fuerza_x(fuerzas_libras[i], angulos[i]))

    # calcular las fuerzas en Y
fuerzas_y = []
for i in range(RANGO):
    fuerzas_y.append(calculo_fuerza_y(fuerzas_libras[i], angulos[i]))

    # sumar las fuerzas en X
fx_1, fx_2, fx_3, fx_4 = fuerzas_x

sum_fuerzas_x = fx_1 - fx_2 - fx_3 + fx_4

# sumar las fuerzas en Y
fy_1, fy_2, fy_3, fy_4 = fuerzas_y
sum_fuerzas_y = fy_1 + fy_2 - fy_3 - fy_4

# calcular la magnitud
magnitud = math.sqrt(sum_fuerzas_x**2 + sum_fuerzas_y**2)

# calcular el angulo tangente negativa
angulo_tangente = abs(math.degrees(math.atan(sum_fuerzas_y/sum_fuerzas_x)))


seguir = True
while seguir:
    print('======================Menu=================')
    print('1.- Sumatoria de fuerzas en X ')
    print('2.- Sumatoria de fuerzas en Y ')
    print('3.- Magnitud')
    print('4.- Direccion')
    print('5.- Todo')
    print('6.- Grafica')
    print('7.- Salir')
    opcion = int(input('Selecciones una opcion: '))
    if opcion == 1:
        print("============================== RESULTADO =============================")
        print("Fuerza en X:", round(sum_fuerzas_x, 2))
    if opcion == 2:
        print("============================== RESULTADO =============================")
        print("Fuerza en Y:", round(sum_fuerzas_y, 2))
    if opcion == 3:
        print("============================== RESULTADO =============================")
        print("Magnitud:", round(magnitud, 2))
    if opcion == 4:
        print("============================== RESULTADO =============================")
        print("Direccion:", round(angulo_tangente, 2))
    if opcion == 5:
        print("============================== RESULTADOS =============================")
        print("Fuerza en X:", round(sum_fuerzas_x, 2))
        print("Fuerza en Y:", round(sum_fuerzas_y, 2))
        print("Magnitud:", round(magnitud, 2))
        print("Direccion:", round(angulo_tangente, 2))
    if opcion == 6:
        print('Grafica')
        grafica_fuerzas(angulos, fuerzas_libras)

    if opcion == 7:
        seguir = False
        print("Gracias por usar la calculadora de fuerzas")

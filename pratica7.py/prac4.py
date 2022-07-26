import math


def calcular_seno(n):
    x = math.radians(n)
    return math.sin(x)


def calcular_cos(n):
    x = math.radians(n)
    return math.cos(x)


def calcular_tan(n):
    x = math.radians(n)
    return math.tan(x)


angulos = [30, 60, 90, 120]
for i in angulos:
    print(f'Sin:{i}={calcular_seno(i)}')
    print(f'Cos:{i}={calcular_cos(i)}')
    print(f'Tan:{i}={calcular_tan(i)}')

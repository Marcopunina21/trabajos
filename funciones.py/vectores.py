import random


def numeroPrimo(numero):
    band = True
    m = int(2)
    while((band) and (m < numero)):
        if (numero % m == 0):
            band = False
        else:
            m = m+1

    if (band):
        return True

    return False


A = [0, 0, 0, 0, 0, 0, 0]
C = int(0)
bandera = True

While(bandera):
    numero = random.randint(2, 1001)
    if(numeroPrimo(numero)):
        A[C] = numero
        C = C+1

        if(C == 10):
            bandera = False

for x in range(0, 10):
    print(str(A[x]))

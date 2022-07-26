# practica 4 ejercio 1
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a == 0:
    print('Divicion para cero')

else:

    d = ((b**2)-(4*a*c))

    if d < 0:
        print('Raiz negativa')
    else:
        x1 = (-b+((b**2)-(4*a*c))**0.5)/2*a
        x2 = (-b-((b**2)-(4*a*c))**0.5)/2*a
    x = x1 and x2
    if x > 0:
        print('Unica solcion:')
        print('x: ', x)
    else:

        print('Dos soluciones:')
        print('x1: ', x1)
        print('x2: ', x2)

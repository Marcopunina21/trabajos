# practica 4 ejercio 1
a = int(input('Ingrrese el valor de a: '))
b = int(input('Ingrrese el valor de b: '))
c = int(input('Ingrrese el valor de c: '))

d = ((b**2)-(4*a*c))
if d < 0:
    print('no exiten valores reales!')
else:
    x1 = (-b+((b**2)-(4*a*c))**0.5)/2*a
    x2 = (-b-((b**2)-(4*a*c))**0.5)/2*a

print('El valor de x1: ', x1)
print('El valor de x2: ', x2)

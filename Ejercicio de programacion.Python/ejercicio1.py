# EJERCICIO 1
numero_acl = int(float(input('Ingrese el numero de ACL: ')))

if(numero_acl >= 1 and numero_acl <= 99):
    print('El dato ingresado corresponde a una ACL de tipo Estándar')
elif(numero_acl >= 1300 and numero_acl <= 1999):
    print('El dato ingresado corresponde a una ACL de tipo Estándar en rango expandido')
elif(numero_acl >= 100 and numero_acl <= 199):
    print('El dato ingresado corresponde a una ACL de tipo Extendida')
elif (numero_acl >= 2000 and numero_acl <= 2699):
    print('El dato ingresado corresponde a una ACL de tipo Extendida en rango expandido')

else:
    print('El dato ingresado, no corresponde a una ACL')


#print(f'Su numero es: {numero_acl}')

import re
def validar(nombre, edad, cedula, email):
    es_valido = False
    if len(nombre)> 4:
        es_valido = True

    if edad > 18 and edad < 100:
        es_valido = True
    if len(cedula) == 10:
        es_valido = True
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower()):
        es_valido = True

    return es_valido
nombre = input("Ingres el monbre: ")
edad = int(input("Ingres la edad: "))
cedula = input("Ingres la cedula: ")
email = input("Ingres el email: ")

print(f"El nombre es {nombre} su edad es {edad} el numero de cedula es {cedula} su email {email}")

if validar(nombre, edad, cedula, email):
    print('Datos correctos')
else:
    print("Datos incorrectos")

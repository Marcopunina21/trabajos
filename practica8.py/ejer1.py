#CONVERSIÓN DE GRADOS CELSIUS A GRADOS FAHRENHEIT
def celsius_a_fahrenheit(c):
    return (c * 1.8) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) / 1.8

c = float(input("Grados Celsius: "))
f = celsius_a_fahrenheit(c)
print(f"Grados Fahrenheit: {f}")

f = float(input("Grados Fahrenheit: "))
c = fahrenheit_a_celsius(f)
print(f"Grados celsius: {c}")


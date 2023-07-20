'''
###############################################################################
Operadores de Comparación en Python
###############################################################################

Los operadores de comparación en Python estan representados por:
>
<
>=
<=
==
!=
'''

# Comparando Cadena de caractereres
print("Apple" == "Apple")
print("Apple" == "apple")
print("1" == 1)

# Comparando Números
print(7 > 3) # Devuelve un True
print(5 < 3) # Devuelve un False

print(2 >= 1) # True
print(8 <= 8) # True

print(3 == 33) # False
print(2 != 2) # False

# Trabajando con valores flotantes:

x = 3.3
print(x)

y = 1.1 + 2.2
print(y)

print(x == y)

tolerance = 0.00001
print(abs(x-y) < tolerance)
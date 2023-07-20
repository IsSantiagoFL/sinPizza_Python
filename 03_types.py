'''
Tipos de datos en Python :
'''

## La diversidad "type()" imprime el tipo de dato de la variable

#1. Cadena: Cadena de caracteres.
nombre = "Santiago"
edad = "12"
## Los "input ()" siempre entre una variabloe de tipo string.

#2. Int: Número entero.
edad = 20

#3. Booleano: Verdadero o Falso
comida = True
dormir = False

print(type(edad))

'''
###############################################################################
tipo de dato: str
###############################################################################
'''

nombre = "Santiago"
apellido = "Flores"

template_1 = "Hola, mi nombre es " +  nombre + ", y mi apelido es " + apellido
print("v1: ", template_1)

template_2 = "Hola, mi nombre es {}, y mi apelido es {}".format(nombre, apellido)
print("v2: ", template_2)

template_3 = f"Hola, mi nombre es {nombre}, y mi apellido es {apellido}"
print("v3: ", template_3)

'''
###############################################################################
tipo de dato: numbers
###############################################################################                                                                          
Por defecto, con numeros muy grandes o muy pequeños, python lo representa con notación
científica
'''
x = 4500000000000000000.056
y = 0.000000000000000674

print(x)
print(y)


año_1 = 20 # int
año_2 = 40

temperatura = 12.34 # float

año_3 = año_1 - 2
print(año_3)

año_3 += 4
print(año_3)

año_3 -= 2
print(año_3)


'''
###############################################################################
tipo de dato: Booleans
###############################################################################
'''

varon = True
mujer = False

print(not True)

print(varon)
varon = not varon
print(varon)          

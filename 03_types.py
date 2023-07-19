'''
Tipos de datos en Python :
'''

# La diversidad "tipo ()" imprime el tipo de dato de la variable

# Cadena: Cadena de caracteres.
nombre = "Santiago"
edad = "12"
## Los "input ()" siempre entre una variabloe de tipo string.

# Int: Número entero.
edad = 20

# Booleano: Verdadero o Falso
comida = True
dormir = False

'''
tipo de dato: str
'''

nombre = "Santiago"
apellido = "Flores"

template_1 = "Hola, mi nombre es " +  nombre + ", y mi apelido es " + apellido
print("v1: ", template_1)

template_2 = "Hola, mi nombre es {}, y mi apelido es {}".format(nombre, apellido)
print("v2: ", template_2)

template_3 = f"Hola, mi nombre es {nombre}, y mi apellido es {apellido}"
print("v3: ", template_3)
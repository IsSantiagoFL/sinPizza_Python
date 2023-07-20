'''
###############################################################################
Listas "arrays" en Python
###############################################################################

Pueden tener elementos de diferentes tipos,
Se pueden actualizar, realizando cambios intenrnos (en las tuplas no se puede hacer esto)

'''

numbers = [1, 2, 3, 4, 5]

paises = ["Perú", "Bolivia", "Venezuela"]

mixto = [1, True, "hola mundo"]

# Obtener un elemento especifico de una lsita, según su posición

pais_1 = paises[0]
print(pais_1)

print("El número 1 de la lsita es: ", numbers[0])

# Actualizar un elemento de una lista:

print(paises)
paises[1] = "Ecuador"
print(paises)

# Seleccionar solo ciertos elementos de una Lista

print("los ultimos 3 numeros de la lista son", numbers[-3:])


# Verificar o buscar si hay cierto elemento dentro de una lista

print(5 in numbers)


'''
###############################################################################
Métodos con Listas, en Python
###############################################################################
CRUD: Create, Read, Update & Delete
'''
# Crear una lista
numeros = [1, 2, 3, 4, 9]

# Update el valor de un elemento de una lista
numeros[-1] = 6
print(numeros)

# Añadir un elemento nuevo a una lista, en las posiciones indicadas
numeros.insert(0, 0)
numeros.insert(-1, 5)
print(numeros)

# Añadir un elemento, siempre en la ultima posición, añadir elementos nuevos:
numeros.append(7)
print(numeros)

# Anexar listas, una al lado de la otra:
numeros_2 = [8, 9, 10, 11, 12]

numeros_3  = numeros + numeros_2
print(numeros_3)

# Obtener la posición de un elemento
colores = ["rojo", "verde", "azul", "morado", "amarillo", "naranja", "purpura"]

index_azul = colores.index("azul")
colores[index_azul] = "blanco"

print(colores)

# Eliminar elementos de una lista
colores.remove("purpura") # Eliminar elemento por su contenido
print(colores)

colores.pop(2) # Elimninar elementos segun su numero de orden
print(colores)

colores.pop() # Elimina automaticamente el ultimo elemento de la lista
print(colores)

# Invertir el orden de los elementos de una lista
numeros.reverse()
print(numeros)

# Ordenar elementos
numeros.sort() # Ordenara los elementos de menor a mayor
print(numeros)

colores.sort() # Ordenara los elementos alfabeticamente
print(colores)
'''
###############################################################################
Tuplas en Python
###############################################################################

Pueden tener elementos de diferentes tipos,
Son inmutables: No se pueden realizar cambios internos (en las listas si.)

'''

# Crear tuplas
numeros = (1, 2, 3, 5)
nombres = ("Santiago", "María", "Juan", "Flor")

'''
Como son inmutables, no todos los métodos crud, funcionan,
se puede entender como que las tuplas son solo de lectura

por lo tanto solo funcionaran los CRUDS, metodos, de lectrua
'''

# Transformar una Tupla a una Lista y visceversa

mi_lista = list(nombres)

mi_tupla = tuple(mi_lista)
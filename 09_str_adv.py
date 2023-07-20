'''
###############################################################################
Strings, funciones avanzadas en Python
###############################################################################
'''

text_1 = "Ella sabe programar en python"
obs = "javascript" in text_1 # "Busca la palabra javascript en el contenido de la variable text_1"

n_caracteres = len("amo r") # Cuenta el número de caracteres, incluyendo espacios
print(n_caracteres)

# Métodos para operar con strings
text_M = text_1.upper() # Convierte todo el texto a mayusculas
print(text_M)

text_m = text_M.lower() # Convierte todo el texto a minusculas

text_a = text_1.count("a") # Cuenta cuantas veces esta "a" en el texto

text_I = text_1.swapcase() # Invierte las mayusculas y minusculas entre si.

text_c = text_1.startswith("Ella") # True o False, si el texto comienza con "Ella"
text_f = text_1.endswith("Python") # True o False, si el texto termina con "Python"

text_go = text_1.replace("Python", "Go") # Remplaza cada palabra Python con Go

"titulo de una novela".capitalize() # La primera letra de la oración, se convierte en mayuscula
"titulo de una novela".title() # LA primera letra de cada palabra se vuelve en mayusculas

"mesa".isdigit() # Evalua si potencialmente es un digito
"53532".isdigit() # Si puede llegar  aser un digito, True


# Indexing: Es acceder a un caracter en una posición determinada en el strg

print(text_1[0]) # Accede al primer caracter, comenzando a contar desde 0, sería "E"
print(text_1[-1]) #  Accede al ultimo caracter, el "-" empieza a contar de derecha a izquierda

# Slicing: Es seleccionar una parte del caracter
print(text_1[0:5]) # Esto seleeciona solo los 6 primeros elementos del strg
print(text_1[:10]) # Comienza desde el el primer elemento hasta el 10
print(text_1[5:]) # Desde el elemento en la psoción 5 hasta el ultimo
print(text_1[:]) # Desde el primer elemento hasta el utlimo elemento, toda la cadena de caracteres original

print(text_1[3:9:2]) # desde la psoción 3 a la 9, haciendo saltos de dos en dos.


'''
###############################################################################
Diccionarios en Python
###############################################################################

Pueden tener elementos de diferentes tipos,
Son inmutables: No se pueden realizar cambios internos (en las listas si.)

'''

my_dict = {} # Se define con corchetes

# Se necesita, una llave o valor, que contenera a un valor o definición

my_dict = {
  "llave o clave": "Valor,o definición",

  "Nombre": "Santiago",
  "Apellido": "Flores",
  "Edad": 20,
  "País": "Perú"
}

print(my_dict["Nombre"])
print(my_dict.get('gsdgs')) # No genera errores si no se encuentra la llave


# Actualizar valores de un diccionario
person = {
  "Nombre": "Santiago",
  "Apellido": "Flores",
  "Edad": 20,
  "País": "Perú",
  "Lenguajes": ["Python", "JS", "C"]
}

print(person)

person["Nombre"] = "Nicole"
person["Edad"] -= 2
person["Lenguajes"].append("C++")

del person["Apellido"]
person.pop("País")

print(person)

# Métodos con Diccionarios
print(person.items())
print(person.values())
print(person.keys())

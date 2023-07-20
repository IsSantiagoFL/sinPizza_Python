'''
###############################################################################
Condicionales en Python
###############################################################################
IF
IF-Else
'''
# IF

if True:
  print('Debería ejecutarse')

if False:
  print("Nunca debería ejecutarse")

# Ejemplos:
pet = input('¿Cual es tu mascota favorita? ')

if pet == "perro":
  print("Tienes buen gusto.")
if pet == "gato":
  print("Suerte.")

# IF - ELSE

pet = input('¿Cual es tu mascota favorita? ')

if pet == "perro":
  print("Tienes buen gusto.")
else:
  print("Mascota no encontrada :(")

# IF - ELIS - ELSE ¿Cual es la ventaja de usarlo respecto a varios IF- IF- IF?
pet = input('¿Cual es tu mascota favorita? ')

if pet == "perro":
  print("Tienes buen gusto.")
elif pet == "pez":
  print("Mala suerte.")
elif pet == "leon":
 print("guauuuu.")  
else:
  print("No tienes ninguna mascota interesante.")
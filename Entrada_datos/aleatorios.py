# Generar valores aleatorios

from random import randint

numero = randint(1, 10)
print(numero)

# Dado de 6 caras

dado = randint(1,6)
print(f'resultado de dado {dado}')

# Generador de id unico

Nombre = input("Introduce tu nombre: ")
Apellido = input("Introduce tu apellido: ")
Año = input("Introduce tu año de nacimiento (YYYY): ")
ID = randint(1000,9999)

Nombre_cad = Nombre[0:2].lower()
Apellido_cad = Apellido[0:2].lower()
Año_cad = Año[0:2]

print(f'ID generado: {Nombre_cad}{Apellido_cad}{Año_cad}{ID}')

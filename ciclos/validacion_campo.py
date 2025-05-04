


print("Validacion de campo de formulario")

nombre_usuario = None
while not nombre_usuario:
    nombre_usuario = input("Ingresa tu nombre de usuario: ")

print(f'nombre de usuario: {nombre_usuario}')


print("*** Función range en python ***")

print("Secuencia del 0 al 4: ")
#Inicio = 0
# Fin = 5-1 = 4
# Incremento = 1 (opcional)
for i in range(5):
    print(i, end=" ")

print("\n\n Secuendia del 10 al 20:")
for i in range(10,20+1):
    print(i, end=" ")

print("\n\n Secuencia del 20 al 30 de 2  en 2:")
for i in range(20,30 +1, 2):
    print(i, end=" ")
import random

print("Juego de adivinar el numero")

numero_secreto = random.randint(1,100)
salir = False
intentos = 0

while not salir:
    print("Adivina el numero entre 1 y 100")
    numero = int(input("Introduce un numero:"))
    intentos +=1
    if numero == numero_secreto:
        print(f"Has adivinado el numero en {intentos} intentos")
        salir = True
    else:
        print("Numero incorrecto, prueba de nuevo")

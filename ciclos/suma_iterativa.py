

print("Suma acumulativa")

Maximo = 5
numero = 1
acumulador_suma = 0

# Empezamos a iterar

while numero <= Maximo:
    # Sumar el numero al acumulador
    acumulador_suma += numero
    numero += 1 # Incrementar el numero

print(f'\n Resultado: { acumulador_suma}')

print("************")
print(" ")
print("Menu iterativo")

print("Sistema de administracion de cuentas")

salir = False
while not salir:
    print("1. Crear cuenta")
    print("2. Eliminar cuenta")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("Creando cuenta...\n")
    elif opcion == 2:
        print("Eliminando cuenta...\n")
    elif opcion == 3:
        print("Saliendo del sistema...\n")
        salir = True
    else:
        print("Intente de nuevo...\n")

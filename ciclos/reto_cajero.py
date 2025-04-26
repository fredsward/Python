

print("Sistema de cajero automatico")

Salir = False
Deposito = 0
retiro = 0
Total = 1000


while not Salir:
    print("1. Consultar saldo \n")
    print("2. Retirar saldo \n")
    print("3. Depositar saldo \n")
    print("4. Salir \n")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print(f"Su saldo es: {Total} \n")
    elif opcion == 2:
        retiro = int(input("Ingrese el monto a retirar: \n"))
        Total = Total - retiro
        print(f'Saldo disponible: {Total}')
    elif opcion == 3:
        Deposito = int(input("Ingrese el monto a depositar: \n"))
        Total = Total + Deposito
        print(f'Saldo disponible: {Total}')
    elif opcion == 4:
        print("Saliendo del sistema...\n")
        Salir = True        
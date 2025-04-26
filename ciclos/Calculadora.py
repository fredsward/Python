

print(" *** Calculadora ***")

Salir = False
while not Salir:
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Salir")

    opcion = int(input('Elige una opción:'))
    if opcion == 1:
        num1 = int(input("Introduce el primer numero:"))
        num2 = int(input("Introduce el segundo numero:"))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado} \n" )
    elif opcion == 2:
        num1 = int(input("Introduce el primer numero:"))
        num2 = int(input("Introduce el segundo numero:"))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado} \n" )
    elif opcion == 3:
        num1 = int(input("Introduce el primer numero:"))
        num2 = int(input("Introduce el segundo numero:"))
        resultado = num1 / num2
        print(f"El resultado de la division es: {resultado} \n" )
    elif opcion == 4:
        num1 = int(input("Introduce el primer numero:"))
        num2 = int(input("Introduce el segundo numero:"))
        resultado = num1 * num2
        print(f"El resultado de la multiplicacion es: {resultado} \n" )
    elif opcion == 5:
        Salir = True
        print("Saliendo de la calculadora...")
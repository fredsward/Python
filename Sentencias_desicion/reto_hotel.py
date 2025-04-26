


Nombre_cliente = input("Ingrese su nombre: ")
Dias_estadia = int(input("Ingrese los dias de estadia: "))
Vista_al_mar = input("Desea vista al mar) (si,no): ")


if Vista_al_mar == "si":
    total = Dias_estadia * 190.50
    print(f"Hola {Nombre_cliente} el total a pagar por los {Dias_estadia} días, es: {total}")
elif Vista_al_mar == "no":

    total = Dias_estadia * 150.50
    print(f"Hola {Nombre_cliente} el total a pagar por los {Dias_estadia} días, es: {total}")


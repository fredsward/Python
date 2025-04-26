


Destino = input("Ingrese el destino (nacional o internacional):")
Peso = int(input("Ingres el peso del paquete en kg:"))

if Destino == "nacional":
    total = Peso * 10
    print("El costo del envio es de: $", total)
elif Destino == "internacional":
    total = Peso * 20
    print("El costo del envio es de: $", total)
else:
    print("Destino no valido, por favor ingrese 'nacional' o 'internacional'")
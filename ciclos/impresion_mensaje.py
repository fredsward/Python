

print(" Repeticion de un mensaje")

mensaje = input("Escribe el mensaje a repetir: ")
numero_rep = int(input("Numero de repeticiones? "))

# Iterar sobre el rango de repeticiones

for i in range(numero_rep):
    print(f"{i+1}. {mensaje}")
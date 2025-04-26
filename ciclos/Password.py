

print("*** Validacion de password ***")

Password = "admin123"
salir = False

while not salir:

    Password2 = input("Password:")
    if Password2 == Password:
        print("Password válido")
        salir = True
    else:
        print("Password invalido, intente de nuevo")


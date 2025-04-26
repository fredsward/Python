

Usuario = "admin"
Password = 12345

user = input("Ingrese su usuario: ")
passwrd = int(input("Ingrese su contraseña: "))


if user == Usuario and passwrd == Password:
    print("Bienvenido al sistema")
elif user != Usuario and passwrd == Password:
    print("Usuario invalido")
elif user == Usuario and passwrd != Password:
    print("Contraseña incorrecta")
elif user != Usuario and passwrd != Password:
    print("Verifique usuario y contraseña")



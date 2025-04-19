#Inmutabilidad en cadenas

Cadena1 = "Hola Mundo"

#No se pueden modificar sus elementos solo crear uno nuevo
#Cadena1[0] = "Z"
Cadena2 = Cadena1
Cadena1 = "Hola como estas"
print(Cadena1)
print(Cadena2)

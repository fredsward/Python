#Subcadenas en python

Cadena1 = "Hola, Mundo!"

#Obtenemos la subcadena
subcadena_hola = Cadena1[6:11]
print(f'Subcadena {subcadena_hola}')

# Buscar y devolver subcadenas con find
posicion = Cadena1.find('Mundo')
print(f'Posicion: {posicion}')

#Reemplazar subcadenas

Cadena2 = "Cadena sin modificar"
nueva_cadena = Cadena2.replace("modificar", "soy el nuevo")#nuevo reemplaza a modificar
print(nueva_cadena)

# Separar subcadenas

datos = "Hola Mundo"
lista = datos.split() #Separa cada elemento
print(lista)

datos = "Juan, 30, Mexico"
lista = datos.split(',')
print(lista)

#Multiplicación de cadenas

texto = " Hola "
veces = 4

resultado = texto*veces
print(resultado)









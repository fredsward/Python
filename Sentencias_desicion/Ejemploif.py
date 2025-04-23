# Sentencia IF, ELSE Y ELSEIF

edad = 20
if edad >= 18:
	print(f'Eres mayor de edad. Tienes {edad} años')

elif 13 <= edad < 18:
	print("Eres un adolescente")

else:
	print("Eres un niño")

# Revisar si un numero es positivo

numero = int(input("Introduce un numero: "))

if numero > 0:
	print(f'El numero {numero} es positivo')
elif numero < 0:
	print(f'El numero {numero} es negativo')
else:
	print(f'El numero es cero')

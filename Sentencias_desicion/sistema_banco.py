# Sistema bancario

print("*** Sistema bancario ***")

salir_sistema_txt = input("Deseas salir del sistema? ")
salir_sistema = salir_sistema_txt.strip().lower() =='si'

if not salir_sistema:
	print(f'Continuas dentro del sistema')
else:
	print("Sales dentro del sistema")



# Casa de los espejos

edad = int(input("Introduce tu edad: "))
Miedo_txt = input("Tienes miedo a la oscuridad(SI,NO): ")
miedo = Miedo_txt.strip().lower() == 'si'

if not miedo and not edad >= 10:
	print("puedes pasar")

else:
	print("No puedes pasar")

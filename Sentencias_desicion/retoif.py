# Reto tienda linea



Gasto = int(input("Ingrese el gasto total: "))
Descuento = 0
Miembro_Tienda = input("Es miembro? (SI,NO) ")


if Gasto > 1000 and Miembro_Tienda.lower().strip() == 'si':
	Descuento = 10
	Pago = (Gasto * Descuento) / 100
	Gasto = Gasto - Pago
	print(f'El pago total es de: {Gasto}')

elif  Gasto < 1000 and Miembro_Tienda.lower().strip() == 'si':
	Descuento = 5
	Pago = (Gasto * Descuento) / 100
	Gasto = Gasto - Pago
	print(f' El pago total es de: {Gasto}')

else:
	print(f'El pago es de: {Gasto}')


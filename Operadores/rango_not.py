


# Revisar si una variable se encuentra dentro de un 1 a  10


dato = int(input("Proporciona un dato entero: "))


# Revisar si esta dentro del rango


#esta_dentro_rango = 1 <= dato <= 10

#print(f'Esta dentro del rango 1 a  10?: {esta_dentro_rango}')


# Logica inversa si el dato esta fuera de rango


esta_fuera_rango = not(1 <= dato <= 10)

print(f'esta fuera de rango ( entre 1 y 10?) {esta_fuera_rango}')



# Ejemplo de ticket de venta


print("*** Generacion de ticket de venta ***")

precio_leche = int(input("Precio leche: "))
precio_pan = int(input("Precio pan: "))

precio_lechuga = int(input('Precio lechuga: '))
precio_platanos = int(input("Precio platanos: "))


sub_total = precio_leche + precio_pan + precio_lechuga + precio_platanos


# Calculo con iva


impuesto = sub_total * 0.16

Descuento = int(input("Ingresa el descuento: "))

# Calculo total de la compra


costo_total = sub_total + impuesto

costo_descuento = costo_total * (Descuento/100)

costo_total = costo_total - costo_descuento

print(f'''

Subtotal : ${sub_total:.2f}

Impuesto: ${impuesto:.2f}

Total con descuento: ${costo_total:.2f}

''')


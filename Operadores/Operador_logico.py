
#Operador AND (Solo si ambos son verdaderos)

#condicion1 = True
#condicion2 = True
#resultado = condicion1 and condicion2
#print(f'Resultado: {resultado}')


# Ejemplo de AND
print("Sistema de descuentos VIP")

No_productos_descuento = 10
Cantidad_productos = int(input("Ingresa los articulos comprados:"))
Tiene_membresia = input("Tiene membresia (SI,NO?):")

es_elegible_descuento = (Cantidad_productos >= No_productos_descuento and Tiene_membresia.strip().lower() == "si")

print(f'Es elegible para el descuento: {es_elegible_descuento}')

# Ejemplo de OR
print("*** Ejemplo de OR ***")


Distancia_permitida_km = 3
Tiene_credencial = input("Tiene credencial (SI,NO?)")
Distancia_biblioteca_km = int(input("A cuantos km vives de la biblioteca?: "))

es_elegible_prestamo = (Tiene_credencial.strip().lower() == 'si' 
                        or Distancia_biblioteca_km <= Distancia_permitida_km)

print(f'es elegible para prestamo? {es_elegible_prestamo}')

# Operador NOT

condicion = False
resultado = not condicion
print(f'Operador NOT: {resultado}')

# Revisar si una variable es cadena vacia
nombre =''
es_cadena_vacia = not nombre
print(f'\nLa cadena no tiene ningun valor? {es_cadena_vacia}')



# Las tuplas son similares a las listas, pero no se pueden modificar una vez creadas.

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

# Iterar tupla
for elemento in mi_tupla:
    print(elemento)


# Crear tupla con cordenada

coordenadas = (3,5)

# Accedemmos a la tupla
print(f'Coordenada x: {coordenadas[0]}')
print(f'Coordenada y: {coordenadas[1]}')

# Tupla unitaria
tupla_un_elemento = 1,

#tupla anidada
tupla_anidada = (1,2,3, (4,5))
print(tupla_anidada[3])


# Desempaquetado de tuplas (unpacking)

producto = ('P001', 'Laptop', 1500.00)

#Desempaquetado
id,descripcion,precio = producto
print(f'ID: {id}')
print(F'Descripcipon: {descripcion}')
print(f'precio: {precio}')


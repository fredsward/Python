

print("Diccionarios en python")

# creamos el diccionario de persona con clave y valor

persona = {
    'nombre' : 'Sergio',
    'edad' : 30,
    'ciudad': 'Mexico'
}

print(f'Diccionario {persona}')

#Acceder a los elementos

print(f'Nombre:  {persona["nombre"]}')
print(f'Edad: {persona.get("edad")}')

# Modificar valor del diccionario

persona['edad'] = 35
print(f'Edad nueva: {persona.get("edad")}')

# Agregar nuevo elemento

persona['profesion'] = 'Ingeniero'
print(f'Diccionario nuevo:  {persona}')

#Eliminar un elemento
del persona['ciudad']
print(f'Diccionario nuevo:  {persona}')

# Otra forma
persona.pop('profesion')
print(f'Diccionario nuevo:  {persona}')

# Iterar elementos del diccionario
for llave, valor in persona.items():
    print(f'Llave: {llave}, valor: {valor}')


# Obtener los valores
for valor in persona.values():
    print(f' Valor: {valor}')

# Obtener las llaves
for llave in persona.keys():
    print(f'Llave {llave}')
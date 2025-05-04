

# Combinar listas con diccionarios

print("*** Listas con diccionarios ***")

personas = [
    {
        'nombre': 'Regina',
        'apellido': 'Flores',
        'edad': 21
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 24
    }
]

print(personas)

# Acceder al diccionario desde una lista

print(f'''
    Nombre: {personas[0].get("nombre")}
    Apellido: {personas[0].get("apellido")}
    Edad: {personas[0].get("edad")}
''')

# Recorrer elementos de la lista
print()
for contador, persona in enumerate(personas):
    print(f'Persona {contador}: {persona}')
    print(f'Detalle: Nombre: {persona.get("nombre")}, Apellido: {persona.get("apellido")}')
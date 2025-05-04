

print("*** Agenda contactos ***")

agenda = {

    'Carlos':{
        'telefono' : '55667711',
        'direccion' : 'Calle Principal 132',
        'email': 'carlos@gmail.com'
    },
    'Maria':{
        'telefono': '44541269',
        'direccion' : ' Calle Principal 154',
        'email': 'maria@gmail.com'
    },
    'Pedro': {
        'telefono': '123456789',
        'email' : 'pedro@gmail.com',
        'direccion': ' Avenida Principal 101'
    }

}

print(agenda)

# Acceder a la informacion de un contacto

print("Informacion de maria")
print(f'Telefono: {agenda["Maria"]["telefono"]}')
print(f'Telefono: {agenda["Maria"]["direccion"]}')
print(f'Telefono: {agenda["Maria"]["email"]}')

# Agregar nuevo contacto
agenda['Ana'] = {
    'telefono': '55678992',
    'email': 'ana@gmail.com',
    'direccion': 'Calle salvador'
}

print(agenda)

#Eliminar un contacto existente
agenda.pop('Pedro')

print(agenda)

# Mostrar los contactos de la agenda
print("\n")

for nombre, detalles in agenda.items():
    print(f'Nombre: {nombre}')
    print(f'Telefono: {detalles.get("telefono")}')
    print(f'detalles: {detalles.get("email")}')
    print(f'direccion: {detalles.get("direccion")}')
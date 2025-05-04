


print("*** Lista de suscriptores ***")

suscriptores = [
    "luisa@gmail.com",
    'marcos@gmail.com',
    "elena@gmail.com"
]

print(f'Suscriptores: {suscriptores}')

# Verificar si un nuevo suscriptor ya esta en la lista

nuevo_suscriptor = 'marcos@gmail.com'
if nuevo_suscriptor in suscriptores:
    print("Ya esta en la lista")
else:
    suscriptores.append(nuevo_suscriptor)
print(f'Suscriptores: { suscriptores}')

# Eliminar un suscriptor de la lista
suscriptor_eliminar = 'elena@gmail.com'
suscriptores.remove(suscriptor_eliminar)
print(f'Suscriptores: {suscriptores}')

# verificar cantidad de suscriptores
print(f'Cantidad de suscriptores: {len(suscriptores)}')

# Mostrar todos los suscriptores
for suscriptor in suscriptores:
    print(suscriptor)

print("*** Lista de suscriptores dinamica ***")

suscriptores1 = []

num_suscriptores = int(input(f'Ingrese el numero de suscriptores a agregar:'))

for i in range(num_suscriptores):
    suscriptor = input(f'Ingrese el correo del suscriptor {i+1}: ')
    if suscriptor in suscriptores1:
        print("Ya esta en la lista")
    else:
        suscriptores1.append(suscriptor)

print(f' Lista de suscriptores: {suscriptores1}')


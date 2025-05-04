

# Crear lista vacia
lista_reproduccion = []

numero_canciones = int(input("Cuantas canciones quieres agregar:"))

# iterar cada elemento de la lista para agregar un nuevo elemento

for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice + 1}')
    lista_reproduccion.append(cancion)

#Agregar canciones

# Ordenar lista en orden alfabetico
lista_reproduccion.sort()

#Mostrar lista de reproduccion
print(f'\n Lista en orden alfabetico: {lista_reproduccion}')

#Mostrar la lista iterando
for cancion in lista_reproduccion:
    print(f'Cancion: {cancion}')

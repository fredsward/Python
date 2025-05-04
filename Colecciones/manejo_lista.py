

print("Manejo de listas")

mi_lista = [1,2,3,4,5]

# Largo de lista
print(f'Largo de la lista: {len(mi_lista)}')

# Acceder a los elementos de la lista
print(f'Acceder al valor del indice 4: {mi_lista[4]}')


print("Modificar elementos de una lista")
mi_lista[1] = 10
print(mi_lista)

#Agregar nuevo elemento al final de la lista
mi_lista.append(6)
print(mi_lista)

# Agregar en un indice especifico
mi_lista.insert(2,15)
print(mi_lista)

# Eliminar un elemento de la lista
mi_lista.remove(15)
print(mi_lista)

# Remover con pop
mi_lista.pop(1)
print(mi_lista)

# Eliminar con del
del mi_lista[2]
print(mi_lista)

#Obtener sublista
sublista = mi_lista[1:3]
print(f'Sublista: {sublista}')

# Iterar listas

nombres = ['Juan', 'Pedro', 'Maria', 'Jose']
for nombre in nombres:
    print(f'Hola {nombre}')
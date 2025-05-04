

# Combinacion de listas y tuplas

# definir una lista que almacena tuplas de productos

productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.0),
    ('p003', 'Zapatos' , 50.0)
]

# Imprimir la informacion de cada producto y calcular el precio total

precio_total = 0

print("Informacion de los productos: ")

for producto in productos:
    codigo, nombre, precio = producto
    print(f'Codigo: {codigo}, Nombbre: {nombre}, Precio: {precio}')
    precio_total += precio # Accede al indice 2 de la tupla
    print(f'Precio total: {precio_total}')


# Sets en python 

print("Manejo de sets en python")

mi_set = {1,2,3,4,4,5}
print(f'Mi set: {mi_set}')

# Agregar elementos al set
mi_set.add(6)
mi_set.add(9)
print(f'Set modificado: {mi_set}')

# Eliminar elementos del set
mi_set.remove(9)
print(f'Set eliminado: {mi_set}')

# Iterar elementos del set
for elemento in mi_set:
    print(f'Elemento: {elemento}')

# Comprobar si existe un elemento en el set
print(f'El elemento 3 esta en el set: {3 in mi_set}')

# Longitud del set
print(len(mi_set))


print(" *** Operaciones con sets ***")

a = {1,2,3,4}
b = {3,4,7,8}

union = a | b # Union de sets
print(f'Union: {union}')

Interseccion = a & b # Interseccion de a y b
print(f'Interseccion: {Interseccion}')

Diferencia = a -b # Diferencia de a y b
print(f'Diferencia: {Diferencia}')
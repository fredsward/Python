

print("*** Sistema de inventarios ***")

inventario = []

numero_productos = int(input("Cuantos productos a agregar: "))

# Iterar

for indice in range(numero_productos):
    print(f"Proporciona los valores del producto {indice + 1}")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("cantidad: "))
    #Crear el diccionario con el detalle del producto

    producto = {"id": indice, "nombre": nombre, "precio" : precio, "cantidad": cantidad}
    #Agregar el producto al inventario
    inventario.append(producto)

    # Mostrar el inventario inicial
    print(f'\nInventario inicial: {inventario}')

# Buscar un producto por ID

id_buscar = int(input("\nIngresa el ID del producto a buscar: "))
producto_encontrado = None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print("Informacion encontrada: ")
    print(f''' Id: {producto_encontrado.get("id")}
        Nombre: {producto_encontrado.get("nombre")}
        Precio: {producto_encontrado.get("precio")}
        Cantidad: {producto_encontrado.get("cantidad")}''')
else:
    print("Producto no encontrado")

# Mostrar inventario detallado

print(f"\nInventario detallado ")
for producto in inventario:
    print(f'''Id: {producto.get("id")}
        Nombre: {producto.get("nombre")}
        Precio: {producto.get("precio")}
        Cantidad: {producto.get("cantidad")})
    ''')
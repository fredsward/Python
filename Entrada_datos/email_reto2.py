# Generador de email

Nombre = input("Ingresa el nombre: ")
Apellido = input("Ingresa los apellidos: ")
Empresa = input("Introduce la empresa: ")
Dominio = input("Introduce el dominio: ")

Nombre_limpio = Nombre.lower().strip()
Nombre_limpio = Nombre_limpio.replace(' ','.')

Apellido_limpio = Apellido.lower().strip()
Apellido_limpio = Apellido_limpio.replace(' ','.')

Empresa_limpio = Empresa.lower().strip()
Empresa_limpio = Empresa_limpio.replace(' ','.')

Dominio_limpio = Dominio.lower().strip()
Dominio_limpio = Dominio_limpio.replace(' ','.')

print(f'Correo generado: {Nombre_limpio}.{Apellido_limpio}@{Empresa_limpio}{Dominio_limpio}')
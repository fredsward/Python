

Usuario_autorizado = "admin"
Password_autorizado = 12345

Usuario = input("Ingrese su usuario:")
Pass = int(input("Ingrese su password:"))

Acceso = Usuario == Usuario_autorizado.strip().lower() == 'admin' and Pass == Password_autorizado

print(f'Acceso autorizado?: {Acceso}')

# Ejercicio de rango entre  0 y 5

Valor_minimo = 0
valor_maximo = 5
Valor_usuario = int(input("Introduce un valor entre 0 y 5: "))

esta_dentro_rango = Valor_minimo <= Valor_usuario <= valor_maximo
print(f'Valor dentro de rango? {esta_dentro_rango}')

# Calculo de area y perimetro de un rectangulo

base = int(input("Introduce la base del rectangulo: "))
altura = int(input("Introduce la altura del rectangulo: "))

area = base * altura
perimetro = (base * altura) / 2
print(f'La base es: { area}')
print(f'La altura es: {perimetro}')


#Operadores aritmeticos

a = 10
b = 3

# Suma de valores
suma = a + b 
print(f'Suma: {suma}')

resta = a - b
print(f'Resta: {resta}')

multiplicacion = a * b 
print(f'Multiplicación: {multiplicacion}')

division = a / b 
print(f'División: {division:.2f}')

# Modulo (Residuo de la división)
modulo = a % b
print(f'Módulo: {modulo}')

# Potencia (Exponenciación)
potencia = a ** b    #10 elevado a 3 = 10*10*10 = 1000
print(f'Potencia: {potencia}')

# Operadores de asignación
print("*** Operadores de asignación ***")
numero = 5
print(f'Número: {numero}')
numero = 10
print(f'Número: {numero}')
cadena = "Saludos desde python"
print(f'Cadena: {cadena}')  

# Operadores de asignacion multiple

a ,b , c = 10, "Hola", 3.14
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')

#Asignacion encadenada  
a = b = c = 10
print(f'a: {a}, b: {b}, c: {c}')

#Asignacion multiple 
x, y = 5, 10
print(f'Valor inicial de x: {x}, Valor inicial de y: {y}')
# Aplicando el concepto de asignacion multiple, cambiamos valores
x , y = y, x
print(f'x: {x}, y: {y}') # x=10, y=5

# Recibir multiples valores de la entrada del usuario

nombre, apellido = input("Ingresa tu nombre y apellido separados por coma: ").split(",")
print(f'Nombre: {nombre.strip()}')
print(f'Apellido: {apellido.strip()}')
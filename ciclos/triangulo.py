

print("*** Dibujar un triangulo ***")

numero_filas = int(input("Numero de filas?: "))

# Iterar sobre cada fila del triangulo
for fila in range(1, numero_filas + 1):
    espacios_blancos = ' ' * (numero_filas - fila)
    asteriscos = '*' * (2 * fila - 1)
    print(f'{espacios_blancos}{asteriscos}')

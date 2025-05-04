

# Promedio de calificaciones 

# Lista vacia
calificaciones = []

# Pedir alumnos a calificar
numero_alumnos = int(input("Cuantoas alumnos quieres calificar: "))

for indice in range(numero_alumnos):
    calificacion = int(input(f'Calificación del alumno {indice + 1}:'))
    calificaciones.append(calificacion)

# Calcular promedio

promedio = sum(calificaciones) / len(calificaciones)
print(
    "El promedio es: " , promedio
)

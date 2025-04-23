# Operador ternario

edad = 18
es_adulto="Sí" if edad >= 18 else "No"
print(es_adulto)


# Salud y fitness

META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04

Nombre = input("Introduce tu nombre: ")
pasos = int(input("Introduce los pasos caminados: "))

# verificar si alcanzo la meta de pasos diarios

meta_alcanzada = pasos >= META_PASOS_DIARIO
meta_alcanzada_txt = 'Sí' if meta_alcanzada else 'No'
#Mostrar las calorias quemadas
calorias_quemadas = pasos * CALORIAS_POR_PASO
#Mostrar la info

print(f'Usuario: {Nombre}')
print(f'Pasos dados hoy: {pasos}')
print(f'Calorias quemadas {calorias_quemadas}')
print(f'Meta alcanzada? {meta_alcanzada_txt}')
print(f'Meta de pasos diario es de: {META_PASOS_DIARIO}')

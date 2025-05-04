

print(" Comprension de listas")

# Lista para generar el cuadrado de cada numero

numeros = [1,2,3,4,5]
cuadrados = [x**2 for x in numeros ]

print(cuadrados)

# Lista de numeros pares
numeros = range(10+1)
pares = [x for x in numeros if x % 2 == 0]
print(pares)
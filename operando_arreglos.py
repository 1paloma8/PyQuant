import random  # Importamos la librería para generar números aleatorios

# Paso 1: Pedir el número de elementos al usuario
n = int(input("Ingrese la cantidad de elementos para cada arreglo: "))

# Paso 2: Llenar los arreglos con números aleatorios
arreglo1 = []
arreglo2 = []

for i in range(n):
    arreglo1.append(random.randint(1, 100))  # Números aleatorios entre 1 y 100
    arreglo2.append(random.randint(1, 100))

# Mostrar los arreglos generados
print("\nArreglo 1:", arreglo1)
print("Arreglo 2:", arreglo2)

# Paso 3: Calcular la suma de cada arreglo
suma1 = 0
suma2 = 0

for num in arreglo1:
    suma1 += num

for num in arreglo2:
    suma2 += num

# Determinar cuál tiene la suma más alta
if suma1 > suma2:
    print("\nEl Arreglo 1 tiene la suma más alta:", suma1)
elif suma2 > suma1:
    print("\nEl Arreglo 2 tiene la suma más alta:", suma2)
else:
    print("\nAmbos arreglos tienen la misma suma:", suma1)

# Paso 4: Encontrar el número mayor y menor en cada arreglo
mayor1 = arreglo1[0]
menor1 = arreglo1[0]

for num in arreglo1:
    if num > mayor1:
        mayor1 = num
    if num < menor1:
        menor1 = num

mayor2 = arreglo2[0]
menor2 = arreglo2[0]

for num in arreglo2:
    if num > mayor2:
        mayor2 = num
    if num < menor2:
        menor2 = num

# Comparar números mayores
if mayor1 > mayor2:
    print("\nEl número mayor está en el Arreglo 1:", mayor1)
elif mayor2 > mayor1:
    print("\nEl número mayor está en el Arreglo 2:", mayor2)
else:
    print("\nAmbos arreglos tienen el mismo número mayor:", mayor1)

# Comparar números menores
if menor1 < menor2:
    print("\nEl número menor está en el Arreglo 1:", menor1)
elif menor2 < menor1:
    print("\nEl número menor está en el Arreglo 2:", menor2)
else:
    print("\nAmbos arreglos tienen el mismo número menor:", menor1)

# Paso 5: Calcular el promedio conjunto y de cada arreglo
promedio1 = suma1 / n
promedio2 = suma2 / n
promedio_conjunto = (suma1 + suma2) / (2 * n)

print("\nEl promedio conjunto de los dos arreglos es:", promedio_conjunto)

# Comparar promedios individuales con el promedio conjunto
if promedio1 > promedio_conjunto:
    print("El promedio del Arreglo 1 está por encima del promedio conjunto.")
else:
    print("El promedio del Arreglo 1 está por debajo o igual al promedio conjunto.")

if promedio2 > promedio_conjunto:
    print("El promedio del Arreglo 2 está por encima del promedio conjunto.")
else:
    print("El promedio del Arreglo 2 está por debajo o igual al promedio conjunto.")

# Paso 6: Contar la cantidad de pares e impares en cada arreglo
pares1 = 0
pares2 = 0
impares1 = 0
impares2 = 0

for num in arreglo1:
    if num % 2 == 0:
        pares1 += 1
    else:
        impares1 += 1

for num in arreglo2:
    if num % 2 == 0:
        pares2 += 1
    else:
        impares2 += 1

# Comparar cantidad de pares e impares
if pares1 > pares2:
    print("\nEl Arreglo 1 tiene más números pares.")
elif pares2 > pares1:
    print("\nEl Arreglo 2 tiene más números pares.")
else:
    print("\nAmbos arreglos tienen la misma cantidad de números pares.")

if impares1 > impares2:
    print("El Arreglo 1 tiene más números impares.")
elif impares2 > impares1:
    print("El Arreglo 2 tiene más números impares.")
else:
    print("Ambos arreglos tienen la misma cantidad de números impares.")
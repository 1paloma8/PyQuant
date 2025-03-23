import csv

# Diccionario para guardar la cantidad de personas por ciudad
ciudades= {}

# Abrir el archivo CSV
with open("C:\\Users\\yuliee\\Downloads\\trabajo grupo\\colexterior.csv", mode='r', encoding="utf-8") as file:

    reader = csv.DictReader(file)
    
    for row in reader:
        ciudad = row['Ciudad de Residencia']
        
        # Si la ciudad ya está en el diccionario, aumentamos su contador en 1
        if ciudad in ciudades:
            ciudades[ciudad] += 1
        # Si la ciudad no está en el diccionario, la agregamos con un valor inicial de 1
        else:
           ciudades[ciudad] = 1

# Imprimir resultados
for ciudad, cantidad in ciudades.items():
    print(f"Ciudad: {ciudad}, Cantidad: {cantidad}")
    print("="*90)
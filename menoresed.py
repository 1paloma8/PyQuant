import csv

# Diccionario para guardar la cantidad de menores de edad por país
menores_por_pais = {}

# Abrir el archivo CSV usando la ruta proporcionada
with open("C:\\Users\\yuliee\\Downloads\\trabajo grupo\\colexterior.csv", mode='r', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Obtener la edad y el país de la fila actual
        edad = int(row['Edad (años)'])
        pais = row['País']
        
        # Verificar si la persona es menor de edad (menor a 18 años)
        if edad < 18:
            # Si el país ya está en el diccionario, aumentamos su contador en 1
            if pais in menores_por_pais:
                menores_por_pais[pais] += 1
            # Si el país no está en el diccionario, lo agregamos con un valor inicial de 1
            else:
                menores_por_pais[pais] = 1

# Imprimir resultados
print("===== Menores de edad por país =====")
for pais, cantidad in menores_por_pais.items():
    print(f"País: {pais}, Menores de edad: {cantidad}")
import csv

# Diccionario para guardar la cantidad de personas sin documentos válidos por país
sin_documentos_por_pais = {}

# Abrir el archivo CSV usando la ruta proporcionada
with open("C:\\Users\\yuliee\\Downloads\\trabajo grupo\\colexterior.csv", mode='r', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Obtener el país y el estado de los documentos (suponiendo que "Nivel Académico" indica la validez)
        pais = row['País']
        documentos = row['Nivel Académico']  # Cambia esto si usas otra columna
        
        # Verificar si la persona no tiene documentos válidos (ejemplo: "NO INDICA")
        if documentos == "NO INDICA":  # Ajusta este valor según tu archivo CSV
            # Si el país ya está en el diccionario, aumentamos su contador en 1
            if pais in sin_documentos_por_pais:
                sin_documentos_por_pais[pais] += 1
            # Si el país no está en el diccionario, lo agregamos con un valor inicial de 1
            else:
                sin_documentos_por_pais[pais] = 1

# Imprimir resultados
print("===== Personas sin documentos válidos por país =====")
for pais, cantidad in sin_documentos_por_pais.items():
    print(f"País: {pais}, Personas sin documentos válidos: {cantidad}")
import csv

# Creamos un diccionario vacío para guardar la cantidad de profesionales por país
profesionales_por_pais = {}

# Abrimos el archivo CSV en modo lectura
with open("C:\\Users\\yuliee\\Downloads\\trabajo grupo\\colexterior.csv", mode='r', encoding="utf-8") as file:

    # Usamos csv.DictReader para leer el archivo como un diccionario
    reader = csv.DictReader(file)
    
    # Recorremos cada fila del archivo
    for row in reader:
        # Obtenemos el país y el nivel académico de la fila actual
        pais = row['País']
        nivel_academico = row['Nivel Académico']
        
        # Verificamos si el nivel académico indica que es un profesional
        if nivel_academico in ["PREGRADO - PROFESIONAL", "POSTGRADO - MAESTRIA", "POSTGRADO - DOCTORADO"]:
            # Si el país ya está en el diccionario, aumentamos su contador en 1
            if pais in profesionales_por_pais:
                profesionales_por_pais[pais] += 1
            # Si el país no está en el diccionario, lo agregamos con un valor inicial de 1
            else:
                profesionales_por_pais[pais] = 1

# Finalmente, imprimimos los resultados
for pais, cantidad in profesionales_por_pais.items():
    print(f"País {pais}: {cantidad} profesionales")
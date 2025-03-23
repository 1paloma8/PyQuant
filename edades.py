import csv

# Creamos un diccionario vacío para guardar la cantidad de personas por rango de edad
emigrantes_por_edad = {
    "0-18": 0,
    "19-30": 0,
    "31-50": 0,
    "60+": 0
}

# Abrimos el archivo CSV en modo lectura
with open("C:\\Users\\yuliee\\Downloads\\trabajo grupo\\colexterior.csv", mode='r', encoding="utf-8") as file:

    # Usamos csv.DictReader para leer el archivo como un diccionario
    reader = csv.DictReader(file)
    
    # Recorremos cada fila del archivo
    for row in reader:
        # Obtenemos la edad de la fila actual
        edad = int(row['Edad (años)'])  # Convertimos la edad a entero
        
        # Agrupamos la edad en los rangos correspondientes
        if edad <= 18:
            emigrantes_por_edad["0-18"] += 1
        elif 19 <= edad <= 30:
            emigrantes_por_edad["19-30"] += 1
        elif 31 <= edad <= 50:
            emigrantes_por_edad["31-50"] += 1
        else:
            emigrantes_por_edad["60+"] += 1

# Finalmente, imprimimos los resultados
for rango, cantidad in emigrantes_por_edad.items():
    print(f"edades  entre un rangode :{rango}: {cantidad} personas")
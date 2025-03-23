import csv

# Creamos un diccionario vacío para guardar la relación género - área de conocimiento
relacion_genero_area = {}

# Abrimos el archivo CSV en modo lectura
with open("C:\\Users\\yuliee\\Downloads\\trabajo grupo\\colexterior.csv", mode='r', encoding="utf-8") as file:

    # Usamos csv.DictReader para leer el archivo como un diccionario
    reader = csv.DictReader(file)
    
    # Recorremos cada fila del archivo
    for row in reader:
        # Obtenemos el género y el área de conocimiento de la fila actual
        genero = row['Género']
        area_conocimiento = row['Área Conocimiento']
        
        # Si el área de conocimiento no está en el diccionario, la agregamos
        if area_conocimiento not in relacion_genero_area:
            relacion_genero_area[area_conocimiento] = {"MASCULINO": 0, "FEMENINO": 0, "otro": 0}
        
        # Incrementamos el contador correspondiente al género en el área de conocimiento
        if genero in relacion_genero_area[area_conocimiento]:
            relacion_genero_area[area_conocimiento][genero] += 1
        else:
            relacion_genero_area[area_conocimiento]["otro"] += 1

# Finalmente, imprimimos los resultados
for area, count in relacion_genero_area.items():
    print("-" * 90)
    print(f"Área de conocimiento: {area}")
    print(f"  Masculino: {count['MASCULINO']}")
    print(f"  Femenino: {count['FEMENINO']}")
    print(f"  Desconocido: {count['otro']}")
    print("-" * 90)
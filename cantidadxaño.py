import csv

# Creamos un diccionario vacío para guardar la cantidad de personas por año
personas_por_año = {}

# Abrimos el archivo CSV en modo lectura
with open("C:\\Users\\yuliee\\Downloads\\trabajo grupo\\colexterior.csv", mode='r', encoding="utf-8") as file:
    # Usamos csv.DictReader para leer el archivo como un diccionario
    reader = csv.DictReader(file)
    
    # Recorremos cada fila del archivo
    for row in reader:
        # Obtenemos el año de registro de la fila actual
        fecha_registro = row['Fecha de Registro']  # Ejemplo: "2023-09"
        año = fecha_registro[:4]  # Extraemos los primeros 4 caracteres (el año)
        
        # Si el año ya está en el diccionario, aumentamos su contador en 1
        if año in personas_por_año:
            personas_por_año[año] += 1
        # Si el año no está en el diccionario, lo agregamos con un valor inicial de 1
        else:
            personas_por_año[año] = 1

# Finalmente, imprimimos los resultados
for año, cantidad in personas_por_año.items():
    print(f"Año {año}: {cantidad} personas registradas")
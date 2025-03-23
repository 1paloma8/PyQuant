import csv

# Diccionario para guardar el estado civil de colombianos por país
estado_civil_por_pais = {}

# Abrir el archivo CSV usando la ruta proporcionada
with open("C:\\Users\\yuliee\\Downloads\\trabajo grupo\\colexterior.csv", mode='r', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Verificar si la persona es colombiana
        if 'COLOMBIA' in row['Ciudad de Nacimiento']:
            pais = row['País']
            estado_civil = row['Estado civil']
            
            # Inicializar el país si no existe
            if pais not in estado_civil_por_pais:
                estado_civil_por_pais[pais] = {}
            
            # Contar el estado civil en el país correspondiente
            if estado_civil in estado_civil_por_pais[pais]:
                estado_civil_por_pais[pais][estado_civil] += 1
            else:
                estado_civil_por_pais[pais][estado_civil] = 1

# Imprimir resultados
for pais, estados in estado_civil_por_pais.items():
    print(f"País: {pais}")
    for estado, cantidad in estados.items():
        print(f"  Estado civil: {estado}, Cantidad: {cantidad}")
    print("*" * 30)
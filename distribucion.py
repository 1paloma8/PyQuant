
import csv
oficinas_registro = {}
with open("C:\\Users\\yuliee\\Downloads\\trabajo grupo\\colexterior.csv", mode='r', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        oficina = row['Oficina de registro']
        oficinas_registro[oficina] = oficinas_registro.get(oficina, 0) + 1
for oficina, cantidad in oficinas_registro.items():
    print(f"Oficina: {oficina}, Cantidad: {cantidad}")
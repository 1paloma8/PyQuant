def es_numero_perfecto(numero):
    """
    Verifica si un número es perfecto.
    """
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son perfectos

    suma_divisores = 0  # Inicializa la suma de los divisores

    for i in range(1, numero):  # Itera sobre los números del 1 al número - 1
        if numero % i == 0:  # Verifica si 'i' es divisor de 'numero'
            suma_divisores += i  # Suma el divisor a la suma total

    return suma_divisores == numero  # Retorna True si la suma de los divisores es igual al número

def numeros_perfectos_entre_1_y_1000():
    """
    Encuentra y muestra los números perfectos entre 1 y 1000.
    """
    perfectos = []  # Lista para almacenar los números perfectos

    for num in range(1, 1001):  # Itera sobre los números del 1 al 1000
        if es_numero_perfecto(num):  # Verifica si el número es perfecto
            perfectos.append(num)  # Añade el número perfecto a la lista

    print("Números perfectos entre 1 y 1000:")
    print(perfectos)  # Imprime la lista de números perfectos
    print(f"Cantidad de números perfectos encontrados: {len(perfectos)}")  # Imprime la cantidad de números perfectos

numeros_perfectos_entre_1_y_1000()  # Llama a la función para ejecutar el programa

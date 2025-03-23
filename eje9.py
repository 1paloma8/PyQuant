Desarrollo
def es_primo(numero):
    """
    Verifica si un número es primo.
    """
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    for i in range(2, int(numero**0.5) + 1):  # Verifica divisores hasta la raíz cuadrada del número
        if numero % i == 0:
            return False  # Si es divisible por algún número, no es primo
    return True  # Si no es divisible por ningún número, es primo

def numeros_primos_entre_1_y_1000():
    """
    Encuentra y cuenta los números primos entre 1 y 1000.
    """
    primos = []  # Lista para almacenar los números primos encontrados
    for num in range(2, 1001):  # Itera sobre los números del 2 al 1000
        if es_primo(num):  # Verifica si el número es primo
            primos.append(num)  # Agrega el número primo a la lista

    print("Números primos entre 1 y 1000:")
    print(primos)  # Imprime la lista de números primos
    print(f"Cantidad de números primos encontrados: {len(primos)}")  # Imprime la cantidad de números primos
numeros_primos_entre_1_y_1000()  # Llama a la función para ejecutar el programa

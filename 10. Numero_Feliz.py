def es_numero_feliz(n):
    def calcular_suma_cuadrados_digitos(numero):
        return sum(int(digit) ** 2 for digit in str(numero))

    historial = set()
    while n != 1 and n not in historial:
        historial.add(n)
        n = calcular_suma_cuadrados_digitos(n)

    return n == 1

while True:
    try:
        # Obtener el número desde el usuario
        numero = int(input("Ingrese un número entero positivo: "))

        # Verificar si el número es positivo
        if numero > 0:
            if es_numero_feliz(numero):
                print(f"{numero} es un número feliz.")
            else:
                print(f"{numero} no es un número feliz.")
            break  # Salir del bucle si se ingresó un número válido
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

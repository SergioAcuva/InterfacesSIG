def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

while True:
    try:
        # Intentar obtener un número entero positivo desde el usuario
        numero = int(input("Ingrese un número entero positivo: "))
        
        # Verificar si el número es positivo
        if numero >= 0:
            resultado_factorial = calcular_factorial(numero)
            print(f"El factorial de {numero} es: {resultado_factorial}")
            break  # Salir del bucle si se ingresó un número válido
        else:
            print("Por favor, ingrese un número entero no negativo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

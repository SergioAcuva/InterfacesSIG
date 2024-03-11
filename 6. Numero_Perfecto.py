def es_numero_perfecto(n):
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

while True:
    try:
        # Intentar obtener un número entero positivo desde el usuario
        numero = int(input("Ingrese un número entero positivo: "))
        
        # Verificar si el número es positivo
        if numero > 0:
            if es_numero_perfecto(numero):
                print(f"{numero} es un número perfecto.")
            else:
                print(f"{numero} no es un número perfecto.")
            break  # Salir del bucle si se ingresó un número válido
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

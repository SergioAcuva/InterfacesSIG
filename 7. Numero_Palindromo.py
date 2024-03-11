def es_palindromo(n):
    # Convertir el número a una cadena para facilitar la comparación
    numero_str = str(n)
    
    # Comparar el número con su reverso
    return numero_str == numero_str[::-1]

while True:
    try:
        # Intentar obtener un número entero positivo desde el usuario
        numero = int(input("Ingrese un número entero positivo: "))
        
        # Verificar si el número es positivo
        if numero >= 0:
            if es_palindromo(numero):
                print(f"{numero} es un número palíndromo.")
            else:
                print(f"{numero} no es un número palíndromo.")
            break  # Salir del bucle si se ingresó un número válido
        else:
            print("Por favor, ingrese un número entero no negativo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

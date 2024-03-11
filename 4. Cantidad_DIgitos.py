def contar_digitos(n):
    numero_str = str(n)
    cantidad_digitos = len(numero_str)
    return cantidad_digitos

while True:
    try:
        # Intentar obtener un número entero positivo desde el usuario
        numero = int(input("Ingrese un número entero positivo: "))
        
        # Verificar si el número es positivo
        if numero > 0:
            resultado = contar_digitos(numero)
            print(f"El número {numero} tiene {resultado} dígitos.")
            break  # Salir del bucle si se ingresó un número válido
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

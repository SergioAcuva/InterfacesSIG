def decimal_a_binario(n):
    if n == 0:
        return "0b0"
    else:
        binario = bin(n)
        return binario

while True:
    try:
        # Obtener el número decimal desde el usuario
        decimal = int(input("Ingrese un número decimal positivo: "))
        
        # Verificar si el número es positivo
        if decimal >= 0:
            resultado_binario = decimal_a_binario(decimal)
            print(f"La representación binaria de {decimal} es: {resultado_binario}")
            break  # Salir del bucle si se ingresó un número válido
        else:
            print("Por favor, ingrese un número decimal no negativo.")
    except ValueError:
        print("Por favor, ingrese un número decimal válido.")

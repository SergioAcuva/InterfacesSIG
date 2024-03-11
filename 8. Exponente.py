def calcular_potencia(base, exponente):
    # Verificar que ambos números sean enteros positivos
    if isinstance(base, int) and isinstance(exponente, int) and base >= 0 and exponente >= 0:
        return base ** exponente
    else:
        raise ValueError("Ambos valores deben ser números enteros positivos.")

while True:
    try:
        # Obtener la base y el exponente desde el usuario
        base = int(input("Ingrese la base (número entero positivo): "))
        exponente = int(input("Ingrese el exponente (número entero positivo): "))
        
        # Calcular la potencia y mostrar el resultado
        resultado_potencia = calcular_potencia(base, exponente)
        print(f"{base}^{exponente} = {resultado_potencia}")
        break  # Salir del bucle si se ingresaron valores válidos
    except ValueError as e:
        print(f"Error: {e}")

def es_primo(numero):
  """
  Esta función comprueba si un número es primo.

  Parámetros:
    numero: El número que se desea comprobar.

  Devuelve:
    True si el número es primo, False si no lo es.
  """

  if numero <= 1:
    return False

  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False

  return True

while True:
  try:
    numero = int(input("Introduzca un número entero positivo: "))
    if numero <= 0:
      raise ValueError
    break
  except ValueError:
    print("El número debe ser un entero positivo.")

if es_primo(numero):
  print(f"El número {numero} es primo")
else:
  print(f"El número {numero} no es primo")


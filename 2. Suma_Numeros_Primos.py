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


def suma_primos(n):
  """
  Esta función calcula la suma de los números primos hasta un número dado.

  Parámetros:
    n: El número límite hasta el que se suman los números primos.

  Devuelve:
    La suma de todos los números primos desde 2 hasta n.
  """
  suma = 0
  for i in range(2, n + 1):
    if es_primo(i):
      suma += i

  return suma
n = numero
suma_primos = suma_primos(n)
print(f"La suma de los números primos hasta {n} es {suma_primos}")

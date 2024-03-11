def convertir_dias(dias):
  """
  Esta función convierte un número de días en años, meses, semanas y días.

  Parámetros:
    dias: El número de días que se desea convertir.

  Devuelve:
    Un diccionario con la equivalencia en años, meses, semanas y días.
  """

  años = dias // 365
  dias_restantes = dias % 365

  meses = dias_restantes // 30
  dias_restantes %= 30

  semanas = dias_restantes // 7
  dias_restantes %= 7

  return {
    "años": años,
    "meses": meses,
    "semanas": semanas,
    "días": dias_restantes
  }

while True:
  try:
    numero = int(input("Introduzca un número entero positivo: "))
    if numero <= 0:
      raise ValueError
    break
  except ValueError:
    print("El número debe ser un entero positivo.")

equivalencia = convertir_dias(numero)

print(f"{numero} días equivalen a:")
for unidad, cantidad in equivalencia.items():
  print(f"  * {cantidad} {unidad}")

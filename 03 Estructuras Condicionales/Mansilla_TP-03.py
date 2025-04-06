# Se limpia la consola cada vez que se inicia el programa.
import os
os.system("cls" if os.name == "nt" else "clear")

"""
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""
print("Ejercicio 1\n")

age = int(input("¿Cuántos años tienes? "))
if age >= 18:
  print("Es mayor de edad")

"""
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”. 
"""
print("\nEjercicio 2\n")

grade = float(input("¿Cuál es tu nota? "))
if grade >= 6:
  print("Aprobado")
else:
  print("Desaprobado")

"""
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
operador de módulo (%) en Python para evaluar si un número es par o impar. 
"""
print("\nEjercicio 3\n")

number = int(input("Ingrese un número: "))
if number % 2 == 0:
  print("Ha ingresado un número par")
else:
  print("Por favor, ingrese un número par")

"""
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años."
"""
print("\nEjercicio 4\n")

user_age = int(input("¿Cuántos años tienes? "))
if user_age < 12:
  print("Niño/a")
elif user_age >= 12 and user_age < 18:
  print("Adolescente")
elif user_age >= 18 and user_age < 30:
  print("Adulto/a joven")
else:
  print("Adulto/a")

"""
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string.
"""
print("\nEjercicio 5\n")

password = input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: ")
if len(password) >= 8 and len(password) <= 14:
  print("Ha ingresado una contraseña correcta")
else:
  "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"

"""
6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
la mediana es menor que la moda.
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
"""
print("\nEjercicio 6\n")

import random
import statistics

# Generar una lista de 50 números aleatorios entre 1 y 100
random_numbers = [random.randint(1,100) for i in range(50)]

# Calculo de moda, mediana y media
mode = float(statistics.mode(random_numbers))
median = statistics.median(random_numbers)
mean = statistics.mean(random_numbers)

print(f"De la lista de números:\n{random_numbers}\n")
print(f"Moda: {mode}")
print(f"Mediana: {median}")
print(f"Media: {mean}")

if mode == median == mean:
  print("No hay sesgo")
elif mean > median and median > mode:
  print("El sesgo es positivo o a la derecha")
elif mean < median and median < mode:
  print("El sesgo es negativo o a la izquierda")
else:
  print("No hay un sesgo definido")

"""
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla.
"""
print("\nEjercicio 7\n")

phrase = input("Escribe una frase: ")
last_character = phrase[len(phrase)-1]
if last_character.lower() == "a":
  print(phrase + "!")
elif last_character.lower() == "e":
  print(phrase + "!")
elif last_character.lower() == "i":
  print(phrase + "!")
elif last_character.lower() == "o":
  print(phrase + "!")
elif last_character.lower() == "u":
  print(phrase + "!")
else:
  print(phrase)

"""
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
"""
print("\nEjercicio 8\n")

user_name = input("¿Cual es tu nombre? ")
option = input("""Ingrese:
1. Si quiere su nombre en mayúsculas
2. Si quiere su nombre en minúsculas.
3. Si quiere su nombre con la primera letra mayúscula.\n""")

if option == "1":
  print(f"Su nombre es {user_name.upper()}")
elif option == "2":
  print(f"Su nombre es {user_name.lower()}")
elif option == "3":
  print(f"Su nombre es {user_name.title()}")
else:
  print("La opción ingresada no es correcta")

"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""
print("\nEjercicio 9\n")

magnitude = float(input("Ingrese la magnitud del terremoto: "))

if magnitude < 3:
    description = "Muy leve (imperceptible)."
elif magnitude < 4:
    description = "Leve (ligeramente perceptible)."
elif magnitude < 5:
    description = "Moderado (sentido por personas, pero generalmente no causa daños)."
elif magnitude < 6:
    description = "Fuerte (puede causar daños en estructuras débiles)."
elif magnitude < 7:
    description = "Muy fuerte (puede causar daños significativos)."
else:
    description = "Extremo (puede causar graves daños a gran escala)."

print(f"De acuerdo con la escala de Richter, el terremoto es: {description}")

"""
10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano.
"""
print("\nEjercicio 10\n")

hemisphere = input("¿En cuál hemisferio te encuentras (Norte o Sur)? ").lower()
month = input("¿Que mes es? ").lower()
day = int(input("¿Que dia es? "))
season = False

# Se comprueban si los datos son correctos
if hemisphere == "norte" or hemisphere == "sur":
  if month == "febrero":
    if day >= 1 and day <= 29:
      print("Los datos son correctos!")
    else:
      print("El dia ingresado no es correcto ")
      day = False
  elif month == "abril" or month == "junio" or month == "septiembre" or month == "noviembre":
    if day >= 1 and day <= 30:
      print("Los datos son correctos!")
    else:
      print("El dia ingresado no es correcto ")
      day = False
  elif month == "enero" or month == "marzo" or month == "mayo" or month == "julio" or month == "agosto" or month == "octubre" or month == "diciembre":
    if day >= 1 and day <= 31:
      print("Los datos son correctos!")
    else:
      print("El dia ingresado no es correcto ")
      day = False
  else:
    print("El mes ingresado no es correcto")
    month = False
else:
  print("El hemisferio ingresado no es correcto")
  hemisphere = False

# Se define una bandera en True si todos los datos son correctos. Caso contrario es False
if hemisphere and month and day:
  flag = True
else:
  flag = False

# Si los datos son correctos
if flag:
  if month == "enero" or month == "febrero":
    if hemisphere == "norte":
      season = "Invierno"
    else:
      season = "Verano"
  
  elif month == "marzo":
    if day <= 20:
      if hemisphere == "norte":
        season = "Invierno"
      else:
        season = "Verano"
    else:
      if hemisphere == "norte":
        season = "Primavera"
      else:
        season = "Otoño"
  
  elif month == "abril" or month == "mayo":
    if hemisphere == "norte":
      season = "Primavera" 
    else:
      season = "Otoño"
  
  elif month == "junio":
    if day <= 20:
      if hemisphere == "norte":
        season = "Primavera"
      else:
        season = "Otoño"
    else:
      if hemisphere == "norte":
        season = "Verano"
      else:
        season = "Invierno"
  
  elif month == "julio" or month == "agosto":
    if hemisphere == "norte":
      season = "Verano"
    else:
      season = "Invierno"
  
  elif month == "septiembre":
    if day <= 20:
      if hemisphere == "norte":
        season = "Verano"
      else:
        season = "Invierno"
    else:
      if hemisphere == "norte":
        season = "Otoño"
      else:
        season = "Primavera"
  
  elif month == "octubre" or month == "noviembre":
    if hemisphere == "norte":
      season = "Otoño"
    else:
      season = "Primavera"
  
  elif month == "diciembre":
    if day <= 20:
      if hemisphere == "norte":
        season = "Otoño"
      else:
        season = "Primavera"
    else:
      if hemisphere == "norte":
        season = "Invierno"
      else:
        season = "Verano"
  
  else:
    print("No se pudo determinar la estación!")

  print(f"Para la fecha {day} de {month} y siendo el hemisferio {hemisphere} la estación es {season}")

else:
  print("No se pudo determinar la estación!")
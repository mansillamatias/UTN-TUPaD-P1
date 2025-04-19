# Importación de librerias a utilizar
import random, os, time

############################################# EJERCICIO 1 ##############################################
print("""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.""")

for i in range(101):
  print(i)

# Colocamos un temporizador de tres segundos para poder ver el resultado
time.sleep(1)

# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 2 ##############################################

print("""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.""")

number = input("Ingresa un número: ")
count = 0

for i in number:
  count += 1

print(f"El {number} tiene {count} digitos")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 3 ##############################################

print("""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.""")

number_1 = int(input("Introduce el primer número: "))
number_2 = int(input("Introduce el segundo número: "))

# Nos Aseguramos de que el valor menor esté primero
smallest_number = min(number_1, number_2)
highest_number = max(number_1, number_2)

# Inicializamos la variable para almacenar la suma
summation = smallest_number + 1

# Usamos un bucle for para sumar los números entre los valores dados
for number in range(smallest_number + 1, highest_number - 1):
    print(summation, "+", (number + 1), "=", end=" ")
    summation += (number + 1)
    print(summation, end=" " "\n")

# Mostrar el resultado
print(f"La suma de los números entre {number_1} y {number_2} sin incluir estos es: {summation}")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 4 ##############################################

print("""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.""")

number = int(input("Ingrese un número (0 para terminar): "))
summation = 0

while number != 0:
  print(summation, "+", (number), "=", end=" ")
  summation += number
  print(summation, end=" " "\n")
  number = int(input("Ingrese un número (0 para terminar): "))

print("La suma total es de: ", summation)

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 5 ##############################################

print("""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.""")

random_number = random.randint(0,9)
print("\nSe ha generado un número aleatorio entre 0 y 9. Puedes adivinarlo?")

user_number = int(input("Ingrese un número: "))
count = 0

while random_number != user_number:
  os.system('cls' if os.name == 'nt' else 'clear')

  if random_number == user_number:
    break
  elif user_number < random_number:
    print("El número ingresado es menor")
  else:
    print("El número ingresado es mayor")
  
  count += 1

  print(f"Cantidad de intentos: {count}")
  user_number = int(input("Ingrese un número: "))

print("Adivinaste!!!")
print(f"Cantidad de intentos: {count}")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 6 ##############################################

print("""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.""")

for i in range(100,0,-1):
  if i % 2 == 0:
    print(i)

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 7 ##############################################

print("""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.""")

number = int(input("Ingrese un numero positivo: "))
summation = 0

for i in range(0,number):
  summation += i

print(f"La suma de los numeros comprendidos entre 0 y {number} es: {summation}")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 8 ##############################################

print("""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).""")

max_number = 5
positive_number = 0
negative_number = 0
even_number = 0
odd_number = 0

print(f"\nDebe ingresar la cantidad de {max_number} números para evaluar si son positivos, negativos, pares o impares\n")

for i in range(max_number):
  number = int(input(f"Ingrese el {i+1} número: "))

  if number > 0:
    positive_number += 1
  else:
    negative_number += 1

  if number % 2 == 0:
    even_number += 1
  else:
    odd_number += 1

print(f"\nNúmeros positivos: {positive_number}\nNúmeros negativos: {negative_number}\nNúmeros pares: {even_number}\nNúmeros impares: {odd_number}")

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 9 ##############################################

print("""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).""")

max_number = 5
summation = 0

print(f"\nDebe ingresar la cantidad de {max_number} números para calcular la media.")

for i in range(max_number):
  number = int(input(f"Ingrese el {i+1} número: "))
  summation += number

average = summation / max_number

print(f"La media es de: {average}")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 10 #############################################
print("""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.""")

number = input("Ingrese un número: ")

inverted_number = number[::-1]
print(inverted_number)
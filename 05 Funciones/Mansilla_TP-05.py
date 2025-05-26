import os

############################################# EJERCICIO 1 ##############################################
print("""\n1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.\n""")

def imprimir_hola_mundo():
  print("Hola Mundo!")

imprimir_hola_mundo()

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 2 ##############################################
print("""\n2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de volver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.\n""")

def saludar_usuario(nombre):
  print(f"Hola {nombre}!")

saludar_usuario("Matias")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 3 ##############################################
print("""\n3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.\n""")

def informacion_personal(nombre, apellido, edad, residencia):
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("¿Cual es tu nombre?: ")
apellido = input("¿Cual es tu apellido?: ")
edad = input("¿Cuantos años tienes?: ")
residencia = input("¿Donde vives?: ")

informacion_personal(nombre, apellido, edad, residencia)

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 4 ##############################################
print("""\n4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.\n""")

from math import pi

radio = float(input("Ingrese el radio del círculo: "))

def calcular_area_circulo(radio):
  area = pi * (radio ** 2)
  return area

def calcular_perimetro_circulo(radio):
  perimetro = 2 * pi * radio
  return perimetro

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 5 ##############################################
print("""\n5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.\n""")

def segundos_a_horas(segundos):
  horas = segundos / 3600
  return horas

segundos = int(input("Ingrese la cantidad de segundos: "))
resultado = segundos_a_horas(segundos)

print(f"{segundos} segundos son equivalentes a: {resultado:.2f} horas")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 6 ##############################################
print("""\n6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la fun ción.\n""")

def tabla_multiplicar(numero):
  print(f"Tabla de multiplicar del {numero}:")
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 7 ##############################################
print("""\n7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.\n""")

def operaciones_basicas(a, b):
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  if b != 0:
    division = a / b
  else:
    division = "Error: División por cero"
  
  return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)

print(f"\nResultados:\nSuma: {resultados[0]}\nResta: {resultados[1]}\nMultiplicación: {resultados[2]}\nDivisión: {resultados[3]}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################ EJERCICIO 8 ##############################################
print("""\n8)  Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.\n""")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

resultado_imc = calcular_imc(peso, altura)

print(f"Su índice de masa corporal (IMC) es: {resultado_imc:.2f}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################ EJERCICIO 9 ##############################################
print("""\n9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.\n""")

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
resultado_fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celsius son equivalentes a {resultado_fahrenheit:.2f} grados Fahrenheit.")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################ EJERCICIO 10 ##############################################
print("""\n10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.\n""")

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

resultado_promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es: {resultado_promedio:.2f}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')
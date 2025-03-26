# Práctico 1: Estructuras secuenciales
# Alumno: Mansilla Matias
# Comisión: M2025-3

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Ejercicio 1 \n")
print("Hola mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
print("\nEjercicio 2 \n")

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
print("\nEjercicio 3 \n")

nombreUsuario = input("Ingresa tu nombre: ")
apellidoUsuario = input("Ingresa tu apellido: ")
edadUsuario =  int(input("Ingresa tu edad: "))
residenciaUsuario = input("Ingresa tu lugar de residencia: ")

print(f"Soy {nombreUsuario} {apellidoUsuario}, tengo {edadUsuario} y vivo en {residenciaUsuario} ")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 
print("\nEjercicio 4 \n")

radio = int(input("Ingrese el radio del circulo: "))
PI = 3.14
perimetro = 2 * radio * PI
area = PI * (radio ** 2)
print(f"El circulo tiene un perimetro de {perimetro:.2f} y un area de {area:.2f}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 
print("\nEjercicio 5 \n")

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivale a {horas:.2f} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.  
print("\nEjercicio 6 \n")

numero = int(input("Ingrese un numero: "))
print(f"La tabla de multiplicar de {numero} es: ")
print(f"{numero} * {0} = {numero * 0}")
print(f"{numero} * {1} = {numero * 1}")
print(f"{numero} * {2} = {numero * 2}")
print(f"{numero} * {3} = {numero * 3}")
print(f"{numero} * {4} = {numero * 4}")
print(f"{numero} * {5} = {numero * 5}")
print(f"{numero} * {6} = {numero * 6}")
print(f"{numero} * {7} = {numero * 7}")
print(f"{numero} * {8} = {numero * 8}")
print(f"{numero} * {9} = {numero * 9}")
print(f"{numero} * {10} = {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("\nEjercicio 7 \n")

numero1 = int(input("Ingrese un numero entero distinto de cero: "))
numero2 = int(input("Ingrese otro numero entero distinto de cero: "))

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 + numero2
cociente = numero1 + numero2

print(f"{numero1} + {numero2} = {suma:.2f}")
print(f"{numero1} - {numero2} = {resta:.2f}")
print(f"{numero1} * {numero2} = {producto:.2f}")
print(f"{numero1} / {numero2} = {cociente:.2f}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
print("\nEjercicio 8 \n")

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / altura ** 2
print(f"Su indice de masa corporal es de {imc:.2f}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
print("\nEjercicio 9 \n")

temperatura = float(input("Ingrese la temperatura en grados Celcius: "))
fahrenheit = temperatura * 9/5 + 32
print(f"{temperatura} grados Celcius es igual a {fahrenheit:.2f} grados Fahrenheit")

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.
print("\nEjercicio 10 \n")

numero_1 = float(input("Ingrese un numero: "))
numero_2 = float(input("Ingrese un segundo numero: "))
numero_3 = float(input("Ingrese un tercer numero: "))
promedio = (numero_1 + numero_2 + numero_3) / 3
print(f"El promedio es de {promedio:.2f}")
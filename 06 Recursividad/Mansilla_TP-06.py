import os

# ############################################# EJERCICIO 1 ##############################################
print("""\n1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario \n""")

def factorial(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num * factorial(num - 1)
  
numero = int(input("Ingrese un número entero positivo: "))
print(f"\nFactorial de {numero}: {factorial(numero)}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 2 ##############################################
print("""\n2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.\n""")

def fibonacci(posicion):
  if posicion == 0:
    return 0
  elif posicion == 1:
    return 1
  else:
    return fibonacci(posicion - 1) + fibonacci(posicion - 2)
  
posicion = int(input("Ingrese la posición en la serie de Fibonacci: "))
print(f"\nValor en la posición {posicion} de la serie de Fibonacci: {fibonacci(posicion)}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 3 ##############################################
print("""\n3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general. \n""")

def potencia(base, exponente):
  if exponente == 0:
    return 1
  else:
    return base * potencia(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"\n{base} elevado a {exponente} es: {resultado}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 4 ##############################################
print("""\n4) Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto.\n""")

def decimal_a_binario(numero):
    if numero == 0:
        return ""
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)

numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    resultado = decimal_a_binario(numero)
    if resultado == "":
        resultado = "0"
    print(f"\nLa representación en binario de {numero} es: {resultado}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 5 ##############################################
print("""\n5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed(). \n""")

def es_palindromo(palabra):
  # Convertimos la palabra a minúsculas para evitar problemas de mayúsculas/minúsculas y eliminamos espacios
  palabra = palabra.strip(palabra.lower())
    
  # Caso base: si la palabra tiene 0 o 1 caracteres, es un palíndromo
  if len(palabra) <= 1:
    return True
    
  # Comparamos el primer y último carácter
  if palabra[0] != palabra[-1]:
    return False
    
  # Llamada recursiva eliminando el primer y último carácter
  return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra o frase sin espacios ni tildes: ")
resultado = es_palindromo(palabra)

if resultado:
    print(f"\n'{palabra}' es un palíndromo.")
else:
    print(f"\n'{palabra}' no es un palíndromo.")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 6 ##############################################
print("""\n6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones: 
 - No se puede convertir el número a string. 
 - Usá operaciones matemáticas (%, //) y recursión. \n""")

def suma_digitos(n):
  # Caso base: si n es 0, la suma de los dígitos es 0
  if n == 0:
    return 0
  else:
    # Sumar el último dígito (n % 10) y llamar recursivamente con el resto del número (n // 10)
    return (n % 10) + suma_digitos(n // 10)

n = int(input("Ingrese un número entero positivo: "))
if n < 0:
  print("Por favor, ingrese un número entero positivo.")
else:
  resultado = suma_digitos(n)
  print(f"\nLa suma de los dígitos de {n} es: {resultado}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 7 ##############################################
print("""\n7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. 
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 0 nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. \n""")

def contar_bloques(n):
  # Caso base: si n es 0, no hay bloques
  if n == 0:
    return 0
  else:
    # Sumar el número de bloques en el nivel actual (n) y llamar recursivamente para el siguiente nivel (n - 1)
    return n + contar_bloques(n - 1)

n = int(input("Ingrese el número de bloques en el nivel más bajo: "))

if n < 0:
  print("Por favor, ingrese un número entero positivo.")
else:
  total_bloques = contar_bloques(n)
  print(f"\nEl total de bloques necesarios para construir la pirámide con {n} bloques en el nivel más bajo es: {total_bloques}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 8 ##############################################
print("""\n8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.\n""")

def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos
  if numero == 0:
        return 0
  else:
    # Verificar si el último dígito del número es igual al dígito buscado
    if numero % 10 == digito:
      return 1 + contar_digito(numero // 10, digito)
    else:
      return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9): "))

if numero < 0 or digito < 0 or digito > 9:
    print("Por favor, ingrese un número entero positivo y un dígito entre 0 y 9.")
else:
    resultado = contar_digito(numero, digito)
    print(f"\nEl dígito {digito} aparece {resultado} veces en el número {numero}.")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')
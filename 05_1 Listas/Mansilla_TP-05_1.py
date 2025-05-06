import os

############################################# EJERCICIO 1 ##############################################
print("""1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.\n""")

multiplos_de_4 = list(range(4,101,4))
print(f"{multiplos_de_4}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 2 ##############################################
print("""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.\n""")

deportes = ["Futbol", "Formula 1", "Tenis", "Motociclismo", "Running"]

# Mostramos el penúltimo elemento de la lista
print(f"\nEl penúltimo elemento de la lista {deportes} es: {deportes[-2]}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 3 ##############################################
print("""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.\n""")

fruits = []
print(f"Lista original: {fruits}")
fruits.append("Apple")
fruits.append("Orange") 
fruits.append("Strawberry")

print(f"Lista despues de agregar elementos: {fruits}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 4 ##############################################
print("""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.  Imprimir la lista resultante por pantalla. animales = ["perro", "gato", "conejo", "pez"] \n""")

animales = ["perro", "gato", "conejo", "pez"]
print(f"Lista original: {animales}")

# Reemplazo del segundo elemento
animales[1] = "loro"

# Reemplazo del último elemento
animales[-1] = "oso"

print(f"Lista modificada: {animales}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 5 ##############################################
print("""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)\n""")

# Se crea una lista de números
numeros = [8, 15, 3, 22, 7]
print(f"[1] Primero se crea una lista de números: {numeros}")

# La función max(numeros) devuelve el valor mas alto de la lista números, en este caso 22 y la función remove elimina el valor que se le pase por parametro. Es decir, de la lista números de va a eliminar el valor mas alto que es 22.
print("[2] De la siguiente linea 'numeros.remove(max(numeros))' tenemos que:")
print(f"* La función max(numeros) devuelve el valor mas grande de la lista. El valor mas grande de la lista es: {max(numeros)} ")
print(f"* La función remove() elimina el valor que se le pase por parametro. En este caso es 22")
numeros.remove(max(numeros))

# Por ultimo, se muestra la lista despues de ser modificada
print("[3] Se muestra por consola la lista modificada")
print(numeros)

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 6 ##############################################
print("""6)Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.\n""")
# Creamos la lista usando la funcion range
list = list(range(10,31,5))
print(f"De la siguiente lista: {list}")

# Se muestra los dos primeros valores
print(f"Los dos primeros valores son: {list[0]} y {list[1]}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 7 ##############################################
print("""7)Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.\n""")

autos = ["sedan", "polo", "suran", "gol"]
print(f"Lista original: {autos}")

autos[1] = "vento"
autos[2] = "golf"
print(f"Lista modificada: {autos}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 8 ##############################################
print("""8)Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.\n""")

dobles = []

dobles.append(10)
dobles.append(20)
dobles.append(30)

print(f"Lista dobles: {dobles}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 9 ##############################################
print("""9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
a) Agregar "jugo" a la lista del tercer cliente usando append. 
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla.\n""")

# Lista compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Agregamos 'jugo' a la lista del tercer cliente
compras[2].append("jugo")
print(f"\na){compras}")

# Remplazamos fideos por tallarines
compras[1][1] = "tallarines"
print(f"b){compras}")

# Eliminamos 'pan' del primer cliente
compras[0].remove("pan")
print(f"c){compras}")

# Mostrar lista resultante
print(f"d)La lista final es: {compras}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')

############################################# EJERCICIO 10 ##############################################
print("""10)Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
● Posición lista_anidada[0]: 15 
● Posición lista_anidada[1]: True 
● Posición lista_anidada[2][0]: 25.5 
● Posición lista_anidada[2][1]: 57.9 
● Posición lista_anidada[2][2]: 30.6 
● Posición lista_anidada[3]: False 
Imprimir la lista resultante por pantalla.\n""")

# Creamos la lista
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(f"La lista anidada es: {lista_anidada}")

# Mensaje para el usuario
input("\nPresione Enter para continuar...")
# Limpiamos la terminal
os.system('cls' if os.name == 'nt' else 'clear')
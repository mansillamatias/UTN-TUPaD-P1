"""
1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300 
"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("1) Diccionario de precios de frutas actualizado:")
for fruta, precio in precios_frutas.items():
    print(f"{fruta}: ${precio}")

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800 
"""

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\n2) Diccionario de precios de frutas actualizado con nuevos precios:")
for fruta, precio in precios_frutas.items():
    print(f"{fruta}: ${precio}")

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios. 
"""

frutas = list(precios_frutas.keys())
print("\n3) Lista de frutas sin precios:")
print(f"{frutas}\n")

"""
4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""
contactos = {}

print("4) Almacenamiento de contactos telefónicos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    contactos[nombre] = numero

print("\n4) Contactos almacenados:")
for nombre, numero in contactos.items():
    print(f"{nombre}: {numero}")

nombre_consulta = input("\nIngrese el nombre del contacto que desea consultar: ")
if nombre_consulta in contactos:
    print(f"Número telefónico de {nombre_consulta}: {contactos[nombre_consulta]}")
else:
    print(f"No se encontró el contacto: {nombre_consulta}")

"""
5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra. 
"""
print("\n5) Solicita al usuario una frase e imprime:")
frase = input("\nIngrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

print("\n5) Palabras únicas:")
print(palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("\nCantidad de veces que aparece cada palabra:")
for palabra, cantidad in contador_palabras.items():
    print(f"{palabra}: {cantidad}")

"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno.
"""

print("\n6) Ingreso de alumnos y sus notas:")
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas = tuple(float(input(f"Ingrese la nota {j + 1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""

print("\n7) Listas de estudiantes que aprobaron Parcial 1 y Parcial 2:")
parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {103, 104, 106, 107}
print(f"Parcial 1: {parcial_1}")
print(f"Parcial 2: {parcial_2}")

# Estudiantes que aprobaron ambos parciales
aprobados_ambos = parcial_1.intersection(parcial_2)
print("\nEstudiantes que aprobaron ambos parciales:")
for estudiante in aprobados_ambos:
    print(estudiante)

# Estudiantes que aprobaron solo uno de los dos parciales
aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2)
print("\nEstudiantes que aprobaron solo uno de los dos parciales:")
for estudiante in aprobados_solo_uno:
    print(estudiante)

# Lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
aprobados_total = parcial_1.union(parcial_2)
print("\nLista total de estudiantes que aprobaron al menos un parcial (sin repetir):")
for estudiante in aprobados_total:
    print(estudiante)

"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe.
"""

print("\n8) Gestión de stock de productos:")
stock_productos = {
    'Laptop': 10,
    'Smartphone': 25,
    'Tablet': 15,
    'Auriculares': 30
}

print("\nStock de productos:")
for producto, cantidad in stock_productos.items():
  print(f"{producto}: {cantidad} unidades")

producto_consulta = input("\nIngrese el nombre del producto que desea consultar: ")
if producto_consulta in stock_productos:
    print(f"Stock de {producto_consulta}: {stock_productos[producto_consulta]} unidades")
    
    agregar_stock = input("¿Desea agregar unidades al stock? (s/n): ").lower()
    if agregar_stock == 's':
        unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
        stock_productos[producto_consulta] += unidades
        print(f"Nuevo stock de {producto_consulta}: {stock_productos[producto_consulta]} unidades") 

else:
    print(f"El producto {producto_consulta} no existe en el stock.")
    agregar_producto = input("¿Desea agregar este nuevo producto? (s/n): ").lower()
    if agregar_producto == 's':
        unidades = int(input(f"Ingrese la cantidad de unidades de {producto_consulta}: "))
        stock_productos[producto_consulta] = unidades
        print(f"Producto {producto_consulta} agregado con {unidades} unidades al stock.")

print("\nStock actualizado de productos:")
for producto, cantidad in stock_productos.items():
    print(f"{producto}: {cantidad} unidades")

"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.
"""
print("\n9) Agenda de eventos:")
agenda = {
    ('Lunes', '10:00'): 'Reunión con el equipo',
    ('Martes', '14:00'): 'Cita médica',
    ('Miercoles', '16:00'): 'Presentación del proyecto'
}
def consultar_evento(dia, hora):
    evento = agenda.get((dia, hora))
    if evento:
        print(f"Evento en {dia} a las {hora}: {evento}")
    else:
        print(f"No hay eventos programados para {dia} a las {hora}.")

dia_consulta = input("Ingrese el día de la semana: ")
hora_consulta = input("Ingrese la hora (formato HH:MM): ")
consultar_evento(dia_consulta, hora_consulta)

"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores. 
"""
print("\n10) Diccionario de países y capitales:")
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Japón': 'Tokio',
    'España': 'Madrid'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("Diccionario original de países y capitales:")
for pais, capital in paises_capitales.items():
    print(f"{pais}: {capital}")

print("\nNuevo diccionario con capitales como claves y países como valores:")
for capital, pais in capitales_paises.items():
    print(f"{capital}: {pais}")
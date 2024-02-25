#!/usr/bin/env python
# coding: utf-8

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
numero_entero = 5
if numero_entero > 0:
    print("El número es mayor que cero.")
elif numero_entero < 0:
    print("El número es menor que cero.")
else:
    print("El número es igual a cero.")

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
variable1 = 10
variable2 = "Hola"
if type(variable1) == type(variable2):
    print("Las variables son del mismo tipo de dato.")
else:
    print("Las variables no son del mismo tipo de dato.")

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} es par.")
    else:
        print(f"{i} es impar.")

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(6):
    print(f"{i} elevado a la potencia 3 es igual a {i**3}.")

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
numero_ciclos = 3
for i in range(numero_ciclos):
    print(f"Este es el ciclo número {i+1}.")

# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
numero_factorial = 5
if isinstance(numero_factorial, int) and numero_factorial > 0:
    resultado = 1
    while numero_factorial > 0:
        resultado *= numero_factorial
        numero_factorial -= 1
    print(f"El factorial es {resultado}.")

# 7) Crear un ciclo for dentro de un ciclo while
contador = 0
while contador < 3:
    for letra in "abc":
        print(letra)
    contador += 1

# 8) Crear un ciclo while dentro de un ciclo for
for i in range(3):
    contador = 0
    while contador < i + 1:
        print(contador)
        contador += 1

# 9) Imprimir los números primos existentes entre 0 y 30
for numero in range(2, 31):
    es_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero)

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
for numero in range(2, 31):
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            break
    else:
        print(numero)

# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
numero = 100
while numero <= 300:
    if numero % 12 == 0:
        print(numero)
    numero += 1

# 13) Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usuario de buscar el siguiente
while True:
    numero = int(input("Ingrese un número (o '0' para salir): "))
    if numero == 0:
        break
    if numero < 2:
        print("El número debe ser mayor o igual a 2.")
        continue
    es_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es primo.")
    else:
        print(f"{numero} no es primo.")

# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
numero = 100
while numero <= 300:
    if numero % 3 == 0 and numero % 6 == 0:
        print(f"El primer número divisible por 3 y múltiplo de 6 es {numero}.")
        break
    numero += 1


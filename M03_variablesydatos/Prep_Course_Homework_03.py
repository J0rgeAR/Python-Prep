#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
numero_entero = 5
print(numero_entero)

# 2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(numero_entero))

# 4) Crear una variable que contenga tu nombre
mi_nombre = "Juan"
print(mi_nombre)

# 5) Crear una variable que contenga un número complejo
numero_complejo = 3 + 2j

# 6) Mostrar el tipo de dato de la variable creada en el punto 5
print(type(numero_complejo))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
verdad_str = 'True'
verdad_bool = True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(verdad_str))
print(type(verdad_bool))

# 10) Asignar a una variable, la suma de un número entero y otro decimal
suma_entero_decimal = 3 + 4.5

# 11) Realizar una operación de suma de números complejos
suma_complejos = (2 + 3j) + (1 + 2j)

# 12) Realizar una operación de suma de un número real y otro complejo
suma_real_complejo = 2 + (1 + 2j)

# 13) Realizar una operación de multiplicación
multiplicacion = 3 * 4

# 14) Mostrar el resultado de elevar 2 a la octava potencia
potencia = 2 ** 8

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27 / 4
print(cociente)

# 16) De la división anterior solamente mostrar la parte entera
parte_entera = 27 // 4
print(parte_entera)

# 17) De la división de 27 entre 4 mostrar solamente el resto
resto = 27 % 4
print(resto)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
resultado = 4 * parte_entera + resto
print(resultado)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
cadena1 = "Hola "
cadena2 = "mundo"
concatenacion = cadena1 + cadena2
print(concatenacion)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("2" == 2)  # Devuelve False porque son tipos diferentes

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int("2") == 2)  # Convertimos la cadena "2" a entero y comparamos

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# Arroja error porque el separador decimal debe ser punto (.) en lugar de coma (,). Sería: a = float('3.8')

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.
variable = 3
variable -= 1
print(variable)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
# El operador << realiza un desplazamiento de bits hacia la izquierda. En este caso, desplaza los bits de 1 dos posiciones a la izquierda,
# lo que es equivalente a multiplicar por 2 dos veces en el sistema binario. Entonces, 1 en binario es 01, y al desplazar dos veces a la izquierda, obtenemos 100, que es 4 en decimal.

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# No está permitido porque los tipos de datos son diferentes (int y str). En Python, la operación "+" está definida de manera diferente para diferentes tipos de datos. Si los dos operandos son del mismo tipo, el resultado generalmente será el esperado, pero aún puede haber casos especiales, como la concatenación de cadenas.

# 26) Realizar una operación válida entre valores de tipo entero y string
resultado_operacion = 5 * int('3')
print(resultado_operacion)




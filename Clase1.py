#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase 01
Created on Fri Dec 29 19:53:03 2023
@author: florencia
"""

# Definir variables 
miValor = 2
valorUsusario = input()

print(miValor)
print(valorUsusario)

# Operadores de asignación
a = 4
a += 5
a -= 5
a *= 5
a /= 5
a **= 5

print(a)

# Suma
suma = 1 + 1
print('Suma:', suma)
print('Suma directa:', 1 + 1)

# Resta 
resta = 1 - 1
print('Resta:', resta)

# Multiplicación
multiplicacion = 5 * 5
print('Multiplicación:', multiplicacion)

# Division
division = 100 / 10
print('División:', division)

print(type(division))

# Division entera
division_entera = 100 // 10
print('Division entera:', division_entera)
print(type(division_entera))

# Division modulo
division_modulo = 2 % 3
print('Division modulo:', division_modulo)

# Exponenciación
exponenciacion = 2 ** 2
print('Exponenciación:', exponenciacion)


# Asignación multiple
miVariable1, miVariable2, miVariable3 = 4, 3, 'Hola'
print(miVariable1, miVariable2, miVariable3)

miEntero, miBooleano = 15, True
print(miEntero, miBooleano)

# Strings Functions
# Concatenación
print('Hola' + 'Mundo')

miCadena1, miCadena2 = 'Hola', 'Virginia'
print(miCadena1, miCadena2)

# Repetición
print(miCadena2 * 10)

# Indexar
miIndexacion = 'La desigualdad es más grave para las mujeres'
print(miIndexacion[6])

# Slicing/ rebanar -->Revisar
print(miIndexacion[0:4])
print(miIndexacion[0:8:4])

# Input/ Valores de entrada
input('Cuantos años tienes:')

print('¡Hola, tontos!')

saludo = '¡Holaaaaa!'
print(saludo)

nombre = input('Escribe tu nombre:')
print('_ . _ . _ .')

print(f'¡Hola, {nombre}!')

operacion = ((-2)/(2 * 2)) ** 2
print('El resultado de la operación es:', operacion)

# Ejercicios de lógica -->revisar
a = 2
b = 3
if a == 2:
        a = 3
        
if b == 3:
        b = 2
        
print('El valor de a es:', a)
print('El valor de b es:', b)
    
a, b = 2, 3
a, b = b, a
    
print('El valor de a es:', a)
print('El valor de b es:', b)
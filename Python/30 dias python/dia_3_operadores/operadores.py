# Operadores
# https://www.w3schools.com/python/python_operators.asp

import math
from turtle import width


print(2+5)
print(2-5)
print(2*5)
print(2/5)
print(2//5)  # sin numero flotante
print(2**3)  # 2 * 2 * 2

num1 = 2
num2 = 3
num2 += num1

print(num2)

# numeros complejos

print(1+1j)
print((1+1j)*(1-2j))

# ejemplo (area, volume,density, weight, perimeter, distance, force)

# area de un circulo
# radio = float(input("pasame el radio del circulo: "))
# area_of_circule = math.pi * radio ** 2  # tambien podes usar sqrt
# print("el area del circulo es =", area_of_circule)

# # area de rectangulo
# length = int(input("pasame el largo del rectangulo: "))
# width = int(input("pasame el ancho del rectangulo: "))

# area_of_rectangle = length * width
# print("el area del rectangulo es =", area_of_rectangle)

# # densidad de un liquido
# masa = int(input("pasame la masa del liquido en kg: "))
# volumen = int(input("pasame el volumen del liquido en metros cubicos: "))
# densidad = masa / volumen
# print("la densidad es =", densidad)

# operadores de comparacion
# == , != , < , > , <=, >=

print(3 == 2)
print(3 != 2)
print(3 < 2)
print(3 > 2)
print(3 <= 2)
print(3 >= 2)
print(len("hola") == len("como estas?"))
print(len("hola") != len("como estas?"))
print(len("hola") > len("como estas?"))
print(len("hola") < len("como estas?"))
print(len("hola") <= len("como estas?"))
print(len("hola") >= len("como estas?"))

# otra forma de comprobar sin operadores logicos
print(1 is 1)
print(1 is not 2)
print("A" in "abcdefg")
print("A" in "Abcdefg")
print("coding" in "coding is good")
print(4 is 2**2)

# operadores logicos
print(3 < 5 and 4 < 2)
print(3 < 5 or 4 < 2)
print(not 3 < 5)
print(not True)
print(not not True)

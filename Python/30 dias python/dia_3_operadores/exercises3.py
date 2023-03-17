# edad = int(input("pasame tu edad: "))
# altura = float(input("pasame tu altura: "))
# num_complejo = 1 + 5j

# area de un triangulo
# base = int(input("pasame la base: "))
# altura = int(input("pasame la altura: "))
# area_of_tringle = 0.5 * base * altura
# print("el area del tiangulo es =", area_of_tringle)

# perimetro de un triangulo
# lado_a = int(input("pasame el lado a: "))
# lado_b = int(input("pasame el lado b: "))
# lado_c = int(input("pasame el lado c: "))
# perimetro = lado_a + lado_b + lado_c
# print("el perimetro del tiangulo es =", perimetro)

# base = int(input("pasame la base: "))
# altura = int(input("pasame la altura: "))
# perimetro = (base + altura) * 2
# print("el perimetro es =",perimetro)

# comparar
python_length = len("python")
dragon_length = len("dragon")
print(python_length < dragon_length)

print(("on" in "python") and ("on" in "dragon"))

print(("on" not in "python") and ("on" not in "dragon"))

# convertir de float a str
len_python = str(len("python"))
print(type(len_python))

# numero par
num = 5
res = num % 2
print(res == 0)

print(7/3 == int(2.7))

print(type(10) == type("10"))

# tabla

array_bidimensional = [[1, 1, 1, 1], [2, 1, 2, 4, 8], [3, 1, 3, 9, 27],
                       [4, 1, 4, 16, 64], [5, 1, 5, 25, 125]]

print(array_bidimensional[0], "\n")
print(array_bidimensional[1], "\n")
print(array_bidimensional[2], "\n")
print(array_bidimensional[3], "\n")
print(array_bidimensional[4], "\n")

for i in range(len(array_bidimensional)):
    for j in range(len(array_bidimensional[i])):
        print(array_bidimensional[i][j], end=" ")
    print()

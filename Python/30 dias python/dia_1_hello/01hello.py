# hola esto es un comentario

# nuestro print
print("hello Tino")

"""
hola soy un comentario
en varias
lineas
"""
print(" ")

# tipoes de datos
print("TIPOS DE DATOS")

num = 4

print(int(num))
print(float(num))

cadena = "hola soy un " + str(num) + " hecho cadena"

print(cadena)

print(" ")

# listas (como los arrays en JS)
print("LISTAS")

frutasListas = ["banana", "manzana", "pera"]

print(frutasListas[0])
print(frutasListas[1])
print(frutasListas[2])

print(" ")

# diccionarios (como los objetos en JS)
print("DICCIONARIOS")

diccionario = {
    "nombre1": "Tino",
    "nombre2": "Juan",
    "nombre3": "Martin",
    "num1": 4,
    "num2": 6,
    "frutas": ["banana", "manzana", "pera"]
}

print(diccionario["nombre1"])
print(diccionario["num1"])
print(diccionario["frutas"][0])

print(" ")

# tuplas (como las listas pero una ves creadas no se pueden modificar)
print("TUPLAS")

tupla = ("auto", "tv", "cell")

print(tupla[2])

print(" ")

# set (Los elementos establecidos(set) no se pueden modificar, pero puede eliminar elementos y agregar elementos nuevos), estos elementos a diferencias de las listas y tuplas estan desordenados (osea cada ves q los uses pueden aparecen en orden distinto)
# ignora los datos duplicados
print("SET")

frutasSet = {4, "banana", "pera", 7}

print(frutasSet)

print(" ")

# check data type
print("TYPE()")

variable1 = 4
variable2 = "hola"

print(type(variable1))
print(type(variable2))
print(type(3.14))
print(type([1, 2, 3]))
print(type({'name': 'Asabeneh'}))
print(type({9.8, 3.14, 2.7}))
print(type((9.8, 3.14, 2.7)))

print(" ")

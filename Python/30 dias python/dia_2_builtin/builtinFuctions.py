# builtin function son funciones globales para tu uso
# las mas comunes --> print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir()
# https://docs.python.org/3.9/library/functions.html --> aca estan el todas

from turtle import pen


cadena = "Hola Tino"
num1 = 4
num2 = 6

largo = len(cadena)
print("el largo de la palabra es = " + str(largo) + "\n")

print(type(str(num1)), "\n")

numInt = int(num1)
print(numInt, "\n")

numFloat = float(num1)
print(numFloat, "\n")

convertirAStr = str(num1)
print(type(convertirAStr), "\n")

# pasameUnTexto = input("escribime algo pibe: ")
# print(pasameUnTexto,"\n")

lista = [4, 5, 6]
listaList = list(lista)
print(lista)
print(lista[0], "soy un numero de la lista\n")


diccionario = dict({
    "nombre": "Tino",
    "edad": "4",
    "machichitas": "muchas",
})
print(diccionario["nombre"], "\n")

maximo = max(num1, num2)
print("el numero maximo es ", maximo, "\n")

minimo = min(num1, num2)
print("el numero minimo es ", minimo, "\n")

numerosList = [9, 10, 8, 4, 6]
suma = sum(numerosList)
print("la suma de todos los elementos de la lista es = ", suma, "\n")


ordenar = sorted(numerosList)
print(ordenar)  # tambine funciona con las letras

letrasList = ("a", "z", "b", "h", "x", "p")
print(sorted(letrasList), "\n")


f = open("30 dias Python\dia 2\demo.txt", "r")
print(f.read(), "\n")

# print(help())

# dir() retorna todas las propiedades y metodos de un objeto
objeto = {
    "nombre": "objeto",
    "numero": 56,
    "email": "hola@gmail.com",
}

print(dir(objeto))


# variables
# nada q no sepas ya salvo q si queres usar una palabra declarado como funcion agragale _ adelante del nombre --> _if
""" vairbles invalidas --> first-name
first@name
first$name
num-1
1num
"""

# declarar multiples variables en una sola linea
nombre, apellido, edad = "Tino", "Machichita", 10

# datos q estan compuestos por otros datos

# listas

# lista vacia
lista = []
# lista compuesta
lista = ["Tino", 45, False]

print(lista)
print(lista[1])

lista[0] = "Juan"
print(lista[0])

# tupla (a diferencia de las listas estas no pueden modificar sus datos)
tupla = ("Tino", 45, False)
print(tupla[0])
# tupla[0] = "Juan"
# print(tupla[0]) --> TypeError: 'tuple' object does not support item assignment


# set (cojuntos) (no tienen orden fijo, osea las posiciones pueden cambiar pero no se pueden modificar los elementos) (no se pueden repetir valores)
set = {"Tino", 45, False}

# dict (diccionario) () ()
# se escribe de la misma forma q un json
diccionario = {
    # key       value
    'nombre': 'Tino',
    'edad': 13,
    'comida': 'Todo',
    'durmiendo': True
}

print(diccionario['nombre'])

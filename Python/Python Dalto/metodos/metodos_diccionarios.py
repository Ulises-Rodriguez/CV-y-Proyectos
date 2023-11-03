diccionario = {
    "nombre": "Tino",
    "edad": 13,
    "comidas": "Pollo y zapallo"
}

# keys() --> devuelve las claves (tambien sirve para iterar)
claves = diccionario.keys()
print(claves)

# get() --> devuelve el valor de una clave, si no lo encuentra el programa continua
valor = diccionario.get("nombre")
print(valor)

# pop() --> elimina un elemento
elem_pop = diccionario.pop("comidas")
print(elem_pop)
print(diccionario)

# clear --> elimina todo el diccionario
diccionario2 = {
    "nombre": "Tino",
    "edad": 13,
    "comidas": "Pollo y zapallo"
}

diccionario2.clear()
print(diccionario2)

# items() --> para iterar un dict
dict_iterable = diccionario.items()
print(dict_iterable)

# diccionarios
'''
los diccionarios son una coleccion de item no ordenados,modificable y sus elementos son key:value
'''

# crear dict
from numpy import empty


empty_dict = {}
empty_dict2 = dict()

# dict con valores
dict_values = {
    "nombre": "Tino",
    "comida": "Machichita",
    "edad": 10,
    "numeros": [4, 8, 9, 6],
    "direccion": {
        "calle": "Angelo Peredo",
        "numero": 34
    }
}


print(dict_values)
print()

# len
print(len(dict_values))
print()

# acceder a los elementos
print(dict_values['nombre'])
print(dict_values["comida"])
print(dict_values["numeros"][2])
print(dict_values["direccion"]["calle"])
# print(dict_values['nombresdfsd']) --> da error xq no existe esta key

print()

# agregar un elemento
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct["key5"] = "Hola soy un valor agragado"
print(dct)
print()

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
person['saludo'] = "Hola"
person['skills'].append('HTML')

print(person)
print()

# modificar elementos
person['age'] = "20"
print(person['age'])

print()

# check a key en el dict
print("country" in person)
print("countrysdasgdf" in person)
print()

# remover un par key:value
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.pop("key1")
print(dct)
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.popitem()  # remove the last item
print(dct)
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
del dct["key2"]
print(dct)
print()

# pasar de dict a list --> items() cambia el dict a una lista de tuplas
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items())

print()

# clear
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.clear()
print(dct)
print()

# delete
numeros = {5, 8, 9, 36, 4}
del numeros
# print(numeros)
print()

# copy
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct.copy()
print(dct_copy)
print()

# obtener la key --> te retorna una lista
print(dct.keys())
print()

# obtener los values --> te retorna una lista
print(dct.values())
print()

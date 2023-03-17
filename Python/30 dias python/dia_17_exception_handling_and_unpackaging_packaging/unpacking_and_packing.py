# Unpacking:

# list
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
# TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# print(sum_of_five_nums(lst))


# para evitar el error tenes q desempacar los elementos de la lista lst --> unpacking
# Unpacking:

# list
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]

# usando el "*" desempacas todos los elementos de lst
print(sum_of_five_nums(*lst))
print()


# podemos desempacar usando la funcion range
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers))  # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = list(range(*args))  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]
print()

# una lista de tuplas
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# esto lo q hace es los primeros 3 elementos de desempacan y se guardan en una variable y el resto en una lista en *rest
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
# aca el primer elemento de desempaca en "one" y todos los elementos excepto el ultimo en "*middle" y el ultimo en "last"
one, *middle, last = numbers
print(one, middle, last)  # 1 [2, 3, 4, 5, 6] 7
print()


# desempacando diccionarios
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'


dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
# Asabeneh lives in Finland, Helsinki. He is 250 years old.
print(unpacking_person_info(**dct))
print()


# Packing
'''
algunas veces no sabemos cuantos argumentos se necesitan pasarle a una funcion, podemos usar el packing metodo para q nuestra funcion tomo un numero ilimitado de argumentos
'''


# Packing Lists
def sum_all(*args):  # usando el "*" indicamos q la funcion tiene un numero arbitrario de parametros, es como el spread operator de "..." de JS
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))
print()


# Packing Dictionaries
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs


print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

print()


#Spreading in Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
# ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print(nordic_countries)

print()


# Enumerate
# Si estamos interesados en el índice de una lista, usamos la función integrada de enumeración para obtener el índice de cada elemento de la lista.
for index, item in enumerate([20, 30, 40]):
    print(index, item)
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print('The country {i} has been found at index {index}')

print()


# Zip
# toma iterables (pueden ser cero o más), los agrega en una tupla y lo devuelve. (tambien pueden ser listas)
# Si se pasa un solo iterable, zip()devuelve un iterador de tuplas con cada tupla que tiene solo un elemento.
# Si se pasan varios iterables, zip()devuelve un iterador de tuplas y cada tupla tiene elementos de todos los iterables.
# Supongamos que se pasan dos iterables a zip(); uno iterable que contiene tres y otro que contiene cinco elementos. Entonces, el iterador devuelto contendrá tres tuplas. Es porque el iterador se detiene cuando se agota el iterable más corto.

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)

print()


# ejem 2 (con listas de distinto tamaño)
numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)
print()

# desempacar con zip
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v = zip(*result_list)
print('c =', c)
print('v =', v)

print()
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

print(fruits_and_veges)

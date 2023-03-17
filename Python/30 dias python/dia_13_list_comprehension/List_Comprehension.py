# List Comprehension
# es una forma compacta de crear listas a partir de una secuencia, esta forma es mucho mas rapida q crear listas usando for loops

# syntax
# [i for i in iterable if expression]


# cambiar de string a array
# forma normal
language = "Python"

lst = list(language)
print(type(lst))
print(lst)
print()

# forma compacta
lst = [i for i in language]
print(type(lst))
print(lst)
print()

# generar lista de numeros
nums = [i for i in range(11)]
print(nums)
print()

# se pueden hacer operaciones matematicas
nums2 = [i*i for i in range(11)]
print(nums2)
print()

# lista de tuplas
nums3 = [(i, i*i) for i in range(11)]
print(nums3)
print()


# lista comprendida con if
even_nums = [i for i in range(21) if i % 2 == 0]
print(even_nums)
print()

# to generate odd numbers in range 0 to 21
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)
print()

# con and/or tambien
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_nums = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_nums)
print()

# descomponiendo un array de 3 dimensiones
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)
print()

# esto para q compares una cosa con otra, mira la diferencia entre el ejem de arriva y este
aux_lst = []

for row in list_of_lists:
    print(row)
    for column in row:
        print(column)
        aux_lst.append(column)
print(aux_lst)
print()


# funcion lambda
# es una pequeña funcion anonima sin nombre, esta puede tomar cualquier numero de argumentos, seguido de una exprecion
# lambda tiene un return implicito

# syntax
# def x(param1, param2, param3): return param1 + param2 + param2
# print(x(arg1, arg2, arg3))

# comparacion con una funcion normal
def add_two_nums(a, b):
    return a + b


print(add_two_nums(2, 3))
print()

print((lambda a, b: a+b)(2, 3))
print()

#square = lambda x : x ** 2
# print(square(3))
# te lo auto convierte un una funcion


# lambda dentro de otra funcion
def power(x):
    return lambda n: x**n


cube = power(2)(3)  # la funcion power necestita otro argumento ahora
print(cube)

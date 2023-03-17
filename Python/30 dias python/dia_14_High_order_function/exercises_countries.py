# Explain the difference between map, filter, and reduce.

''''
map toma una lista y una funcion q se le aplica a los elems de la lista devolviendo una lista nueva con los cambios aplicados

filter toma una lista y una funcion q aplica algun tipo de condicion, y devuelve una lista con los elems q cuplan esa condicion

reduce es una funcion de functools module q hay q imporatar, toma una lista y una funcion y devuleve el resultado en un unico elemento
'''

# Explain the difference between higher order function, closure and decorator

'''
funciones high order son ciudadanos de primer orden osea funciones q pueden tomar otras funciones como parametros, retornar otras funciones

closure son funciones dentro de otras funciones, estas consta de una funcion principal y una funcion interna q esta definida dentro de la funcion principal
lo q retorna la funcion principal es la funcion interna

decorator es patron de diseño, osea tomar una funcion/metodo/objeto q ya existe y darle funcionalidades nuevas sin alterar su estructura original
'''
from countries_list import country_list
from countries_data import country_list_data
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define a call function before map, filter or reduce, see examples.


def sum_one(num):
    return num + 1


def vowel_name(name):
    if name[0] in 'aeiouAEIOU':
        return True
    return False


def concat(a, b):
    return ", ".join((a, b))


print(list(filter(vowel_name, names)))
print(list(map(sum_one, numbers)))
print(reduce(concat, countries))
print()


# Use for loop to print each country in the countries list.
for country in countries:
    print(country)
print()

# Use for to print each name in the names list.
for i in names:
    print(i)

print()

# Use for to print each number in the numbers list.
for i in numbers:
    print(i)
print()


# Use map to create a new list by changing each country to uppercase in the countries list
def up(country):
    return country.upper()


print(list(map(up, countries)))
print()


# Use map to create a new list by changing each number to its square in the numbers list
def square_enix_XD(num):
    return num**2


res = list(map(square_enix_XD, numbers))

print(res)
print()


# Use map to change each name to uppercase in the names list
print(list(map(up, names)))
print()


# Use filter to filter out countries containing 'land'.
def contain_land(countri):
    if "land" in countri:
        return True
    return False


print(list(filter(contain_land, countries)))
print()


# Use filter to filter out countries having exactly six characters.
def amount_characters(country):
    if len(country) == 6:
        return False
    return True


print(list(filter(amount_characters, countries)))
print()


# Use filter to filter out countries containing six letters and more in the country list.
def amount_characters2(country):
    if len(country) > 6:
        return False
    return True


print(list(filter(amount_characters2, countries)))
print()


# Use filter to filter out countries starting with an 'E'
def start_E(country):
    if country[0] in "E":
        return True
    return False


print(list(filter(start_E, countries)))
print()

# Chain two or more list iterators(eg. arr.map(callback).filter(callback).reduce(callback))


def even(num):
    if num % 2 == 0:
        return True
    return False


def sum(a, b):
    return a+b


res = reduce(sum, list(map(sum_one, list(filter(even, numbers)))))
print(res)

print()

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.


def get_string_lists(lst):
    res = []

    for item in lst:
        for i in item:
            res.append(i)

    return res


print(get_string_lists(names))
print()

# Use reduce to sum all the numbers in the numbers list.

print(reduce(sum, numbers))
print()


# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print(reduce(concat, countries))
print()


# Declare a function called categorize_countries that returns a list of countries with some common pattern(you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries():
    res = []

    for country in country_list:
        if "land" in country or "ia" in country or "island" in country or "stan" in country:
            res.append(country)

    return res


print(categorize_countries())
print()

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
keys = []
keys = [i[0] for i in country_list if i[0] not in keys]


def count(inicial, lst):
    res = 0

    for i in lst:
        if inicial == i:
            res += 1
        else:
            return res

    return res


def remove_string(indice, lst, amount):

    for _ in range(amount+1):
        del lst[0]

    return lst


def iniciales(lst):
    res = []
    aux = []
    amount = 0

    for i in lst:
        if i not in aux:
            aux.append(i)

    for _ in range(len(aux)):
        amount = count(aux[0], lst)
        res.append((aux[0], str(amount)))
        del aux[0]

        if aux != []:
            lst = remove_string(aux[0], lst, amount)

    return res


res = iniciales(keys)
# print(res)
print(dict(res))
print()

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
res = []
res = [country_list[i] for i in range(len(country_list)) if i < 10]
print(res)
print()


def get_first_ten_countries():
    res = []

    for i in range(len(country_list)):
        if i < 10:
            res.append(country_list[i])

    return res


print(get_first_ten_countries())
print()


# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

def get_last_ten_countries():
    res = []
    country_list.reverse()
    for i in range(len(country_list)):
        if i < 10:
            res.append(country_list[i])

    return res


print(get_last_ten_countries())
print()


# Sort countries by name, by capital, by population
# print(sorted(country_list_data, key=lambda name: name["name"]))
# print(sorted(country_list_data, key=lambda capital: capital["capital"]))
# print(sorted(country_list_data,
#       key=lambda population: population["population"]))
# print()


# Sort out the ten most spoken languages by location.
def languages(lst):
    res = []

    for country in range(len(lst)):

        for language in range(len(lst[country]["languages"])):
            res.append(lst[country]["languages"][language])

    return res


def count2(inicial, lst):
    amount = 0
    res = []

    for i in lst:
        if inicial == i:
            amount += 1

    return amount


def big_ten(lst):
    aux = []
    lst.sort(key=lambda x: x[1], reverse=True)

    for i in range(0, 10):
        aux.append(lst[i])

    return aux


def count_languages(lst):
    languages_list = []
    languages_list = languages(lst)

    amount = 0
    res = []

    for language in languages_list:
        amount = count2(language, languages_list)

        if (language, amount) not in res:
            res.append((language, amount))

    res = big_ten(res)

    return res


print(count_languages(country_list_data))
print()

# Sort out the ten most populated countries.
res = sorted(country_list_data,
             key=lambda population: population["population"], reverse=True)

res = res[0:10]

for item in res:
    country = item["name"]
    population = item["population"]
    print("{} tiene una pobalcion de {}".format(country, population))

# Listas

'''
tenemos 4 formas de crear listas:
1) listas (list)--> coleccion de elementos ordenados, modificables y permiten elementos repetidos
2) tuplas (tuple)--> ordenada, no modificable, permite elementos repetidos
3) set --> no ordenada, no indexada, no modificable, no elementos repetidos
4) diccionario (dict)--> no ordenada, modificable, indexada y no elementos repetidos

estas listas pueden estar vacias o tener varios elementos de distinto tipo
'''

# crear lista

# con builtin-function

lista = list()
print("esto es una lista vacia creada con list()", lista)

print()

lista2 = []
print("esto es una lista vacia creada con []", lista2)

print()

# lista con valores iniciales
fruits = ['banana', 'orange', 'mango', 'lemon']
print("frutas lista:", fruits)
print("length de lista de frutas", len(fruits))

print()

# lista con diferentes tipos

lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]
print(lst)

print()

# para acceder a cierto elemento uso la posicion
print(fruits[0])
last_index = len(fruits) - 1
print(fruits[last_index])

print()

# al usar numeros negativos el recorrido de la lista es al reves osea ["manzana","banana","pera"] -1 --> pera -2 --> banana -3 --> manzana

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

print()

# desempacar elementos
lst_unpacking = ['item', 'item2', 'item3', 'item4', 'item5']
# el * es para indicar q el resto de elemtos los guarde en rest
first_item, second_item, third_item, *rest = lst_unpacking
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

print()

first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

print()

# slice elementos de la lista: podemos especificar start, end y step, el resultado va a ser una nueva lista
fruits_slice = ['banana', 'orange', 'mango', 'lemon']

# puede ser un numero mas grande como para indicar dale hasta el final (lo ideal seria guardar el maximo de la lista en una variable)
all = fruits_slice[0:4]
print("todas las frutas", all)

all2 = fruits_slice[0:]
print("todas las frutas", all2)

# para un ejemplo mas visual
# https://www.geeksforgeeks.org/python-list-slicing/#:~:text=With%20this%20operator%2C%20one%20can,list%20from%20the%20existing%20list.&text=If%20Lst%20is%20a%20list,at%20a%20step%20size%20IndexJump.
orange_and_mango = fruits_slice[1:3]
print("elementos de la posicon 1 al 2 (el end no lo toma)", orange_and_mango)

orange_mango_lemon = fruits_slice[1:4]
print("elementos de la posicon 1 al 3", orange_mango_lemon)

# here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
orange_and_lemon = fruits[::2]
print(orange_and_lemon)

print()

# modificar elementos
fruits_modify = ['banana', 'orange', 'mango', 'lemon']
fruits_modify[0] = "watermelon"
print(fruits_modify)

print()

# ver si un elemeto esta en la lista
is_in = "banana" in fruits_modify
is_in2 = "lemon" in fruits_modify
print(is_in)
print(is_in2)

print()

# append(element) --> añadir elementos al final de la lista
fruits_modify.append("pear")
print(fruits_modify)

print()

# insert(index,element) --> insertar elementos (util para ponerlo en la posicion q queramos)
fruits_modify.insert(3, "apple")
print(fruits_modify)

print()

# remover elementos de una lista

# remove() --> elimina un elemento especifica
fruits_remove = ['banana', 'orange', 'mango', 'lemon']
fruits_remove.remove("banana")
print(fruits_remove)

print()

# pop(index) --> elimina y retorna el elemento cuya posicion sea la misma q el index (si no le pones index elimina el ultimo)
ciudades = ['New York', 'Dallas', 'San Antonio', 'Houston', 'San Francisco']

print("Ciudad removida : ", ciudades.pop())
print("La ciudad en el indice 2 es : ", ciudades.pop(2))

print()

# del --> elimina el índice especificado y también se puede usar para eliminar elementos dentro del rango del índice. También puede eliminar la lista por completo.

fruits_del = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits_del[0]
print(fruits_del)

del fruits_del[1:3]
print(fruits_del)

print()

# clear()--> vacia una lista

lst_clear = ['item1', 'item2']
print(lst_clear.clear())

print()

# copy()--> copiar lista
'''
lista1 = [4,5,6]
lista2 = lista1 --> al hacer esto lista2 tiene la mismas referencia q lista1, por lo cual si modificamos lista2 tambien  lista 1
'''

lst_original = [4, 5, 6]

lst_copy = lst_original.copy()

print("lista original:", lst_original)
lst_copy.append("esta lista es la copia")
print("copia de la lista original:", lst_copy)

print()

# joining list: tenemos varias formas de concatenar 2 listas

# concatenar con +
lst1 = [4, 5, 6]
lst2 = [7, 8, 9]
lista3 = lst1 + lst2
print(lista3)

print()

# extend() --> te permite hacer append de una lista en otra

list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
print(list1)

print()

# count() --> devuelve el numero de veces q un elemento aparece en una lista

numeros = [4, 5, 8, 6, 2, 4, 5, 8, 4]
print(numeros.count(4))
print(numeros.count("4"))

print()

# index() --> retorna la posicion de un elemento en la lista

print(numeros.index(2))

print()

# reverse() --> invierte el orden de la lista
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)
print()

# sort()--> ordena la lista de menor a mayor o de mayor a menor si le pasas como argumento reverse=true
ages_unorderer = [22, 19, 24, 25, 26, 24, 25, 24]
ages_unorderer.sort()
print(ages_unorderer)

ages_unorderer.sort(reverse=True)
print(ages_unorderer)

print()


abcd = ["z", "a", "f", "b", "c", "g", "j", "g"]
abcd.sort()
print(abcd)

abcd.sort(reverse=True)
print(abcd)

print()


# sorted() --> retorna la lista ordenada pero sin modificar la orginal
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))

fruits = sorted(fruits, reverse=True)
print(fruits)

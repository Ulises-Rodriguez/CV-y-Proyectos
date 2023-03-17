# tuplas --> son una coleccion de elementos ordenados, pueden ser de distintos tipos pero no se las puede alterar

# metodos
'''
tuple() --> crea una tupla vacia
count() --> cuenta el numero de elemtos dentro de la tupla
index() --> encontrar el index de un elemento dentro de la tupla
'''

# crear tupla
tupla_vacia = ()
tupla_vacia2 = tuple()

# tupla con valores iniciles
tupla_con_items = (4, "hola", True)

# len con tuplas
print(len(tupla_con_items))
print()

# acceder a los elementos dentro de la tupla, al igual q las listas arrancan desde el 0
first = tupla_con_items[0]
last = tupla_con_items[int(len(tupla_con_items)-1)]
print("primer elemento:", first)
print("ultimo elemento:", last)
print("con numeros negativos:", tupla_con_items[-1])
print()

print()

# slice
fruits = ('banana', 'orange', 'mango', 'lemon')

print(fruits[0:3])
print(fruits[0:])
print()

# con valores negativos
print(fruits[-4:])
print(fruits[-3:-1])
print()

# cambiar tupla a lista
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)
print(lst)
print()

# ver si un elemento esta dentro de la tupla
print('orange' in fruits)
print()

# fruits[0] = 'apple' --> no xq los elemtnos de la tupla son inarterables

# join (unir 2 tuplas)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

print()

# eliminar la tupla --> no es posible remover un elemento en especifico pero si es posible toda la tupla
tpl1 = ('item1', 'item2', 'item3')
del tpl1
# print(tpl1) --> al borrarla si intentas imprimirla en consola te dice q no sabe lo q es

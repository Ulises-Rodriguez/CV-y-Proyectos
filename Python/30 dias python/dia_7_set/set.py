# set --> coleccion de elemtos no ordenados y por lo cual no indexado

# crear set
st = {}
st2 = set()

# crear set con elementos
st_values = {"manzana", "pera", 7, 5}
print(st_values)
print()

# len
print(len(st_values))
print()

# para acceder a los elementos usamos un loop
for element in st_values:
    print(element)
print()

# check si un elemento pertenece
print("manzana" in st_values)
print()

# agragar un elemento
st_add = {'item1', 'item2', 'item3', 'item4'}
st_add.add('item5')
print(st_add)
print()

# update() --> como add() pero te permite agregar multiples elementos al mismo tiempo
fruits = {'banana', 'orange', 'mango', 'lemon'}
# tambien lo podes poner entre {} o []
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)
print()

# remover elementos

# remove("item")
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.remove("orange")
print(fruits)

# pop() --> elimina un elemento al azar
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
# tambien podes guardar el elemto removido
# element_removed = fruits.pop()
print(fruits)
print()

# vaciar
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)
print()

# delete set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
# print(fruits)
print()

# convertir list --> set y set --> list
set_to_list = {4, 5.6, 5, 8}
list_to_set = ["a", "g", "j", "d"]

st = set(list_to_set)
lst = list(set_to_list)

print(st)
print(lst)
print()

# join --> tenemos union(),update()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)  # recorda q te lo va a imprimir en un orden aleatorio a los elementos
print()

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)
print(st3)
print()

# SE PUEDEN APLICAR CON LETRAS TANTO CON LETRAS COMO CON NUMEROS,ETC

# interseccion
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st_intersection = st1.intersection(st2)
print(st_intersection)
print()


# El issubset()método devuelve True si todos los elementos del conjunto existen en el conjunto especificado
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st1.issubset(st2))
print(st2.issubset(st1))  # st2 es subcojunto de st1 por lo cual devuelve true
print()

# El issuperset()método devuelve True si todos los elementos del conjunto especificado existen en el conjunto original
print(st1.issuperset(st2))
print(st2.issuperset(st1))

print()
# diferencias entre 2 set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))
# devuelve vacio xq no hay elementos q esten en even_numbers q no esten en whole_numbres
print(even_numbers.difference(whole_numbers))
print()

# (A\B) ∪ (B\A)
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.symmetric_difference(dragon))
print()


# disjoint sets --> If two sets do not have a common item or items
print(python.isdisjoint(dragon))

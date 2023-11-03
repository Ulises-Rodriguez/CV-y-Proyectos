# list --> crea una lista
lista = list(["Hola", 5, True])
print(lista)

# es menos raros hacer esto
lista = ["Hola", 5, True, "Juan", "Facu", 45, 684]
print(lista)


# len --> cuenta la cantidad de elementos de la lista
print(len(lista))

# append --> agrega un elemento a la lista al final
lista.append("valor_append")
print(lista)

# insert --> agrega un elemento a la lista en la posicion especificada
lista.insert(1, "valor_insert")
print(lista)

# extend --> agraga varios elementos a la lista
lista.extend(["extend1", "extend2", False])
print(lista)

# pop --> elimina un elemento de la lista, pide indice y te devuelve el valor eliminado
elem_eliminado = lista.pop(0)
print(elem_eliminado)

# al poner -1 eliminas el ultimo elemento de la lista
elem_eliminado = lista.pop(-1)
print(elem_eliminado)

# al poner -1 eliminas el anteultimo elemento de la lista
elem_eliminado = lista.pop(-2)
print(elem_eliminado)


# reomve --> remueve un elemento de la lista, pide valor
# lista.remove("jkl")  # al no encontrarlo no elimina nada y tira una excepcion
# print(lista)
lista.remove(45)
print(lista)

# clear --> remueve todos los elementos de la lista
lista2 = ["j", 4, 78]
lista2.clear()
print(lista2)

# sort --> ordena los elementos de la lista
# no pode combinar letras con nums pero si true y false ya q estos 2 se pueden escribir tambien como 1 y 0
lista3 = [45, 78, 5, 7, 0, True]
lista3.sort()
print(lista3)

l = ["a", "z", "j"]
l.sort()
print(l)

l = ["a", "z", "j"]
l.sort(reverse=True)  # los ordena pero al reves
print(l)

# reverse --> invierte los elementos de la lista
lista3.reverse()  # l.sort(reverse=True) y .reverse() no es lo mismo reverse no ordena solo invierte los elementos
print(lista3)

conjunto = set(["dato 1", "dato 2"])

print(conjunto)

# otro dato de los conjuntos es q sus elementos no pueden mutar osea cambiarlos, por eso no se le puede pasar cosas como una lista ya q estas si pueden cambiar

# conjunto = set(["dato 1", "dato 2", ["dato lista 1", "dato lista 2"]]) esto da error ya q la lista es unhasable osea q es un elemento q se puede modificar

# pero si podes pasar una tupla ya q estas no se modificarn
conjunto = set(["dato 1", "dato 2", ("dato lista 1", "dato lista 2")])

print(conjunto)

# metiendo un conjunto dentro de otro conjunto tengo q usar la funcion "frozenset"
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = set([conjunto1, "dato 4"])

print(conjunto2)

# para ver si un conjunto es subconjunto de otro
conj1 = {1, 3, 7, 9}
conj2 = {1, 3, 9}

res = conj2.issubset(conj1)
print(res)

# otra forma es con el <=

res = conj2 <= conj1
print(res)

# para ver si es un superconjunto
conj1 = {1, 3, 7, 9}
conj2 = {1, 3, 9}

res = conj2.issuperset(conj1)
print(res)

# aca tiene q ser >
res = conj2 > conj1
print(res)


# ahora si queremos ver si hay algun elemento del conj2 dentro del conj1
res = conj2.isdisjoint(conj1)
print(res)  # devuelve false ya q .isdisjoint() solo devuelve true cuando los conjuntos q se estan comparando no tienen ningun numero igual

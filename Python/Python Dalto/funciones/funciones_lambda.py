# es medio como una funcion flecha en JS

# lambda es una funcion anonima, osea no tiene nombre
# son utiles cuando tenes  q hacer una sola intruccion
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

impares = filter(lambda x: x % 2 == 0, lista)

# si no le pones list te devuelve un objeto filter
print(list(impares))

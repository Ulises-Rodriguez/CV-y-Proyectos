# tuple es un forma de crear tuplas, para indicar los datos q va a tener es necesario pasarle una lista
tupla = tuple(["dato 1", "dato 2"])

print(tupla)

# la otra forma de crear las tuplas

tupla = "dato 1", "dato 2"

print(tupla)

# q es lo mismo q hacer

tupla = ("dato 1", "dato 2")

print(tupla)

# ahora si queres crear una tupla con un solo dato lo q haces es poner una , al final
tupla = "dato 1",

print(tupla)

# las tuplas podemos crearlas en casos como elementos de solo lectura ya q al no poder modificar los datos dentro de la tupla estas se manejan mejor en la memoria q las listas ya q estas guardan 2 lugares en memoria con la misma lista, una en la q modificarn primero y una ves esta se modifica cambian la otra (es como si se guardaran 2 listas y se modifica una para comprobar q esta todo bien y luego se modifica la original)

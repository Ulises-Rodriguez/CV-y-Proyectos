import pandas as pd
print(type(pd))

# df --> data frame son estructuras de datos bidimencionales similares a una hoja de calculo
# la forma de organizar los datos son 2 filas y columnas
# con names podemos agregar encabezados en ves de tener q ponerlos de forma manueal nosotros en el .csv
# df = pd.read_csv("archivos\\csv_prueba.csv", names=["name", "lastName", "age"])
# print(df)

# print()
# nombres = df["name"]
# print(nombres)

# lo ideal para trabajar con ciencias de datos es usar jupiter
# ctr+shit+p --> jupiter nootbook

print()

# esto es slicin q es una forma de cortar una array, [indicando donde comienza : indica donde termina]
cadena = "0123456789"

# te devuelve todo
print(cadena[:])
# empieza desde la posicion 0 hasta la 5 pero sin incluir esta ultima osea un intervalor 0a4
print(cadena[0:5])
# por defecto empieza en 0 y termina en 6
print(cadena[:6])
# empieza en 6 y termina en el ultimo elemento
print(cadena[6:])
# inicia de posicion 2 y termina en 6 sin incluir
print(cadena[2:6])

print()
print()
# ahora q pasa si quiero ordenar los datos del .csv por edad
df = pd.read_csv("archivos\\csv_prueba.csv")

df_ordenado_edad = df.sort_values("edad")
print(df_ordenado_edad)

print()

# ordenando de mayor a menor
df_ordenado_edad = df.sort_values("edad", ascending=False)
print(df_ordenado_edad)

print()

# concatenar df
df = pd.read_csv("archivos\\csv_prueba.csv")
df2 = pd.read_csv("archivos\\csv_prueba.csv")

# usando pandas y le pasas una lista
df_concat = pd.concat([df, df2])
print(df_concat)

print()

# head y tail --> te permiten acceder a la primera o ultima fila
# el valor q le pases es la cantidad de filas q te va a mostrar
primeras_filas = df.head(2)
print(primeras_filas)
print()

ultimas_filas = df.tail(2)
print(ultimas_filas)
print()

# accediendo a la cantidad de filas y columnas
f_c = df.shape
print(f_c)
print()

# obteniendo data estadistica del df
df_info = df.describe()
print(df_info)
print()

# accediendo a un elemento especifico del df con loc
elem_especifico_loc = df.loc[2, "edad"]
print(elem_especifico_loc)

# idem pero con indices
elem_especifico_loc = df.iloc[2, 2]
print(elem_especifico_loc)
print()

# accediendo a todas las filas de una columna
# esto seria como posiciones x,y --> df.iloc[0:(0, 1)]
apellidos = df.iloc[:, 1]
print(apellidos)
print()

# accediendo a filas con edad mayor q 30
# las filas solo las q son > 30 : las comlumnas todas
mayor_30 = df.loc[df["edad"] > 30, :]
print(mayor_30)
print()

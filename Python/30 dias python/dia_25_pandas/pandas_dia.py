# Pandas
'''
Pandas es una estructura de datos y herramientas de análisis de datos de código abierto, alto rendimiento y fácil de usar para el lenguaje de programación Python. Pandas agrega estructuras de datos y herramientas diseñadas para trabajar con datos similares a tablas, que son Series y Data Frames. Pandas proporciona herramientas para la manipulación de datos:

reorganización
fusionando
clasificación
rebanar
agregación
imputación Si está utilizando anaconda, no tiene que instalar pandas.

Una serie es una columna y un DataFrame es una tabla multidimensional compuesta por una colección de series. Para crear una serie de pandas, debemos usar numpy para crear matrices unidimensionales o una lista de python. Veamos un ejemplo de una serie:
'''
import numpy as np
import pandas as pd


# Series
# crear una seria con pandas
nums = [1, 2, 3, 4, 5, 6, 7]
s = pd.Series(nums)
print(s)
print()

fruits = ['Orange', 'Banana', 'Mango']
# para modificar el indice usas index
fruits = pd.Series(fruits, index=[1, 2, 555])
print(fruits)
print()

# crear una serie pandas con un dict
dct = {
    "nombre": "Tino",
    "comida": "Machichita",
    "edad": 10,
}

s = pd.Series(dct)
print(s)
print()


# crear constantes con pandas
s = pd.Series(10, index=[1, 2, 3])
print(s)
print()


# crear una serie usando linespace
s = pd.Series(np.linspace(5, 20, 10))
print(s)
print()


# DataFrames
# con listas
data = [
    ["Tino", 10],
    ["Ulises", 25],
    ["Juan", 25],
]
df = pd.DataFrame(data, columns=["nombre", "edad"])
print(df)
print()

# con dict
data = {"nombre": ["Tino", "Uli", "Juan"], "edad": [10, 25, 25]}
df = pd.DataFrame(data)
print(df)
print()

# con lista de dicts
data = [
    {"nombre": "Tino", "edad": 10},
    {"nombre": "Uli", "edad": 25},
    {"nombre": "Juan", "edad": 25},
]
df = pd.DataFrame(data)
print(df)
print()

# leer un csv file
df = pd.read_csv("30 dias python\dia_25_pandas\weight-height.csv")
# print(df.to_string())  # lee todo el archivo
# print()
print(df.head())  # lee solo las primeras 5 filas
print()
print(df.tail())  # lee solo las ultimas 5 filas
print()
print(df.shape)  # nos permite saber la cantidad de filas y columnas
print()
print(df.columns)  # nos obtiene las columnas
print()
# obtener una columna especifica
heights = df["Height"]
print(heights)
print()
weights = df['Weight']
print(weights)
print()
print(len(heights) == len(weights))
print()
print(heights.describe())  # nos da todos los valores de estadisticas
print()
print(weights.describe())
print()
print(df.describe())
print()


# modificar dataframes
data = [
    {"nombre": "Tino", "edad": 10},
    {"nombre": "Uli", "edad": 25},
    {"nombre": "Juan", "edad": 25},
]
df = pd.DataFrame(data)
print(df)
print()

# añadir una columna
weights = [10, 60, 69]
df['Weight'] = weights
print(df)
print()

heights = [20, 184, 182]
df['Height'] = heights
print(df)
print()

# modificar una columna
df['Height'] = df['Height'] * 0.01
print(df)
print()


# lo mismo pero dentro de una fincion para hacerlo mas limpio
def modificaciones():
    weights = df["Weight"]
    heights = df["Height"]
    indice_de_masa_corporal = []

    for w, h in zip(weights, heights):
        b = w/(h*h)
        indice_de_masa_corporal.append(b)

    return indice_de_masa_corporal


indice_masa_corporal = modificaciones()

df["bmi"] = indice_masa_corporal
print(df)
print()

# formatear columna bmi a solo un numero depues de la ,
df["bmi"] = round(df["bmi"], 1)
print(df)
print()

# añadimos algunos datos mas
color = ["negro", "rojo", "azul"]
year = pd.Series(2022, index=[0, 1, 2])
color_serie = pd.Series(color)
# print(color_serie)
df["color"] = color_serie
df["year"] = year
print(df)
print()

# check data type
print(df.Weight.dtype)
print()
# it gives string object , we should change this to number
print(df['year'].dtype)
print()
df['year'] = df['year'].astype('int')
print(df['year'].dtype)  # let's check the data type now
print()

# tambien podemos restar una columna con otra (con el mismo tipo osea no le restes un numero a una letra XD)
dif = df["Weight"] - df["edad"]
print(dif)
print()

# bool index
print(df[df["edad"] > 20])
print()

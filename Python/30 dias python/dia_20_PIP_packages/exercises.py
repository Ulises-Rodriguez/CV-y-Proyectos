import pandas as pd
import requests
from collections import Counter
import numpy as np
# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

res = requests.get(romeo_and_juliet)

# split_it = res.text.split()

# # print(split_it)


# count = Counter(split_it)

# print(count)


def most_common_words(text):
    split_it = text.split()
    Cnter = Counter(split_it).most_common(4)
    # Cnter.sort(reverse=True)
    return Cnter[:10]


# print(most_common_words(res.text))


# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# 1_the min, max, mean, median, standard deviation of cats' weight in metric units.
# 2_the min, max, mean, median, standard deviation of cats' lifespan in years.
# 3_Create a frequency table of country and breed of cats


url = "https://api.thecatapi.com/v1/breeds"
res = requests.get(url)
cats = res.json()


def get_metic_values(lst):
    lst_aux = []

    for cat in range(len(lst)):
        # print(type(cats[cat]["weight"]["metric"]))
        aux = lst[cat]["weight"]["metric"].split(" - ")
        # print()
        num1 = aux[0]
        num2 = aux[1]
        lst_aux.append(int(num1))
        lst_aux.append(int(num2))

    return lst_aux


def get_life_span(lst):
    lst_aux = []

    for cat in range(len(lst)):
        aux = lst[cat]["life_span"].split(" - ")
        num1 = aux[0]
        num2 = aux[1]
        lst_aux.append(int(num1))
        lst_aux.append(int(num2))

    return lst_aux


def info(cats, f):
    min = 0
    max = 0
    promedio = 0
    mediana = 0
    desvio_estandar = 0

    lst = f(cats)

    min = np.min(lst)
    max = np.max(lst)
    promedio = np.mean(lst)
    mediana = np.median(lst)
    desvio_estandar = np.std(lst)

    print("min = {}, max = {}, mean = {}, median = {}, sd = {}".format(
        min, max, promedio, mediana, desvio_estandar))


# info(cats, get_metic_values)
# info(cats, get_life_span)


def get_country_breed(lst):
    lst_aux_country = []
    lst_aux_breed = []

    aux = []

    for cat in range(len(lst)):
        country = lst[cat]["origin"]
        breed = lst[cat]["name"]
        lst_aux_country.append(country)
        lst_aux_breed.append(breed)

    aux.append(lst_aux_breed)
    aux.append(lst_aux_country)

    return aux


def frequency_table(lst):

    aux = get_country_breed(lst)

    breed = aux[0]
    country = aux[1]

    aux2 = pd.DataFrame({"breed": breed,
                         "country": country})

    # aux = pd.DataFrame({'    Grado': ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'D', 'D'],
    #                     '    Edad': [18, 18, 18, 19, 19, 20, 18, 18, 19, 19],
    #                     '    Género': ['M', 'M', 'F', 'F', 'F', 'M', 'M', 'F', 'M', 'F']})

    # print(aux)

    print(aux2.to_string())  # el to_string() es xq pandas por defecto solo muestra las primeras 10 filas --> solucion : https://www.geeksforgeeks.org/how-to-display-all-rows-from-dataframe-using-pandas/


frequency_table(cats)


url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
print(response.headers)
print(response.text)

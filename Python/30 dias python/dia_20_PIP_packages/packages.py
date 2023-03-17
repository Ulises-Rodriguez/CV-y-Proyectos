from my_packages.saludo import saludo_persona

import requests
import webbrowser
import pandas
import numpy
import webbrowser

print(saludo_persona("Ulises", "Rodriguez"))

'''
NumPy es el paquete fundamental para la computación científica con Python. Contiene entre otras cosas:
    un poderoso objeto de matriz N-dimensional
    funciones sofisticadas (de radiodifusión)
    herramientas para integrar código C/C++ y Fortran
    útiles capacidades de álgebra lineal, transformada de Fourier y números aleatorios

Pandas es una biblioteca de código abierto con licencia BSD que proporciona estructuras de datos y herramientas de análisis de datos fáciles de usar y de alto rendimiento para el lenguaje de programación Python.

webbrowser --> módulo de navegador web, que puede ayudarnos a abrir cualquier sitio web. No necesitamos instalar este módulo, ya está instalado de forma predeterminada con Python 3. Por ejemplo, si desea abrir una cantidad de sitios web en cualquier momento o si desea programar algo, puede usar este módulo de navegador web.

Reading from URL --> A estas alturas ya está familiarizado con la forma de leer o escribir en un archivo ubicado en su máquina local. A veces, nos gustaría leer desde un sitio web usando url o desde una API. API significa interfaz de programa de aplicación. Es un medio para intercambiar datos estructurados entre servidores principalmente como datos json. Para abrir una conexión de red, necesitamos un paquete llamado requests: permite abrir una conexión de red e implementar operaciones CRUD (crear, leer, actualizar y eliminar).

    get(): to open a network and fetch data from url - it returns a response object
    status_code: After we fetched data, we can check the status of the operation (success, error, etc)
    headers: To check the header types
    text: to extract the text from the fetched response object
    json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

package --> un modulo puede contener varias funciones,clases,objeots,etc, ahora un package puede contener varios modulos
            Vamos a crear un paquete llamado mypackage, usando los siguientes pasos:

            Cree una nueva carpeta llamada mypackage dentro de la carpeta 30DaysOfPython. Cree un archivo init.py vacío en la carpeta mypackage. Cree los módulos aritmetic.py y greeting.py con el siguiente código:
'''

lst = [1, 5, 9, 6, 3]

np_arr = numpy.array(lst)

print(np_arr)
print(len(np_arr))
print(np_arr + 2)
print(np_arr * 2)


# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)

# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
# response = requests.get(url)
# print(response.status_code)
# print(response.headers)
# print(response.text)


# la pagina esta caida asi q no va andar pero es para q se vea la idea de como hacer con json
# url = 'https://restcountries.eu/rest/v2/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# print(response)  # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# # we sliced only the first country, remove the slicing to see all countries
# print(countries[:1])

'''
<Response [200]>
200
[{'alpha2Code': 'AF',
  'alpha3Code': 'AFG',
  'altSpellings': ['AF', 'Afġānistān'],
  'area': 652230.0,
  'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'],
  'callingCodes': ['93'],
  'capital': 'Kabul',
  'cioc': 'AFG',
  'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '؋'}],
  'demonym': 'Afghan',
  'flag': 'https://restcountries.eu/data/afg.svg',
  'gini': 27.8,
  'languages': [{'iso639_1': 'ps',
                 'iso639_2': 'pus',
                 'name': 'Pashto',
                 'nativeName': 'پښتو'},
                {'iso639_1': 'uz',
                 'iso639_2': 'uzb',
                 'name': 'Uzbek',
                 'nativeName': 'Oʻzbek'},
                {'iso639_1': 'tk',
                 'iso639_2': 'tuk',
                 'name': 'Turkmen',
                 'nativeName': 'Türkmen'}],
  'latlng': [33.0, 65.0],
  'name': 'Afghanistan',
  'nativeName': 'افغانستان',
  'numericCode': '004',
  'population': 27657145,
  'region': 'Asia',
  'regionalBlocs': [{'acronym': 'SAARC',
                     'name': 'South Asian Association for Regional Cooperation',
                     'otherAcronyms': [],
                     'otherNames': []}],
  'subregion': 'Southern Asia',
  'timezones': ['UTC+04:30'],
  'topLevelDomain': ['.af'],
  'translations': {'br': 'Afeganistão',
                   'de': 'Afghanistan',
                   'es': 'Afganistán',
                   'fa': 'افغانستان',
                   'fr': 'Afghanistan',
                   'hr': 'Afganistan',
                   'it': 'Afghanistan',
                   'ja': 'アフガニスタン',
                   'nl': 'Afghanistan',
                   'pt': 'Afeganistão'}}]
'''

# Usamos el método json() del objeto de respuesta, si estamos obteniendo datos JSON. Para txt, html, xml y otros formatos de archivo podemos usar texto.

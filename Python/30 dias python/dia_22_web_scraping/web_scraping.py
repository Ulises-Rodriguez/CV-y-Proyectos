# Web Scraping
'''
web scraping es el proceso de extraer y recolectar data de las web y almacenarla en database o data local
'''

import requests
from bs4 import BeautifulSoup

# BeutifulSoup para analizar los datos obtenidos de la pagina
url = 'https://archive.ics.uci.edu/ml/datasets.php'


response = requests.get(url)
content = response.content  # obtener todo el contenido de la pagina
# beutiful soup da chance de analizar
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)  # obtiene la etiqueta title
print()
print(soup.title.get_text())  # obtiene el contenido de la etiqueta title
print()
print(soup.body)  # nos da todo el contenido de la pagina
print()

# Estamos apuntando a la tabla con el atributo cellpadding con el valor de 3
tables = soup.find_all("table", {"cellpadding": "3"})

# Podemos seleccionar usando id, clase o etiqueta HTML
table = tables[0]
for td in table.find("tr").find_all("td"):
    print(td.text)

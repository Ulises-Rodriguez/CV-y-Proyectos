import json
import requests
from bs4 import BeautifulSoup

url = "https://www.bu.edu/president/boston-university-facts-stats/"

res = requests.get(url)

soup = BeautifulSoup(res.content, "html.parser")
head = soup.head
body = soup.body

array_aux = []


def convert_dict_head():
    id = 0
    head_dict = {}

    for i in head.find_all("style"):
        head_dict["style_{}".format(id)] = i
        id += 1

    for i in head.find_all("link"):
        head_dict["link_{}".format(id)] = i
        id += 1

    for i in head.find_all("meta"):
        head_dict["meta_{}".format(id)] = i
        id += 1

    for i in head.find_all("script"):
        head_dict["script_{}".format(id)] = i
        id += 1

    array_aux.append(head_dict)

    return str(array_aux)


def convert_dict_body():
    id = 0
    body_dict = {}

    for i in body.find_all("header"):
        body_dict["header_body_{}".format(id)] = i
        id += 1

    for i in body.find_all("div", {"class": "wrapper"}):
        body_dict["wrapper_body_{}".format(id)] = i
        id += 1

    for i in body.find_all("footer"):
        body_dict["footer_body_{}".format(id)] = i
        id += 1

    for i in body.find_all("script"):
        body_dict["script_body_{}".format(id)] = i
        id += 1

    array_aux.append(body_dict)

    return str(array_aux)


# with open("30 dias python\dia_22_web_scraping\exercise1.json", "w", encoding="utf-8") as f:

#     aux1 = convert_dict_head()
#     aux2 = convert_dict_body()

#     # data = {"header": aux1, "body": aux2}
#     data = [{"header": aux1}, {"body": aux2}]

#     json.dump(data, f, ensure_ascii=False, indent=4)

#     # txt = json.load(f)
#     # print(txt)


# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

url2 = "https://archive.ics.uci.edu/ml/datasets.php"

res2 = requests.get(url2)
soup2 = BeautifulSoup(res2.content, "html.parser")

tables = soup2.find_all("table")


def convert_table_json():
    table_dict = {}

    table_dict['table_0'] = str(tables[0])
    table_dict['table_1'] = str(tables[1])
    table_dict['table_2'] = str(tables[len(tables)-1])

    return table_dict


# with open("30 dias python\dia_22_web_scraping\exercise2.json", "w", encoding="utf-8") as f:
#     aux = convert_table_json()
#     data = [aux]

#     json.dump(data, f, ensure_ascii=False, indent=4)


# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

url3 = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

res3 = requests.get(url3)
soup3 = BeautifulSoup(res3.content, "html.parser")


def president_table():
    aux = {}
    aux["president_table"] = soup3.find(
        "table", {"class": "wikitable"})

    return aux


with open("30 dias python\dia_22_web_scraping\exercises3.json", "w", encoding="utf-8") as f:

    aux = soup3.find(
        "table", {"class": "wikitable"})

    data = {
        "president_table": "{}".format(aux)
    }

    json.dump(data, f, ensure_ascii=False, indent=4)

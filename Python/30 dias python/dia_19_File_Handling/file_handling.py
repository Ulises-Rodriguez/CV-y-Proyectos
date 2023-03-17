# File Handling

# open("filename",flags) --> nos permite abrir y obtener datos de un archivo
# dependiendo de q flags usemos podemos hacer varias cosas
'''
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

Flags:
"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

# abriendo un archivo de .txt
# por defecto el falg es w
import xml.etree.ElementTree as ET
import csv
import json
import os
f = open("30 dias Python/dia_19_File_Handling/texto.txt")
print(f)
print()

# para poder ver el contenido
txt = f.read()
print(txt)

# cuando abrimos un archivo hay q recordar de cerrarlo una ves terminemos de usarlo
f.close()
print()


# ahora imagina q solo te interasan las primeras 10 caracteres del del .txt
f = open("30 dias Python/dia_19_File_Handling/texto.txt")
txt = f.read(10)
print(txt)
f.close()
print()

# readline --> lee la primera linea del .txt
f = open("30 dias Python/dia_19_File_Handling/texto.txt")
txt = f.readline()
print(txt)
f.close()
print()

# readlines --> lee todas las lineas del .txt
f = open("30 dias Python/dia_19_File_Handling/texto.txt")
txt = f.readlines()
print(txt)
f.close()
print()

# splitlines --> otra forma de leer todo el contenido
f = open("30 dias Python/dia_19_File_Handling/texto.txt")
txt = f.read().splitlines()
print(txt)
f.close()
print()


# with --> nos permite hacer un open() y no preocuparnos por cerrarlo ya q with se encarga
with open("30 dias Python/dia_19_File_Handling/texto.txt") as f:
    txt = f.read().splitlines()
    print(txt)
print()


# abrir y escribir en los archivos
# "a" lo q escribas se añade al final del archivo txt abierto
with open("30 dias Python/dia_19_File_Handling/texto.txt", "a") as f:
    f.write("Texto q se agrega al final")

with open("30 dias Python/dia_19_File_Handling/texto.txt") as f:
    txt = f.read()
    print(txt)

print()

# "w" --> si no encuentra archivo indicado, este crea uno nuevo con ese nombre
# si encuentra un archivo con el nombre indicado "w" sobreescribe todo el contenido original
with open("30 dias Python/dia_19_File_Handling/writing_file.txt", "w") as f:
    f.write("Texto q se agregado en el archivo creado")


with open("30 dias Python/dia_19_File_Handling/writing_file.txt") as f:
    txt = f.read()
    print(txt)


# para eliminar un archivo usamos el modulo os

# acordate de crear una archivo para el ejem XD
# os.remove tira error si no encuentra el archivo por eso lo ideal es usar condicionales para comprobar si el archivo existe antes de intentar eliminarlo
if os.path.exists("30 dias Python/dia_19_File_Handling/example.txt"):
    os.remove("30 dias Python/dia_19_File_Handling/example.txt")
else:
    print("el archivo no existe")


# File Types
'''
.txt --> archivo super comun, es texto plano 

.json --> Los JSON son cadenas - útiles cuando se quiere transmitir datos a través de una red. Debe ser convertido a un objeto nativo de JavaScript cuando se requiera acceder a sus datos. Ésto no es un problema, dado que JavaScript posee un objeto global JSON que tiene los métodos disponibles para convertir entre ellos

    # dictionary
    person_dct= {
        "name":"Asabeneh",
        "country":"Finland",
        "city":"Helsinki",
        "skills":["JavaScrip", "React","Python"]
    }
    # JSON: A string form a dictionary
    person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

    # we use three quotes and make it multiple line to make it more readable
    person_json = {
        "name":"Asabeneh",
        "country":"Finland",
        "city":"Helsinki",
        "skills":["JavaScrip", "React","Python"]
}


.csv --> CSV significa valores separados por comas. CSV es un formato de archivo simple que se utiliza para almacenar datos tabulares, como una hoja de cálculo o una base de datos. CSV es un formato de datos muy común en la ciencia de datos.

    "name","country","city","skills"
    "Asabeneh","Finland","Helsinki","JavaScript"

.xlsx --> para leer archivos excel

.xml --> XML es otro formato de datos estructurados que se parece a HTML. En XML, las etiquetas no están predefinidas. La primera línea es una declaración XML. La etiqueta de persona es la raíz del XML. La persona tiene un atributo de género.

    <?xml version="1.0"?>
    <person gender="female">
    <name>Asabeneh</name>
    <country>Finland</country>
    <city>Helsinki</city>
    <skills>
        <skill>JavaScrip</skill>
        <skill>React</skill>
        <skill>Python</skill>
    </skills>
    </person>
'''

# cambiar json a diccionario --> usamos el modulo json

# esto lo ideal es q este en el servidor o en un txt aparte
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

persona_dict = json.loads(person_json)
print(type(persona_dict))
print(persona_dict)
print(persona_dict["name"])

# cambiar de dict a json
# La función json.dumps() convertirá un subconjunto de objetos Python en una cadena json. No todos los objetos son convertibles y es posible que deba crear un diccionario de datos que desee exponer antes de serializar a JSON.
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

persona_json = json.dumps(person)
# indent es la cantidad de espacio q deja entre cada par clave : valor
persona_json2 = json.dumps(person, indent=2)
persona_json4 = json.dumps(person, indent=4)
persona_json8 = json.dumps(person, indent=8)

print(type(persona_json))
print(persona_json)
print()
print(persona_json2)
print()
print(persona_json4)
print()
print(persona_json8)
print()

# Saving as JSON File
# para esto usamos json.dump()

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

with open("30 dias Python/dia_19_File_Handling/example_json.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

print()

# File with csv Extension --> modulo csv

with open("30 dias Python/dia_19_File_Handling/example_csv.csv") as f:
    csv_reader = csv.reader(f, delimiter=",")
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

print()

# File with xlsx Extension --> modulo xlrd

# import xlrd --> tira problemas como q no lo reconoce, pandas puede servir tambien (https://stackoverflow.com/questions/3239207/how-can-i-open-an-excel-file-in-python)
# excel_book = xlrd.open_workbook('sample.xls)
# print(excel_book.nsheets)
# print(excel_book.sheet_names)


# File with xml Extension --> modulo xml --> documentacion : https://docs.python.org/2/library/xml.etree.elementtree.html
tree = ET.parse("30 dias Python/dia_19_File_Handling/example_xml.xml")
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)

for child in root:
    print('field: ', child.tag)

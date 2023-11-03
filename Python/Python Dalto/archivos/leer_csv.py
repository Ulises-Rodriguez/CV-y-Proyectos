import csv

with open("archivos\\csv_prueba.csv") as archivo_csv:
    print(csv.reader(archivo_csv))

with open("archivos\\csv_prueba.csv") as archivo_csv:
    reader = csv.reader(archivo_csv)
    for row in reader:
        print(row)

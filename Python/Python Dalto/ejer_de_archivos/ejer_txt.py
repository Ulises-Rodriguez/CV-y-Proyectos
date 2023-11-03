# tenemos 2 listas una con nombres y otra con apellidos, tenemos q escribir los datos en un archivo de texto de forma optima con un for

nombres = ["Tino", "Juanchis", "Martincho", "Teitun", "ElPampa"]
apellidos = ["Machichita", "ElMagicina", "Lenox", "Donger", "ScoutMaster"]

with open("ejer_de_archivos\\nombre_apellido.txt", "w") as archivo:

    # archivo.writelines(["Nombre", "---Apellido\n"])

    # for i in range(len(nombres)):
    #     nombre_apellido = f"{nombres[i]} ---> {apellidos[i]}\n"
    #     archivo.write(nombre_apellido)

    # for tupla in zip(nombres, apellidos):
    #     nombre, apellido = tupla
    #     nombre_completo = f"{nombre}---{apellido}\n"
    #     archivo.write(nombre_completo)

    archivo.writelines("Los datos son: \n\n")

    [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n-------------\n")
     for n, a in zip(nombres, apellidos)]

'''
w --> reescribe el contenido del archivo o te crea un archivo nuevo si no lo encuentra
a --> escribe al final de la linea lo q le pases pero te mantiene el contenido previo
r --> es el valor por defecto y es para lectura
'''

with open("archivos\\texto1.txt", "a") as archivo:
    # archivo.write("lo q quieras escribir, pero ojo xq estas reescribiendo todo el contenido del archivo")
    # archivo.write("Hola pibe todo bien?")

    # pasarle un array es lo mismo q hacer 2 o mas .writelines seguidos
    # el \n es para hacer un salto de linea
    archivo.writelines(["Hola pibe todo bien?\n", "nada maquinola todo tanki"])

    # tabajando con un for
    for i in range(5):
        archivo.writelines(f"agrego linea {i}\n")

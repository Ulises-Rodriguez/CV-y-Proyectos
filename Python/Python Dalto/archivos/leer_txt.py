# open para abrir el archivo
# por defecto open esta en read --> "r" (no hace falta ponerlo)
# el encoding="UTF-8" es por el tema de codificacion q lee todos los caracteres (depende el sistema operativo)
archivo_sin_leer = open("archivos\\texto", "r", encoding="UTF-8")

# con .read() lees el contenido del .txt
archivo_leido = archivo_sin_leer.read()
print(archivo_leido)

archivo_sin_leer.close()

print()
print()
print()

'''
Como dato con alt+shift cambias el idioma del teclado (por si llegas a necesitar cambiar los caracteres del teclado y ahorrate el laburo de ir a la configuracion)
'''

# si un archivo se lee 1 ves ya no se puede leer otra ves hasta q lo cierres y lo vuelvas a abrir
archivo_sin_leer = open("archivos\\texto", "r", encoding="UTF-8")

# .readlines() te devuelve un array con todas las lineas
lineas = archivo_sin_leer.readlines()
print(lineas)

archivo_sin_leer.close()

print()
print()
print()

archivo_sin_leer = open("archivos\\texto", "r", encoding="UTF-8")

# .readline() te sirve para leer una linea en especifico
# si le pasas un numero esto te lee esas cantidad de caracteres
lineas = archivo_sin_leer.readline(2)
print(lineas)

archivo_sin_leer.close()

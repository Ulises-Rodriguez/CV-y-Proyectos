cadena1 = "Tino"
cadena2 = "Queres tomar mate?"

# dir --> devuelve todos los atributos de un objeto
print(dir(cadena1))  # te devuelve los metodos q podes aplicarle al objeto
print(dir(4))
print(dir(["jkl", 32, True]))

# upper, lower, capitalize

# todo mayusculas
# fijate q hay una diferencia, dir() es una funcion mientras q .upper() es un metodo, osea va seguido al objeto q queramos aplicarlo
print(cadena1.upper())

# todo minusculas
print(cadena1.lower())

# primera letra en mayusculas el resto en minusculas
print(cadena1.capitalize())
print("alo WAChIn".capitalize())

# find --> encuentra la primera aparicion del valor pasado, en caso contrario devuelve -1
res = cadena1.find("ino")
print(res)
res = cadena1.find("O")
print(res)

# index --> encuentra la primera aparicion del valor pasado, en caso contrario devuelve una excepcion
# print(cadena1.index(cadena2))
print(cadena1.find("T"))

# isnumeric --> si es numerico devuelve true
print(cadena1.isnumeric())
# a pesar de q aca el 456 es un string el .isnumeric() revisa si es un numero
print("456".isnumeric())

# isalpha --> si hay solo caracteres de la a-z o A-Z devuelve true
print(cadena1.isalpha())
print("Hola todo bien?".isalpha())

# count --> cuenta la cantidad de ocurrencias de una cadena en otra
print(cadena1.count(cadena2))
print(cadena2.count("a"))

# len --> cuenta los caracteres en una cadena
print(len(cadena2))

# startwidth --> verifica si la cadena comienza con
print(cadena2.startswith("Que"))
print(cadena2.startswith("ue"))

# endswidth --> verifica si la cadena termina con
print(cadena2.endswith("ue"))
print(cadena2.endswith("ate?"))

# replace --> remplaza un valor por otro
# el primer valor es lo q busca y el sugundo valor es el con el q va a reemplzar al primero en caso de encontrarlo
cadena_nueva = cadena2.replace("Que", "Tino")
print(cadena_nueva)
# recorda q py es sensible a mayusculas y minusculas, entonces al no encontrar "que" en cadena2 replace te devuelve la cadena original
cadena_nueva = cadena2.replace("que", "Tino")
print(cadena_nueva)

# split --> parte una cadena por el valor dado y el resultado lo convierte en lista
cadena_lista = cadena2.split()  # por defecto es el espacio
print(cadena_lista)

# te lo separa en partes donde encuentre en este caso el #
cadena_lista = "Hola#Todo#Bien".split("#")
print(cadena_lista)

# si a split le pasas un valor numerico le indicas el numero de elemento maximos q queres separar
cadena_lista = "Hola#Todo#Bien".split("#", 1)
print(cadena_lista)

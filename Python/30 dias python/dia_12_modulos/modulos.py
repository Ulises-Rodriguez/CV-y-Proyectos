# modulos
# un modulo es un archivo q contine una parte de codigo q puede ser incluido en la aplicacion
# estos modulos pueden ser desde una variable, funcion o codigo mucho mas complejo

# para poder usar el modulo se usa la palbra clave import + el nombre del modulo (no hace falta poner .py)
# cuidado con el auto completar q te puede dar mas problemas q ayudas
# import mymodule

# 1) importar solo cierta parte del modulo
from mymodule import suma as add
# 2) imporatar funciones y renombrarlas (as)
from mymodule import full_name
# 3) imporatando bultin_modulos --> crear o cambiar el directorio de trabajo actual
import os
# 4) sys modulo --> funciones y variables para manipular path
# Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.
import sys
# 5) The statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: mean, median, mode, stdev etc.
from statistics import *  # con esto imporatas todo
# 6) math --> opraciones matematicas --> sumatorias,pi potencias,etc
# from math import pi, sqrt, pow, floor, ceil, log10 --> podes importar muchas funciones a la ves
import math
# 7) random genera numeros random
import random
# 8) string
import string

# 1
print(full_name("Tino", "Rodriguez"))
print()

# 2
print(add(5, 4))
print()

# 3
# una ves hecho comentalo xq sino te tira error de q el directorio ya esta creado
# os.mkdir("30 dias Python/dia_12/prueba")  # crear un directorio nuevo

# ojo q si copias el path te lo da con las \ y asi te tira error cambialas por /
# os.chdir("30 dias Python/dia_12/asd")  # cambiar el path

a = os.getcwd()  # obtener el directorio con el q se esta trabajando
print(a)

# os.rmdir("30 dias Python\dia_12\hola")  # remover el directorio
print()

# 4
# print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print(len(sys.argv))
print('Welcome {}. Enjoy  {} challenge!'.format(
    sys.argv[0], "30 dias de python"))
# to exit sys
# sys.exit() # si tenes esto antes de el resto de las lamadas a sys no van a correr
# To know the largest integer variable it takes
print(sys.maxsize)
print()
# To know environment path
print(sys.path)
print()
# To know the version of python you are using
print(sys.version)
print()


# 5
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

print()

# 6 y 7
random = random.randint(2, 9)
print(random)
potencia = math.sqrt(2)
print(potencia)
print()

# 8
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

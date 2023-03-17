# strings, son un tipo de dato (o cadenas de caracteres en C)

letter = "p"
print(letter)

# multiline string se crean usando ''' o """"""

multiline_string = '''Hola todo bien?
si todo tranki y vos?
aca andamos estudiendo'''

print(multiline_string)
print()

# concatenacion

nombre = "Tino"
apellido = "Machichita"

full_name = nombre + " " + apellido
print(full_name)

print(len(apellido))
print(len(nombre) > len(apellido))
print()

# Escape Sequences in Strings --> \

'''
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
'''

print('Hola como estas?')
print("dia:10\tmes:10\taño:22")

# para poder escribir la \ en el mesnaje
print('This is a backslash  symbol (\\)')
print()

# to write a double quote inside a single quote
print('In every programming language it starts with \"Hello, World!\"')
print('sin la \\ funciona igual "aca la prueba"')


# formatear string(estilo viejo) --> %
print()


'''
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision
'''

nombre2 = "Ulii"
apellido2 = "Rodriguez"
lenguaje = "Python"
full_name2 = "yo soy %s %s y estoy aprendiendo %s" % (
    nombre2, apellido2, lenguaje)
print(full_name2)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' % (
    radius, area)  # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
# "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
print(formated_string)

print()
# formatear string(estilo nuevo) --> string.format()
texto_Fomateado = "yo soy {} {} y estoy aprendiendo {}".format(
    nombre2, apellido2, lenguaje)
print(texto_Fomateado)


a = 4
b = 5

print('{} + {} = {}'.format(a, b, a + b))
# limits it to two digits after decimal
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

print()


# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}'.format(
    radius, area)  # 2 digits after decimal
print(formated_string)

print()

# String Interpolation / f-Strings --> nos permite poner data en las respectivas posiciones

a = 4
b = 5

print(f"{a} + {b} = {a+b}")

print()

# string como secuencias de caracteres
nombre_tino = 'TinoElGordo'
# unpacking sequence characters into variables
a, b, c, d, e, f, g, h, i, j, k = nombre_tino
print(a)  # T
print(b)  # i
print(c)  # n
print(d)  # o
print(e)  # E
print(f)  # l
print(g)  # G
print(h)  # o
print(i)  # r
print(j)  # d
print(k)  # o

print()
# string como cadena de caracteres
array_letras = ["a", "b", "c", "d"]

for letra in range(len(array_letras)):
    print(array_letras[letra])

# se pude usar index negativo --> array_letras[-1]
# si a es la posicion 0 , con index negativo d es la posicion -1 (osea va al resves)
print()

# slice strings
languaje = "Python"
print(languaje[0:3])
# con esto le indicas q imprima del caracter 3 en adelante (le podes poner 6 o 20 o un numero grande como para indicar q es hasta el final)
print(languaje[3:6])
print(languaje[-3])
print(languaje[3:])

print(languaje[::-1])  # para revertir strings

# skip caracteres, osea desde la poscion 0 hasta el 6 slice cada 2
print(languaje[0:6:2])

print()


# string metodos

# capitaliza()
manzana = "manzana"
banana = "bAnANa"
# te pone la primera con mayucula y las otras en minusculas
print(manzana.capitalize())
print(banana.capitalize())


print(manzana.count("a"))
print(manzana.count("A"))

# count() returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count
challenge = 'thirty days of python'
# conta las Y q haya desde la posicion 7 hasta la 14
print(challenge.count('y', 7, 14))

# endswith() revisa si un string termina de cierta forma
print(challenge.endswith("on"))

# expandtabs() -->  Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge_tab = 'thirty\tdays\tof\tpython'
print(challenge_tab.expandtabs())   # 'thirty  days    of      python'
print(challenge_tab.expandtabs(10))  # 'thirty    days      of        python'

# find() --> retorna el index de la primera ocurrencia
print(challenge.find("y"))
print(challenge.find("thon"))

# rfind() --> retorna el index de la ultima ocurrencia encontrada
print(challenge.rfind('y'))
print(challenge.rfind('th'))

# index() --> Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError

sub_string = 'da'
print(challenge.index(sub_string))  # 7
# print(challenge.index(sub_string, 9))  # error

# rindex() --> lo mismo q index() pero con el valor de index mas alto
print(challenge.rindex(sub_string))  # 8

# isalalpha() --> chekea si todos los elementos del string pertenecen al alfabeto (a-z)(A-Z)
texto1 = "AbshfihSJHDkjskJSDñ"
texto2 = "ABhd456SDghfkhj"

print(texto1.isalpha())
print(texto2.isalpha())

# isdecimal() --> chekea si todos los elementos del string son decimales (0-9)
decimales = "45001354"
no_todos_decimales = "4531zxdfs4f652"

print(decimales.isdecimal())
print(no_todos_decimales.isdecimal())

# islower() --> chekea si todas las letras son en misnusculas
# isupper() --> chekea si todas las letras son en mayusculas
minisculas = "adsfjkl"
mayusculas = "SHVGDFK"
mix = "AKHsdfjhgSAlgk"

print(minisculas.islower())
print(mayusculas.islower())
print(mix.islower())
print(minisculas.isupper())
print(mayusculas.isupper())
print(mix.isupper())

# join()--> retorna un string concatenado
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# en los '' es lo q queres concatenar, es como si hicieras un for
result = ' '.join(web_tech)
print(result)  # 'HTML CSS JavaScript React'

result2 = '# '.join(web_tech)
print(result2)  # 'HTML# CSS# JavaScript# React'

# strip()--> elimina los caracteres dados desde el principio y el final de la cadena original, si no le pones nada como argumento saca los espacios en blanco
challenge = '  thirty days of pythoonnn  '
print(challenge.strip())
print(challenge.strip(" t"))  # esto si q no lo entiendo

# replace()--> remplaza una palabra por otra
challenge = 'thirty days of pythoonnn'
print(challenge.replace('python', 'coding'))

# split() --> divide los string, si no se le pasa nada como argumento--> los divide con una ,
# si se le pasa un argumento divide el string en el caracter indicado
challenge = 'thirty days of python'
print(challenge.split())  # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split('t'))

# title() -> te lo devuelve como si fuera un titulo (pone cada l letra con mayusculas y el resto con minuculas, es como lo q haces en JS con toLowerCase() y toUpperCase())
challenge = 'thirty Days of pyTHon'
print(challenge.title())  # Thirty Days Of Python

# swapcase() --> te invierte mayusculas y minusculas
print(challenge.swapcase())

# startswith() --> revisa si un string empieza con cierto caracter
print(challenge.startswith("t"))
print(challenge.startswith("T"))
print(challenge.startswith("p"))

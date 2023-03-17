# regular expressions
'''
Es una cadena de texto especial que ayuda a encontrar patrones en los datos. Se puede usar un RegEx para verificar si existe algún patrón en un tipo de datos diferente. Para usar RegEx en python primero debemos importar el módulo RegEx que se llama re.
'''

import re

'''
re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string
'''


# re.match(substr,string,re.I)

texto = "Tino le gustan mucho las machichitas"

match = re.match("Tino le gus", texto, re.I)
match2 = re.match("Tino le gusadgdfgfhg", texto, re.I)
print(match)
print(match2)
print()

# span  nos obtiene el principio y final de la coicidencia, como una tupla
span = match.span()
print(span)
print()

# desempacando los los elementos de span
start, end = span
print(start, end)
print()


substr = texto[start:end]
print(substr)
print()


# re.search(substr,string,re.I)
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_search = re.search("recommend", txt, re.I)
print(match_search)

span = match_search.span()
# podemos usar span para obtener la posicion de donde empieza a donde termina el match
print(span)
print()

# match vs search

string_with_newlines = """something 
someotherthing"""

# re.match no busca en todo el string "someotherthing" por lo cual no encuentra una ocurrencia
print(re.match('someother', string_with_newlines))

# re.search si busca en todo el string por lo cual si encuentra una ocurrencia
print(re.search('someother', string_with_newlines))
print()


# re.findall() --> a diferencia de las anteriores q te devuelven solo el primer match esta te devuelve todas los match q encuentra
# tambien otra dif seria q lo q retorna es una lista
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall("language", txt, re.I)
print(matches)
print()

# ya q estamos usando re.I no hace distincion entre mayuscula y minuscula
matches2 = re.findall("python", txt, re.I)
print(matches2)
print()

# si no ponemos el re.I tenemos q indicar q la palabra q buscamos se puede escribir de 2 formas
# la | nos sirve para buscar mas de una palabra al mismo tiempo
matches2 = re.findall("python|Python", txt)
print(matches2)
print()

matches2 = re.findall("python|language", txt)
print(matches2)
print()

# aca al no poner la | solo se queda con python con minusculas
matches3 = re.findall("python", txt)
print(matches3)
print()


# otra forma de buscar min y mayusculas
matches4 = re.findall("[Pp]ython", txt)
print(matches4)
print()


# Replacing a Substring
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub("[Pp]ython", "Tino", txt)
print(match_replaced)
print()

# otro ejem
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
print()


# split a text
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split("\n", txt))  # te lo separa cuando hay un salto de linea
print()


# Writing RegEx Patterns

# es como declarar un string normal pero agregando la r antes de los ""
regex_pattern = r"apple"
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '

matches = re.findall(regex_pattern, txt)
print(matches)

matches = re.findall(regex_pattern, txt, re.I)
print(matches)

regex_pattern = r"[Aa]pple"
matches = re.findall(regex_pattern, txt, re.I)
print(matches)


# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/images/regex.png
# []: A set of characters
# [a-c] means, a or b or c
# [a-z] means, any letter from a to z
# [A-Z] means, any character from A to Z
# [0-3] means, 0 or 1 or 2 or 3
# [0-9] means any number from 0 to 9
# [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
# \: uses to escape special characters
# \d means: match where the string contains digits(numbers from 0-9)
# \D means: match where the string does not contain digits
# .: any character except new line character(\n)
# ^: starts with
# r'^substring' eg r'^love', a sentence that starts with a word love
# r'[ ^ abc] means not a, not b, not c.
# $: ends with
# r'substring$' eg r'love$', sentence that ends with a word love
# *: zero or more times
# r'[a]*' means a optional or it can occur many times.
# +: one or more times
# r'[a]+' means at least once (or more)
# ?: zero or one time
# r'[a]?' means zero times or once
# {3}: Exactly 3 characters
# {3, }: At least 3 characters
# {3, 8}: 3 to 8 characters
# |: Either or
# r'apple|banana' means either apple or a banana
# (): Capture and group
print()

# Algunos ejem

# Escape character(\) in RegEx
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
# ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want
print(matches)
print()

# One or more times(+)
# d is a special character which means digits, + mean one or more times
regex_pattern = r'\d+'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!
print()

# Period(.)
# this square bracket means a and . means any character except new line
regex_pattern = r'[a].'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
print()


# Zero or more times(*)
# Zero or many times. The pattern could may not occur or it can occur many times.
regex_pattern = r'[a].*'  # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
print()

# Zero or one time(?)
# Zero or one time. The pattern may not occur or it may occur once.
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
print()

#Quantifier in RegEx
# podemos especificar el largo del substring
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']
print()

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
print()

# Cart ^:

# Starts with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
print()

# Negation
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
# ^ in set character means negation, not A to Z, not a to z, no space
regex_pattern = r'[^A-Za-z ]+'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
print()

import re

# las expresiones regulares son utiles para encontrar patrones, una ves se encuentra la coincidencia lo q podemos hacer es devolverla, devolver todas, reemplazarla, usarla como separador, etc

texto = """Hola gordo Tino, esta es la cadena 1. como estas?
Esta es la segunda linea de texto 235
esta es la ultima linea de texto
456987
abbbbb abb
abababab
"""

# diferencia entre mayusculas y minusculas
res = re.search("Hola", texto)  # encuentra la coicidencia y la devuelve
print(res)

# flags=re.IGNORECASE ignora distincion entre mayusculas y minusculas
# encuentra todas las concidencias
res = re.findall("esta", texto, flags=re.IGNORECASE)
print(res)

# \d --> busca digitos numericos del 0-9
# r es para idicar q voy a usar expresiones regulares
res = re.findall(r"\d", texto, flags=re.IGNORECASE)
print(res)

# para los casos contrarios (no en todos los casos) se usa la letra mayuscula
# \D me va a encontrar todo menos digitos numericos
res = re.findall(r"\D", texto, flags=re.IGNORECASE)
print(res)

# \w --> busca caracteres alfanumericos [a-z, A-Z, 0-9, _]
# \W --> busca todo menos caracteres alfanumericos [a-z, A-Z, 0-9, _]
res = re.findall(r"\w", texto)
print(res)

# \s --> busca espacios en blanco --> espacio, tab, \n (osea los saltos de linea)
# \S --> busca todo menos espacios en blanco --> espacio, tab, \n (osea los saltos de linea)
res = re.findall(r"\s", texto)
print(res)

# . --> busca todo menos saltos en linea
res = re.findall(r".", texto)
print(res)

# \n --> busca saltos en linea
res = re.findall(r"\n", texto)
print(res)

# \ --> cancelamos caracteres especiales (, , (), ?, -)
# cancelando la funcion del punto y buscando puntos
res = re.findall(r"\.", texto)
print(res)

# armando una cadena q busque un numero, seguido de un punto y un espacio en linea
# va a buscar una cadena q tenga un numero seguido de un . seguido de un espacio
res = re.findall(r"\d\.\s", texto)
print(res)

# ^ --> busca el comienza de una linea
res = re.findall(r"^Hola", texto)  # buscando Hola al pricipio de la linea
print(res)

# "Esta" esta al pricipio de una linea pero para q "^" te lo encuentre necesitas usar flags
# flags=re.M --> cada linea interpretala como si fuera una nueva linea
res = re.findall(r"^Esta", texto, flags=re.M)
print(res)

# $ --> busca el final de una linea
# fijate q tenes q poner "$" al final xq sino te toma lo q viene despues de "texto" como final de la linea
res = re.findall(r"texto$", texto, flags=re.M)
print(res)

# {n} --> busca n cantidad de veces el valor de la izquierda
res = re.findall(r"\d{3}", texto)  # \d{3} --> encontrame 3 numeros juntos
print(res)

# {n,m} --> al menos n, como maximo m
# me devuelve todos los valores donde encuentre por lo menos 2 numeros y como maximo 4 numeros
# fijate q si encuentra un numero como 456987 te lo parte en los 4 primeros numeros y los otros 2
res = re.findall(r"\d{2,4}", texto)
print(res)

# busca una "a" seguido de por lo menos 2 "b" y maximo 4 "b"
res = re.findall(r"ab{2,4}", texto)
print(res)

# con () hacemos grupos
# si encontras "abab" 2 veces me devolves solamente "ab"
res = re.findall(r"(ab){2}", texto)
print(res)

# | --> busca una cosa o la otra pero devuelve las 2 si las encuentra
res = re.findall(r"\d{2,4}|Hola", texto)
print(res)

# sub reemplaza un patron por otro en caso de encontrarlo
res = re.sub("texto", "Texto_remplazado", texto)
print(res)

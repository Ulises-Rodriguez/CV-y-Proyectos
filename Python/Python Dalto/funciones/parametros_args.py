# q pasa si queremos pasar muchos parametros a una funcion
# def fun(a,b,c,d,....) se hace muy largo

# forma no optima pero sirve
def sumar(lista):
    nums_sumados = 0

    for num in lista:
        nums_sumados += num

    return nums_sumados


res = sumar([1, 2, 3, 4, 5, 6, 7, 8])
print(res)

# si bien sirve lo ideal es hacer q la cantidad de argumentos sea indefinida, no pasarle una lista

# ojo : este parametro "*" se tiene q usar al final, osea yo puedo pasarle mas argumentos al principio pero no despues de "*"

# lo q pasa aca es q el primer valor q le paso es "Tino", luego el resto de valores son una lista de los numeros


def sumar_args(nombre, *nums):
    return f"{nombre} la suma de tus numeros es {sum(nums)}"


res = sumar_args("Tino", 1, 2, 3, 4, 5, 6, 7, 8)
print(res)


def sumar_desglosar(nums):
    return sum([*nums])


res = sumar_desglosar([1, 2, 3, 4, 5, 6, 7, 8])
print(res)

# parametros de palabras claves --> forzar los argumentos


def saludar(nombre, apellido, adjetivo):
    print(f"hola {nombre} {apellido} sos muy {adjetivo}")


# ojo: todos los parametros tienen q ser asi si queres cambiar el orden en el q se los pasas, osea no podes pasar solo adjetivo=... y los otros dejarlos de la forma comun
saludar(adjetivo="Gordito", nombre="Tino", apellido="Machichita")


# podes poner un valor por defecto a los argumentos para q asi en caso de q cuando se llama a la funcion no le pasas todos los parametros necesarios no te tire error ya q va a usar el valor por defecto
def saludar2(nombre, apellido, adjetivo="Gordito"):
    print(f"hola {nombre} {apellido} sos muy {adjetivo}")


# aca usa el valor por defecto
saludar2("Tino", "Machichita")
# aca al pasarle el adjetivo este pisa al valor por defecto
saludar2("Tino", "Machichita", "Rapidito")

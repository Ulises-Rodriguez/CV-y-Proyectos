# funciones --> def
# las funciones son bloques de codigo q son reutilizables, se las hace para hacer una tarea en especifico, las funciones solo funcionan si se las llama o invoca dentro de otras funciones con ()
# las funciones pueden o no terner 1 o varios parametros
# una funcion sin parametro de retorno devuleve none

def funcion_sin_parametros():
    name = "Tino"
    food = "Machichitas"
    print("A {} le gustan las {}".format(name, food))


funcion_sin_parametros()
print(funcion_sin_parametros())  # none

print()

name = "Tino"
food = "Machichitas"

# los nombres de los parametros pueden ser culauier cosa, no tienen xq llamarse igual a los argumentos q pasas
# la cantidad de parametros depende de vos


def funcion_con_parametros(name, food):
    print("A {} le gustan las {}".format(name, food))


funcion_con_parametros(name, food)

print()

# funciones q retornan un valor


def funcion_sin_parametros():
    name = "Tino"
    food = "Machichitas"
    full = name + " "+food

    return full


print(funcion_sin_parametros())

print()

# pasar argumentos con key y value


def suma(a, b):
    res = a + b
    return res


print(suma(a=2, b=3))

print()

# funciones con for


def sumatoria(a):
    res = 0

    for i in range(a+1):
        res += i

    return res


print(sumatoria(100))
print()

# funciones con bool y if


def es_menor(a, b):
    if a >= b:
        return True
    else:
        return False


print(es_menor(5, 2))
print()

# retornando una lista


def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(10))
print()


# funciones con parametros por defecto, osea q si no le pasas ningun parametro usa el q tiene por defecto
def parametros_por_defecto(a=5):
    res = list()
    for i in range(a+1):
        res.append(i)
    return res


print(parametros_por_defecto())
print(parametros_por_defecto(a=100))
print()

# cantidad de numeros arbitraria de argumentos, osea no definir la cantidad de forma manual
# recorda q puede ser cualquier nombre los parametros


def resta(*args):
    res = 200
    for num in args:
        res -= num
    return res


print(resta(100, 50, 20))
print()

# tambien podes hacer un combo entre argumentos por defecto y arbitrarios


def mix(equipo, *nums):
    print(equipo)
    for i in nums:
        print(i)


mix("equipo1", 1, 2, 3)
print()

# funciones con otras funcones


def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


# fijate q a la funcion cuando se la pasa como paramemtro no se le ponen con () ya q los () es para invocarla
print(do_something(square_number, 3))
print()

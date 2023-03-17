'''
In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

A function can take one or more functions as parameters
A function can be returned as a result of another function
A function can be modified
A function can be assigned to a variable
'''

# funciones como parametros


from functools import reduce


def sum_numbers(nums):  # normal function
    return sum(nums)


def hihg_order_function(f, lst):  # function as a parameter
    sumation = f(lst)
    return sumation


res = hihg_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(res)
print()

# funciones como return value


def square(x):          # a square function
    return x ** 2


def cube(x):            # a cube function
    return x ** 3


def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):  # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
print()


# Closures --> https://codigofacilito.com/articulos/closures-python
'''
Python permite que una función anidada acceda al ámbito externo de la función envolvente. Esto se conoce como Cierre (Clousure). el cierre se crea anidando una función dentro de otra función encapsuladora y luego devolviendo la función interna
'''


def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


clouser_res = add_ten()
print(clouser_res(5))
print(add_ten()(5))
print()


# scope
def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'

        print(a)
        print(b)

    funcion_anidada()
    # print(c)  # En este caso si ejecutamos funcion_principal obtendremos como resultado un error , donde se nos indica que la variable c no se encuentra definida. Esto error es gracias al scope, al alcance que tiene la variable.

# Al las variables a y b definirse en un scope superior, al que posee la variable c, estás posee un ciclo de vida mayor, es decir, podrán ser utilizadas dentro de funcion_principal y dentro de la función anidad. Sin embargo, al la variable c definirse dentro de la función anidada tendrá un alcance menor que a y b, solo pudiendo ser utilizada dentro de dicha función dentro de su bloque.

# Cómo sabemos, una variable podrá ser utilizada dentro del scope donde fue definida, y de igual forma, podrá ser utilizada en scopes de nivel inferior, pero nunca en un scope de nível superior


def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'
        b = 'Cambios de valor'

    funcion_anidada()
    print(b)  # Si ejecuto el script nos percatamos que la variable b no sufre cambio alguno. Esto sucede ya que para Python la variable b, dentro de la función anidada, es completamente diferente a la variable b de función funcion_principal


def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'
        # En este caso, nuevamente, obtendremos un error: local variable 'b' referenced before assignment.
        print(b)
        b = 'Cambios de valor'

    funcion_anidada()
    print(b)


# Si queremos indicar a Python que la variable b dentro de la función anidada será la misma variable b del escope superior, entonces haremos uso de la palabra reservada nonlocal.
def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        nonlocal b

        c = 'c'
        print(b)
        b = 'Cambios de valor'
        return b
    return funcion_anidada


res = funcion_principal()
print(res())
print()

# Decorators --> https://codigofacilito.com/articulos/decoradores-python
#  es un patron de diseño, en python esto permite al usuario añadir funcionalidades nuevas a objetos q ya existen sin modificar su estructura (esto se suele hacer antes de la llamada a la funcion q queres decorar)

'''
un decorador no es más que una función la cual toma como input una función y asu vez retorna otra función. Puede sonar algo confuso ¿no? lo que nos debe quedar claro es que al momento de implementar un decorador estaremos trabajando, con por lo menos, 3 funciones. El input, el output y la función principal
Para que nos quede más en claro a mi me gusta nombrar a las funciones como: a, b y c.


Donde a recibe como parámetro b para dar como salida a c. Esta es una pequeña "formula" la cual me gusta mucho mencionar.

a(b) -> c
'''


def greeting():
    return 'Welcome to Python'


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


g = uppercase_decorator(greeting)
print(g())

# para ahorrarte el laburo de tener q crear otra variable y pasar una funcion a otra usas el decorator @ + nombre de la funcion q queres cambiar como se comporta, dentro la funcion q le pasas

'''This decorator function is a higher order function
that takes a function as a parameter'''


# 3_ viene aca y con el greeting como parametro empieza a correr
def uppercase_decorator(function):
    def wrapper():  # 4_ la funcion wrapper() (q puede ser cualquier nombre pero lo comun es este) empieza a ejecutarse
        func = function()  # 5_ se le asigna a una variable la funcion greeting
        # 6_ en la variable make_uppercase asignamos la funcion greeting a la q le aplicamos upper
        make_uppercase = func.upper()
        return make_uppercase  # 7_ retornamos make_uppercase
    return wrapper  # 8_ retornamos el wrapper


@uppercase_decorator  # 1_ funcion a cambiar el comportamiento
def greeting():  # 2_ funcion q le pasas, osea --> g = uppercase_decorator(greeting)
    return 'Welcome to Python'


# 9_ imprimimos geeting con los cambios q se le aplican en el wrapper
print(greeting())
print()

# con mutliples decoradores

'''These decorator functions are higher order functions
that take functions as parameters'''


# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


# 1_ se toma la funcion gretting y se la pasa a uppercase_decorator
# 2_ el resultado del wrapper de uppercase_decorator se lo pasa a split_string_decorator
# 3_ el resultado del wrapper de split_string_decorator se retorna y se imprime
@split_string_decorator
# order with decorators is important in this case - .upper() function does not work with lists
@uppercase_decorator
def greeting():
    return 'Welcome to Python'


print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
print()


# Accepting Parameters in Decorator Functions
# Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters.
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))


print_full_name("Asabeneh", "Yetayeh", 'Finland')


#map, filter ,reduce

# map()función ejecuta una función específica para cada elemento en un iterable. El elemento se envía a la función como un parámetro.
numbers = [1, 2, 3, 4, 5]  # iterable


def square(x):
    return x ** 2


numbers_squared = map(square, numbers)
print(list(numbers_squared))
print()

# filter() es una funcion q toma una funcion y un iterable(osea una lista) y te devuelve una lista con los elementos q cumplan los requisitos.
ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


# Filter the array, and return a new array with only the values equal to or above 18:
adults = filter(myFunc, ages)

for x in adults:
    print(x)
print()

# reduce --> The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value
numbers_str = ['1', '2', '3', '4', '5']  # iterable


def add_two_nums(x, y):
    return int(x) + int(y)


total = reduce(add_two_nums, numbers_str)
print(total)    # 15
print()

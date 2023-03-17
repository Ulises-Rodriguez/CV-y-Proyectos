# Exception Handling
'''
python para manejar los errores usa try y except

el programa detecta un error y hace una salida con gracia ("exits gracefully") de manera contralada como resultado, lo usual es imprimir un mensaje que describe el error en la terminal 

las excepciones se pueden usar en para inputs incorrectos, nombre incorrecto de archivos, archivos q no se pueden encontrar, etc

con las excepciones podemos manejar estos errores sin q el programa crashe
'''

# flujo

'''
try : {run code}

si hay un error en el codigo dentro del try la excepcion se maneja con el except

except : {codigo a ejecutar cuando hay una excepcion}

else: {si no hay excepciones corre este codigo}

finally: {codigo q siempre se ejecuta sin imporatar nada}
'''

try:
    # aproposito estoy intentando sumar un numero con un string, por lo cual va a ver un error
    print(10 + "5")
except:
    # en ves de q el programa crashe se imprime este mensaje y ejecuta el resto del porgrama
    print("hubo un error")


print("hola soy un msg q se puede ejectuar xq se manejo el error")


print()


# podes agregar el tipo de error para indicar q except se encarga de manejar el error
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    # esta variable es un string por lo cual el error va a se manejado por TypeError
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')

except TypeError:
    print("Type error occured")

except ValueError:
    print("Value error occured")

except ZeroDivisionError:
    print("Zero division error occured")

print()

# con condicionales
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print("I alway run")

print()


# podes englobar todos los casos
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 / 0  # - int(year_born) esto para q el try funcione
    print('You are {name}. And your age is {age}.')

except Exception as e:  # en este caso dejas q este except maneje todos los error e imprima el error correspodiente q va a ser e
    print(e)
print()


# Packing and Unpacking Arguments in Python
'''
tenemos 2 operadores:

    - * para tuplas
    - ** para diccionarios
'''

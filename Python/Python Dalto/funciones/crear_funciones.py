import random

# crear funcion


def hola():
    print("Hola todo bien?")


# llamando a la funcion
hola()


def hola_2(nombre):
    print(f"Hola {nombre} todo bien?")


# llamando a la funcion
hola_2("Tino")


# funcion q retorna valores
def doble(num):
    return num * 2


res = doble(2)
print(res)

# crear contraseña


def crear_contraseña(num):
    letras = "abcdefghi"
    contraseña = ""

    for _ in range(num):
        num_random = random.randint(0, 10)
        letra_random = random.randint(0, 8)

        if num_random >= letra_random:
            contraseña = contraseña + str(num_random) + letras[letra_random]
        else:
            contraseña = contraseña + letras[letra_random] + str(num_random)

    return (contraseña, num)


# no olvides q podes desempaquetar para quedarte con el valor q quieras
res = crear_contraseña(5)[0]
print(res)

res, numero = crear_contraseña(5)
print(res, numero)

# creando propia excepcion

# las clases siempre la primera letra con mayuscula (no es obligacion pero es la costumbre)
# lo q le pases dentro de () es lo q hereda
class MiExcepcion(Exception):
    # constructor
    def __init__(self, err):
        print(err)


# raise es la palabra calve para lanzar una excepcion
# raise ZeroDivisionError("no dividas por 0 pa...")

try:
    raise MiExcepcion("eso no se hace")
except:
    print("no cometas ese error")

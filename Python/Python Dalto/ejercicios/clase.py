# falto el profe y los alumnos se organizaron para dar elllos la clase
'''
1 alumno profe
1 alumno ayudante

a) pedri la edad de los compañeros q vinieron hoy a clases y ordenar los datos de menor a mayor
b) el mayor de la clase es el profe y el menor el asistente
'''


def pedir_alumnos(cantidad):
    compañeros = []

    for _ in range(cantidad):
        nombre = input("decime tu nombre: ")
        edad = int(input("decime tu edad: "))
        compañeros.append((nombre, edad))

    # como tengo 2 datos dentro de cada tupla si no le paso key por defecto ordena por el primer elemento
    compañeros.sort(key=lambda a: a[1])
    # al usar un key puedo indicarle q quiero q ordene por el segundo elemento

    return compañeros


def profe_ayudante(cantidad):

    aux = pedir_alumnos(cantidad)

    # tambien podria usar pop / cantidad-1
    print(
        f"El profesor de la clase es {aux[-1][0].upper()} ya que su edad {aux[cantidad-1][1]} es la mayor")
    print(
        f"El ayudante de la clase es {aux[0][0].upper()} ya que su edad {aux[0][1]} es la menor")


profe_ayudante(3)

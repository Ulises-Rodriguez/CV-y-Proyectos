'''
La herencia es una herramienta fundamental para la orientación a objetos. Permite definir jerarquías de clases que comparten diversos métodos y atributos. Por ejemplo, consideremos la siguiente clase Rectangulo.
'''


class Rectangulo:
    """
    Define un rectángulo según su base y su altura.
    """

    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h


rectangulo = Rectangulo(20, 10)
print("Área del rectángulo: ", rectangulo.area())


'''
Supongamos, ahora, que necesitamos definir otra clase Triangulo.

class Triangulo:
    """
    Define un triángulo según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return (self.b * self.h) / 2
        
los códigos son muy similares, a excepción del método area(). Pero dado que el método __init__() es el mismo, podemos abstraerlo en una clase padre de la cual hereden tanto Rectangulo como Triangulo.
'''


class Poligono:
    """
    Define un polígono según su base y su altura.
    """

    def __init__(self, b, h):
        self.b = b
        self.h = h


class Rectangulo2(Poligono):

    def area(self):
        return self.b * self.h


class Triangulo(Poligono):

    def area(self):
        return (self.b * self.h) / 2


rectangulo = Rectangulo2(20, 10)
triangulo = Triangulo(20, 12)

print("Área del rectángulo: ", rectangulo.area())
print("Área del triángulo:", triangulo.area())

'''
Una misma clase puede heredar de varias clases (herencia múltiple); en ese caso, se especifican los nombres separados por comas.

class ClaseA(ClaseB, ClaseC, ClaseD):
    pass
'''

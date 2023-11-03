'''
Python es un lenguaje orientado a objetos, de modo que tiene soporte de primer nivel para la creación de clases. No obstante, no es condición necesaria hacer uso de ellas para poder crear un programa

Para crear una clase vamos a emplear la palabra reservada class seguido de un nombre escrito en Mayuscula

    class Alumno:
    pass --> Aquí introducimos, además, la palabra reservada pass, que sirve para rellenar un espacio que es requerido sintácticamente
    
Sabemos que las clases pueden contener funciones, a las que llamamos métodos.

    Todas las funciones definidas dentro de una clase deberán tener, al menos, un argumento, que por convención se lo llama self y es una referencia a la instancia de la clase
    
    class Alumno:

        def saludar(self):
            """Imprime un saludo en pantalla."""
            print("¡Hola, mundo!")
    
crear una instancia de nuestra clase.    

    Nótese que, al invocar a un método de la clase, no debemos indicar el argumento self, ¡Python hace eso por nosotros! De hecho, en nuestro ejemplo, self no es más que el objeto alumno

    alumno = Alumno()
    alumno.saludar()


'''


class Alumno:

    # Una clase también puede contener variables, a las que se conoce con el nombre de atributos. Para crear atributos definimos un método especial llamado __init__(), que es invocado por Python automáticamente siempre que se crea una instancia de la clase (conocido también como constructor o inicializador).

    def __init__(self):
        # En primer lugar, definimos el método inicializador ya mencionado que, al igual que el resto, debe llevar por primer argumento a self. Dentro de él creamos una variable llamada nombre. Sin embargo, para que no se pierda una vez finalizada la función y pueda ser accedida desde otros métodos de la clase (incluso por fuera de la clase), la definimos como self.nombre

        # En rigor, lo que hemos hecho en el inicializador es similar a lo siguiente.
        # alumno = Alumno()
        #alumno.nombre = "Pablo"

        self.nombre = "Pablo"

    def saludar(self):
        """Imprime un saludo en pantalla."""
        print(f"¡Hola, {self.nombre}!")


# claramente todos los alumnos que crearemos no tendrán el mismo nombre. Por ello sería conveniente permitir que, al definir una instancia, se pase como argumento el nombre del alumno y éste se almacene en el atributo self.nombre.
class Alumno2:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        """Imprime un saludo en pantalla."""
        print(f"¡Hola, {self.nombre}!")


alumno = Alumno2("Pablo")
alumno.saludar()

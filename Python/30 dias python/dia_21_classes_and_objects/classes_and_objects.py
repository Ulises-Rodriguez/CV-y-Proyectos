#Classes and Objects

'''
Python es un lenguaje de programación orientado a objetos. Todo en Python es un objeto, con sus propiedades y métodos. Un número, cadena, lista, diccionario, tupla, conjunto, etc. utilizado en un programa es un objeto de una clase

Una clase es como un constructor de objetos o un "modelo" para crear objetos. Instanciamos una clase para crear un objeto. La clase define los atributos y el comportamiento del objeto, mientras que el objeto, por otro lado, representa la clase.

>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
'''

# Crear una clase
'''
# syntax
class ClassName:
  code goes here
'''


class Persona:
    pass


print(Persona)  # <class '__main__.Persona'>
print()


# Crear un Objeto
p = Persona()
print(p)  # <__main__.Persona object at 0x0000023250A0E9D0>
print()

# Constructores de clase
'''
Ya creamos una clase pero una clase sin constructor no es realmente util
Al igual q JS Python tiene una funcion contructora built-in init(). init() es una funcion contructora q es una referencia a la intancia de la clase 
'''


class Persona:
    def __init__(self, name) -> None:
        self.name = name  # self --> nos permite adjuntar, poner parametros a las clases


p = Persona("Tino")
print(p.name)
print(p)
print()


class Persona:
    def __init__(self, firstname, lastname, age, country, city) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


p = Persona("Tino", "Machichita", 10, "Arg", "Cordoba")
print(p.firstname, p.lastname, p.age, p.country, p.city)
print()


# Metodos --> son funciones q pertenecen a la clase
class Persona:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def persona_info(self):
        return f"{self.firstname}, {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}"


p = Persona("Tino", "Machichita", 10, "Arg", "Cordoba")
print(p.persona_info())
print()


# Metodos por defecto de los objetos --> valores por defecto lo cual es util para evitar errores q pueden pasar por si el usuario se olvida de pasar alguno de los parametros
class Persona:
    def __init__(self, firstname="Tino", lastname="Machichita", age=10, country="ARG", city="Cordoba") -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def persona_info(self):
        return f"{self.firstname}, {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}"


# aca se pasan todos los parametros
p = Persona("Ulises", "Rodriguez", 25, "ARG", "Cordoba")
p2 = Persona("Tino")  # aca solo se pasan algunos

print(p.persona_info())
print(p2.persona_info())
print()


# Método para modificar los valores predeterminados de la clase --> En el siguiente ejemplo, la clase de persona, todos los parámetros del constructor tienen valores predeterminados. Además de eso, tenemos el parámetro de habilidades, al que podemos acceder usando un método.

class Persona:
    def __init__(self, firstname="Tino", lastname="Machichita", age=10, country="ARG", city="Cordoba") -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def persona_info(self):
        return f"{self.firstname}, {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}"

    def add_skill(self, skill):
        self.skills.append(skill)


p = Persona()
print(p.persona_info())
p.add_skill("HTML")
p.add_skill("CSS")
p.add_skill("JS")
p.add_skill("React JS")
p.add_skill("Python")

p2 = Persona('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.persona_info())
print(p.skills)
print(p2.skills)
print()

# Inheritance (Herencia) --> Usando la herencia podemos reutilizar el código de la clase principal. La herencia nos permite definir una clase que hereda todos los métodos y propiedades de la clase padre. La clase padre o superclase o clase base es la clase que proporciona todos los métodos y propiedades. La clase secundaria es la clase que hereda de otra clase principal.


# # No llamamos al constructor init() en la clase secundaria. Si no lo llamamos, aún podemos acceder a todas las propiedades desde el padre. Pero si llamamos al constructor, podemos acceder a las propiedades principales llamando a super.
# Podemos agregar un nuevo método al elemento secundario o podemos anular los métodos de la clase principal creando el mismo nombre de método en la clase secundaria. Cuando agregamos la función init(), la clase secundaria ya no heredará la función init() del padre.
class Estudiante(Persona):
    pass


s1 = Estudiante('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Estudiante('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.persona_info())
s2.add_skill("HTML")
s2.add_skill("CSS")
s1.add_skill("JS")
s1.add_skill("React JS")
s1.add_skill("Python")
print("s1 skills:", s1.skills)
print("s2 skills:", s2.skills)
print()


# Anulando los metodos del padre
class Estudiante(Persona):
    # ahora como estamos llamando __init__ es necesario usar super para acceder a las propiedades del padre
    def __init__(self, firstname="Tino", lastname="Machichita", age=10, country="ARG", city="Cordoba", genero="male") -> None:
        self.genero = genero  # funcionalidad extra q no esta en el padre
        # con super accedemos a las propiedades del padre
        super().__init__(firstname, lastname, age, country, city)

    def persona_info(self):
        genero = "He" if self.genero == "male" else "She"
        return f'{self.firstname} {self.lastname} is {self.age} years old. {genero} lives in {self.city}, {self.country}.'


s1 = Estudiante('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
s2 = Estudiante('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.persona_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.persona_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
print()

# Podemos usar la función integrada super() o el nombre del padre Persona para heredar automáticamente los métodos y propiedades de su padre. En el ejemplo anterior, anulamos el método principal. El método del niño tiene una característica diferente, puede identificar si el género es masculino o femenino y asignar el pronombre adecuado (Él/Ella).

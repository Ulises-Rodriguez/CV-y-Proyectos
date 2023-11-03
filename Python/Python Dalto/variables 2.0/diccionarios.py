# para crear los diccionarios usando dict() tenes q pasarle una clave=valor
dicc = dict(nombre="tino", edad=12)
print(dicc)

# esta es la forma como json (dato: de esta manera no se puede crear diccionarios vacios)
dicc = {
    "nombre": "Tino",
    "edad": 12
}

print(dicc)

# creando diccionarios con fromkeys
# es una metodo q nos permite crear diccionarios con todos sus valores none

dicc = dict.fromkeys(["nombre", "apellido"])

print(dicc)
print(dicc["nombre"])

# una cosa curiosa es q si no le pasas los elementos dentro de [] te itera el primer elemento
dicc = dict.fromkeys("abcdef")
print(dicc)

# si le pasamos un segundo valor lo q hace es iterar el primero e igualarlo al segundo valor
dicc = dict.fromkeys("abcdef", "Hola")
print(dicc)

# tambien podes iterar mas de un elemento pasandole una lista
dicc = dict.fromkeys(["nombre", "apellido"], "Nose")
print(dicc)

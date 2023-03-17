import math

# The radius of a circle
diametro = int(input("pasame el radio: "))
radio = diametro/2
pi = math.pi

area = pi * radio

print("el radio es de: ", radio)
print("el area del circulo es igual a", area)


# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

nombre = input("decime tu nombre: ")
apellido = input("decime tu apellido: ")
pais = input("decime tu pais: ")

print("nombre: " + nombre + "\n" + "appellido: " +
      apellido + "\n" + "pais: " + pais + "\n")

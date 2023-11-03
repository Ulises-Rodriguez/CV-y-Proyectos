a = 2
print(a + 3)

# concatenar
nombre = "TIno"
bienvenida = "Hola " + nombre + " ,Como estas?"
print(bienvenida)
# lo mismo q con + pero te ahorras tener q poner los espacios
print("Hola", nombre, ",Como estas?")


num = 5
# bienvenida = "Hola " + nombre + " ,Como estas?" --> si lo dejas asi nada mas te tira erro ya q intentas concatenar un palabras con un numero

# f strings
bienvenida2 = f"Hola {num} ,Como estas?"
# el format es un metodo q te completa los {} con lo q le pasas como parametro
bienvenida3 = "Hola {} ,Como estas?".format(num)
# ambos te sirven para convertirlo a texto

print(bienvenida2)
print(bienvenida3)

# con del borras una variable
del bienvenida3
# print(bienvenida3)


# operadores de pertenencia e identidad
# el in te va a buscar Ola en bienvenida
print("Ola" in bienvenida)
# el not hace q el in haga lo opuesto, osea va a ver si Ola no esta en bienvenida
print("Ola" not in bienvenida)

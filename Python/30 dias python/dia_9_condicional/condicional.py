# condicionales --> if, elfi, else

# el codigo dentro del if se ejecuta si y solo si se cumple la condicion

# a = int(input("pasame un numero: "))

# if a > 0:
#     print("se cumplio la condicion del if")
# elif a == 0:
#     print("se cumplio la condicion del elif")
# else:
#     print("se cumplio la condicion del else")


# tienen short hand
# b = int(input("pasame un numero: "))
# print("el numero q me paseste es par") if b % 2 == 0 else print(
#     "el numero es impar")

# condicionales anidades --> if dentro de otro if

# c = int(input("pasame un numero: "))
# if c > 0:
#     if c % 2 == 0:
#         print('A is a positive and even integer')
#     else:
#         print('A is a positive number')
# elif c == 0:
#     print('A is zero')
# else:
#     print('A is a negative number')


# condicionales y operadores logicos
d = int(input("pasame un numero: "))

if d > 0 and d % 2 == 0:
    print("numero par y positivo")
elif d == 0 or d < 0:
    print("nuermo 0 o negativo")
else:
    print("numero no par")

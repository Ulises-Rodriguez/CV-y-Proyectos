# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

# age = int(input("pasame tu edad: "))

# if age >= 18:
#     print("sos mayor de edad podes manejar")
# else:
#     dif = 18 - age
#     print("sos menor de edad todavia te faltan {}".format(dif))

# Compare the values of my_age and your_age using if … else. Who is older(me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

# my_age = 25

# if age >= my_age:
#     dif = age - my_age
#     if dif == 0:
#         print("tenemos la misma edad")
#     else:
#         print("tenes {} años mas q yo".format(dif))
# else:
#     dif = my_age - age
#     print("tengo {} años mas q vos".format(dif))


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

# num1 = int(input("pasame el primer numero: "))
# num2 = int(input("pasame el segundo numero: "))

# if num1 > num2:
#     print("{} es mas grande q {}".format(num1, num2))
# elif num1 < num2:
#     print("{} es menor q {}".format(num1, num2))
# else:
#     print("{} es igual a {}".format(num1, num2))

# Write a code which gives grade to students according to theirs scores
'''
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''

# nota = int(input("pasame tu nota: "))

# if nota >= 80 and nota <= 100:
#     print("tu nota es {}".format(nota), "estas entre 80-100, tu grado es A")
# elif nota >= 70 and nota <= 89:
#     print("tu nota es {}".format(nota), "estas entre 70-89, tu grado es B")
# elif nota >= 60 and nota <= 69:
#     print("tu nota es {}".format(nota), "estas entre 60-69, tu grado es C")
# elif nota >= 50 and nota <= 59:
#     print("tu nota es {}".format(nota), "estas entre 50-59, tu grado es D")
# else:
#     print("tu nota es {}".format(nota), "estas entre 0-49, tu grado es F")


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

# mes = (input("pasame un mes: ")).capitalize()

# if mes == "Semtiembre" or mes == "Octubre" or mes == "Nomviembre":
#     print("Otoño")
# elif mes == "Diciembre" or mes == "Enenro" or mes == "Febrero":
#     print("Invierno")
# elif mes == "Marzo" or mes == "Abril" or mes == "Mayo":
#     print("Primevera")
# elif mes == "Junio" or mes == "Julio" or mes == "Agosto":
#     print("Verano")
# else:
#     print("no escribiste bien el mes")


# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

# fruits = ['banana', 'orange', 'mango', 'lemon']

# fruta = input("decime una fruta para agregar al carrito: ")

# if fruta not in fruits:
#     fruits.append(fruta)
#     print(fruits)
# else:
#     print("la fruta {} ya se encuentra en el carrito {}".format(fruta, fruits))


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1_Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

# skill = input("decime algun lenguaje/libreria/framework: ")
# skill = skill.capitalize()


# if skill in person['skills']:
#     length = len(person['skills']) / 2
#     print(person['skills'][int(length)])
# else:
#     print("Ese skill no esta en la lista")

# 2_Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

# skill = input("decime algun lenguaje/libreria/framework: ")
# skill = skill.capitalize()

# if skill in person['skills']:
#     py = input("Sabes Python? y/n: ")
#     if py == "y":
#         print("bien ahi :3")
#     else:
#         print("xq no le das una chance :3")
# else:
#     print("Ese skill no esta en la lista")


# 3_If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

# sabes_JS = input("Sabes JS: y/n ")
# sabes_RJS = input("Sabes ReactJS: y/n ")
# sabes_Node = input("Sabes Node: y/n ")
# sabes_Py = input("Sabes Python: y/n ")
# sabes_MDB = input("Sabes MongoDB: y/n ")

# if sabes_JS == "y" and sabes_RJS == "y":
#     print("sos front-edn developer")
# elif sabes_Node == "y" and sabes_Py == "y" and sabes_MDB == "y":
#     print("sos back-end developer")
# elif sabes_RJS == "y" and sabes_Node == "y" and sabes_MDB == "y":
#     print("sos full-stack developer")
# else:
#     print("unknown title")

# 4_If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.

if person['country'] == "Finland" and person['is_marred'] == True:
    print("{} {} lives in {}. He is married".format(
        person['first_name'], person['last_name'], person['country']))

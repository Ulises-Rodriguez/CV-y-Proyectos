# loops

# nos permiten hacer q se repita cierta accion sin la necesidad de escribir el codigo una y otra ves

# While
count = 0

while count < 5:
    print(count)
    count += 1

print()

# In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

print()

# while con break
count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        print("se ejecuta el break")
        break

print()

# para hacer skip usamos continue --> nos permite saltear el resto de sentencias
var = 10                    # Second Example
while var > 0:
    var = var - 1
    if var == 5:
        continue  # --> se sasltea el numero 5
    print('Current variable value :', var)
print("Good bye!")

print()


# for
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    print(number)

print()

for number in range(0, int(len(numbers))):
    print(number)


# for con string
for letra in "Python":
    print(letra)

print()

language = "Python"
for letra in range(len(language)):
    # no te olvides q un string es un array de chars por lo cual si solo pones print(letra) te va a imprimir las posiciones de las letras
    print(language[letra])

print()

# for con tuplas

tpl = (0, 1, 2, 3, 4)

for num in tpl:
    print(num)

print()

# for en dict

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

for key in person:
    print(key)

print()


for key, value in person.items():  # fijate q podes usar mas de una variable en el loop
    print(key, value)

print()


for skill in range(len(person['skills'])):
    print(person['skills'][skill])

print()

# for con set
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

print()

# el break y continue tambien funcionan con el for
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break

print()

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    # for short hand conditions need both if and else statements
    print('Next number should be ', number +
          1) if number != 5 else print("loop's end")
print('outside the loop')

print()

# la funcion range(start,end,step) --> start es por donde empieza por defecto es 0, end donde termina (sin incluirlo) y step es el incremento q si no lo pones es 1

lst = list(range(11))
print(lst)

set = set(range(2, 11))
print(set)

tpl = tuple(range(2, 12, 2))
print(tpl)

print()

# loops anindados

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

for key in person:
    if key == "skills":
        for skill in person['skills']:
            print(skill)

print()

# for else
for num in range(11):
    print(num)
else:
    print("el loop freno en el numero:", num)

print()

# pass
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current Letter :', letter)

print("Good bye!")

print()

dicc = {
    "nombre": "Tino",
    "edad": 12,
    "comida": "pollo con zapallo"
}

for key in dicc:
    print(key)  # esto solo nos devulve las claves

print()
print()

for datos in dicc.items():
    # print(key)  # al usar items nos devuelve una tupla con claves y valores

    key = datos[0]
    value = datos[1]

    print(key, ":", value)


# break y continue

frutas = ["manzana", "banana", "pera", "granada", "kiwi", "melon"]

for fruta in frutas:
    if fruta == "granada":
        continue  # lo q va a pasar aca es q se va a saltear la vuelta en la q apraresca granada
    print(fruta)

print()

for fruta in frutas:
    if fruta == "kiwi":
        break  # aca lo q va a pasar es q cuando la furta sea kiwi el bucle termina por completo, no imporata si quedan vueltas por dar
    print(fruta)

print()

# break y else
for fruta in frutas:
    if fruta == "kiwi":
        break
    print(fruta)
else:
    # lo curioso de un break es q al ejecutarse se saltea todo lo relacionado al for incluido el else
    print("temino el bucle")

print()

# List Comprehension --> La comprensión de listas ofrece una sintaxis más corta cuando desea crear una nueva lista basada en los valores de una lista existente.
# la sintaxis --> newlist = [expression for item in iterable if condition == True]
# La expresión es el elemento actual en la iteración, pero también es el resultado, que puede manipular antes de que termine como un elemento de lista en la nueva lista
# El iterable puede ser cualquier objeto iterable, como una lista, una tupla, un conjunto, etc
# La condición es como un filtro que solo acepta los elementos que se valoran en True (no es obligacion q este el if)
nums = [2, 3, 5, 6]
nums_duplicados = [x*2 for x in nums]
print(nums_duplicados)

# esto funciona para tuplas y conjuntos tambien

animales = ["perro", "gato", "loro", "pez"]

# recorres usando los elemtos q hay en animales
for animal in animales:
    print(animal)

nums = [10, 5, 6, 8]

for num in nums:
    res = num * 2
    print(res)

# iterar sobre 2 listas
# una forma seria poner un for dentro de otro for
# otra forma es usando una funcion zip

# primero las listas tienen q tener la misma cantidad de elementos
animales = ["perro", "gato", "loro", "pez"]
nums = [10, 5, 6, 8]

# tambien puede ser con mas de 2 listas
# ojo xq esto se itera todo al mismo tiempo, osea no q se itera toda la primera lista y luego la segunda
for num, animal in zip(nums, animales):
    print("recorriendo lista nums: ", num)
    print("recorriendo lista animales: ", animal)


# con range recorres usando numeros
for i in range(2, 5):
    print(i)

# podes combinar con len para haci recorrer hasta q te quedes sin elementos en animales
for i in range(len(animales)):
    print(animales[i])

# forma mejor de recorrer una lista por su indice
# ahora num es igual a dos variables --> es una tupla
for num in enumerate(nums):
    # print(num)  # nos devuelve el indice junto con el valor
    # print(num[0])  # para acceder a los indices
    # print(num[1])  # para acceder al valor

    # para acceder a los 2 valores de la tupla
    indice = num[0]
    valor = num[1]

    print(f"indice = {indice} y valor = {valor}")


# usando el for/else
for num in nums:
    print(num)
# los else se ejecutan siempre
else:
    print("el bucle termino")

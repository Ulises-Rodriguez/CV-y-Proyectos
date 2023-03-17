# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers(imaginary siblings are fine)
nombres_hermanas = ("ludmi", "maria")
nombres_hermanos = ("juan", "tino")

# Join brothers and sisters tuples and assign it to siblings
names = nombres_hermanas + nombres_hermanos

# How many siblings do you have?
print(len(names))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = ("sergio", "alicia") + nombres_hermanas + nombres_hermanos

# Unpack siblings and parents from family_members
father, mother, *sibilings = family_members
print(father, mother, sibilings)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana")
vegetables = ("carrot", "potato", "onion")
animal = ("cow", "fish")

food = fruits + vegetables + animal
print(food)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_list = list(food)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food[2:4])

# Slice out the first three items and the last three items from food_staff_lt list
x = slice(0, 1)
print(food[x])

# Delete the food_staff_tp tuple completely
del food
print(food)

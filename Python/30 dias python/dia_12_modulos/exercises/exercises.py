# Write a function which generates a six digit/character random_user_id
from random_digits import random_id, user_id_gen_by_user, rgb_color_gen, list_of_hexa_colors, list_of_rgb_colors, generate_colors, shuffle_list, unique_items

print(random_id())
print()


# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# te tira un None al final xq no estas retornando nada con la funcion user_id_gen_by_user()
# para evitarlo en ves de imprimir los id guardalos en un array y despues en ves de imprimir user_id_gen_by_user() hace otra funcion q te los desempaque
# print(user_id_gen_by_user())

# o simplemente no lo pongas dentro de un print XD
user_id_gen_by_user()
print()

# Write a function named rgb_color_gen. It will generate rgb colors(3 values ranging from 0 to 255 each).
print(rgb_color_gen())

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

print(list_of_hexa_colors(5))
print()

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print(list_of_rgb_colors())
print()
# Write a function generate_colors which can generate any number of hexa or rgb colors.
'''
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
'''

print(generate_colors("hexa", 5))
print()
print(generate_colors("rgb", 6))
print()

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
print(shuffle_list([1, 5, 9, 6, 3]))
print()


# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print(unique_items())
print()

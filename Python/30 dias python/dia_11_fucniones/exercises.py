# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b


print(add_two_numbers(1, 5))
print()

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.


def area_of_circle(pi, r1, r2):
    area = 0
    area = pi * r1 * r2
    return area


print(area_of_circle(3.14, 2, 2))
print()


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    res = 0
    for num in nums:
        res += num
    return res


print(add_all_nums(5, 8, 9, 3, 6, 4, 7))
print()

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.


def convert_celsius_to_fahrenheit(cel):
    far = cel * (9/5) + 32
    msg = "{}°C son iguales a {}°F".format(cel, far)
    return msg


print(convert_celsius_to_fahrenheit(20))
print()

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.


def check_season(mes):
    estacion = ""
    if mes == "Semtiembre" or mes == "Octubre" or mes == "Nomviembre":
        estacion = "Otoño"
    elif mes == "Diciembre" or mes == "Enenro" or mes == "Febrero":
        estacion = "Invierno"
    elif mes == "Marzo" or mes == "Abril" or mes == "Mayo":
        estacion = "Primevera"
    elif mes == "Junio" or mes == "Julio" or mes == "Agosto":
        estacion = "Verano"
    else:
        estacion = "no escribiste bien el mes"

    return estacion


print(check_season("Diciembre"))
print()

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
lista = [1, 5, "hola", "Tino", True]


def print_list(lst):
    for item in lst:
        print(item)


print_list(lista)
print()

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).


def reverse_list(lst):
    lst.reverse()
    for item in lst:
        print(item)


reverse_list(lista)
print()

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
string_list = ["Hola", "tINO", "JuAn", "coMiDA"]


def capitalize_list_items(lst):
    for item in lst:
        print(item.capitalize())


capitalize_list_items(string_list)
print()

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.


def add_item(a, lst):
    lst.append(a)
    return lst


print(add_item("item agregado", lista))
print()

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it


def remove_item(a, lst):
    if a in lst:
        lst.remove(a)
        return lst
    else:
        return "el elemento {} no esta en la lista {}".format(a, lst)


print(remove_item(9, lista))
print(remove_item(1, lista))
print()

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
nums = [1, 5, 8, 9, 6, 3, 4]


def sum_of_numbers(nums, a):
    nums.append(a)
    res = 0
    for num in nums:
        res += num
    return res


print(sum_of_numbers(nums, 10))
print()


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(nums, a):
    nums.append(a)
    res = 0
    for num in nums:
        if num % 2 != 0:
            res += num
    return res


print(sum_of_odds(nums, 5))
print()

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.


def sum_of_even(nums, a):
    nums.append(a)
    res = 0
    for num in nums:
        if num % 2 == 0:
            res += num
    return res


print(sum_of_even(nums, 8))
print()

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.


def evens_and_odds(num):
    evens = 0
    odds = 0
    msg = ""

    for i in range(num):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    msg = "En el numero: {}\nLa cantidad de numeros pares es: {}\nLa cantidad de numeros impares es: {}".format(
        num, evens, odds)
    return msg


print(evens_and_odds(10))
print()

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number


def factorial(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res


print(factorial(4))
print()

# Write a function called is_prime, which checks if a number is prime.


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("El numero {} no es primo".format(num))
            return False
    print("El numero {} es primo".format(num))
    return True


print(is_prime(10))
print(is_prime(5))
print()

# Write a functions which checks if all items are unique in the list.
lista = [1, 5, 8, 9, "Hola", "Tino"]


def is_in(lst, item):
    if item in lst:
        return True
    else:
        return False


print(is_in(lista, 5))
print(is_in(lista, 10))
print(is_in(lista, "Hola"))
print()

# Write a function which checks if all the items of the list are of the same data type
lst1 = [1, 5, 6, 9, 8]
lst2 = [4, "hola", "45", 3, True]


def all_same_type(lst):
    for item in range(1, len(lst)):
        if type(lst[item-1]) != type(lst[item]):
            return False
    return True


print(all_same_type(lst1))
print(all_same_type(lst2))
print()

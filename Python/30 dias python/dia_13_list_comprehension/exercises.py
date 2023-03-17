# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_nums = [i for i in numbers if i < 0 or i == 0]
print(negative_nums)
print()

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

flatten = [num for i in list_of_lists for k in i for num in k]
print(flatten)
print()

# Using list comprehension create the following list of tuples:
'''
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''

list_of_tuples = [(i, i**0, i**1, i**2, i ** 3, i ** 4, i ** 5)
                  for i in range(11)]
print(list_of_tuples)
print()

# def generate_list_of_tuples():
#     list_of_tuples = []
#     for i in range(11):
#         list_of_tuples.append(
#             (i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5))
#     return list_of_tuples


# print(generate_list_of_tuples())


# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


def flatten_list_of_tuples():
    countries = [[('Finland', 'Helsinki')], [
        ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    return [[sub2[0].upper(), sub2[0].upper()[:3], sub2[1].upper()] for sub in countries for sub2 in sub]
    # for sub in countries --> por cada elemento de countries
    # for sub2 in sub --> por cada elemento dentro de sub
    # [sub2[0].upper(), sub2[0].upper()[:3], sub2[1].upper()] --> me va a hacer esta operacion


print(flatten_list_of_tuples())


# def ff():
#     aux = []
#     a = ""
#     b = ""
#     c = ""
#     for item_array in countries:
#         for item_tuple in item_array:
#             a = item_tuple[0]
#             b = item_tuple[0][:3]
#             c = item_tuple[1]
#         aux.append([a, b, c])
#     print(aux)

# ff()

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']


def list_string():
    aux = []
    a = ""
    b = ""
    for i in names:
        for j in i:
            a = j[0]
            b = j[1]
        c = a + " " + b
        aux.append(c)
    # print(aux)


def lst_strig_comprehension():
    result = [b[0] + " " + b[1] for i in names for b in i]

    return result


# print(lst_strig_comprehension())

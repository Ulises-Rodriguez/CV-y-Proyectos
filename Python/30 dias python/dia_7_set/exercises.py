it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))
print()

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
print()

# Insert multiple IT companies at once to the set it_companies
other_companies = {"company_1", "company_2", "company_3"}
it_companies.update(other_companies)
print(it_companies)
print()

# Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)
print()


# What is the difference between remove and discard
# remove(elem): Remove element elem from the set. Raises KeyError if elem is not contained in the set.
# discard(elem): Remove element elem from the set if it is present.

# Join A and B
a_union_b = A.union(B)
print(a_union_b)
print()

# Find A intersection B
a_intersection_b = A.intersection(B)
print(a_intersection_b)
print()

# Is A subset of B

print(A.issubset(B))
print()


# Are A and B disjoint sets

print(A.isdisjoint(B))
print()


# Join A with B and B with A

print(A.union(B))
print(B.union(A))

print()

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
print()

# Delete the sets completely
# del it_companies
# del A
# del B
# print()


# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)

len_age_list = len(age)
len_age_set = len(age_set)

print("length age list =", len_age_list, "length age set =", len_age_set)
print()

# Explain the difference between the following data types: string, list, tuple and set
'''
string son un array de elementos chars
list es una coleccion de elementos q pueden o no ser del mismo tipo, se permiten elementos repetidos, elementos ordenados y se pueden repetir
tupla es una coleccion de elementos, repetibles, ordenados pero no modificables
set es un conjunto de elementos q no permite elementos repetidos, ni orden, no indexada pero si modificable
'''

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

palabra = "I am a teacher and I love to inspire and teach people"

x = palabra.split()  # recorda q el metodo split divide un string y lo guarda en una lista
print(x)

st = set(x)
print(st)

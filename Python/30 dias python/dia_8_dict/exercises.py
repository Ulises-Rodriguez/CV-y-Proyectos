# Create an empty dictionary called dog
dog = {}
dog2 = dict()

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Tino"
dog["color"] = "Black"
dog["legs"] = 4
dog["age"] = 10

print(dog)
print(type(dog))
print()

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Ulises",
    "last_name": "Rodriguez",
    "gender": "Male",
    "age": 25,
    "martial_status": "Single",
    "skills": ["HTML", "CSS", "JS", "ReactJS", "SQL", "Python"],
    "country": "Argentina",
    "city": "Cordoba",
    "addres": {
        "street": "Angelo Peredo",
        "num": "34"
    }
}

# Get the length of the student dictionary
print(len(student))
print()

# Get the value of skills and check the data type, it should be a list
values_skills = student["skills"]
print(type(values_skills))
print()

# Modify the skills values by adding one or two skills
student["skills"].append("skill1")
student["skills"].append("skill2")
print(student["skills"])
print()

# Get the dictionary keys as a list
print(student.keys())
print()


# Get the dictionary values as a list
print(student.values())
print()

# Change the dictionary to a list of tuples using items() method
lst = list(student)
print(lst)
lst2 = student.items()
print(lst2)
print()

# Delete one of the items in the dictionary
del student["age"]
# print(student["age"])
print()

# Delete one of the dictionaries
del dog
# print(dog)

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

thirty = "Thirty"
days = "Days"
of = "Of"
python = "Python"

print(thirty, days, of, python)
print()

# Declare a variable named company and assign it to an initial value "Thirty Days Of Python".
company = thirty + " " + days + " " + of+" " + python
print(company)
print()

# Print the length of the company string using len() method and print().
print(len(company))
print()

# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
print(company.upper())
print(company.lower())

print()

# Use capitalize(), title(), swapcase() methods to format the value of the string
print(company.capitalize())
print(company.title())
print(company.swapcase())
print()

# Cut(slice) out the first word of Thirty Days Of Python string.

print(company[1:])
print(company.strip("T"))
print()

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
coding = "Coding For All"
print(coding.index("Coding"))
print()

# Replace the word coding in the string 'Coding For All' to Python.
print(coding.replace("Coding", "Python"))
print()

# Split the string 'Coding For All' using space as the separator (split())
print(coding.split())
print(coding.split("o"))
print()

# What is the character at index 0 in the string Coding For All.
print(coding.index(""))  # C --> 0
print()

# What is the last index of the string Coding For All. --> 13

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(coding.rfind("l"))
print()

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'

print(sentence.find("because"))
print()

# Use rindex to find the position of the last occurrence of the word because
print(sentence.rindex("because"))

print()

# Slice out the phrase 'because because because' in the following sentence
print(sentence.split("because because because"))

print()

# Does 'Coding For All' start/end with a substring Coding?

print(coding.startswith("Coding"))
print(coding.endswith("Coding"))
print()

# remove the left and right trailing spaces in the given string.
coding_with_spaces = '   Coding For All      '
print(coding_with_spaces.strip())
print()

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
arrya_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

res = "#".join(arrya_libraries)
print(res)
print()

# Use the new line escape sequence to separate the following sentences
text1 = "I am enjoying this challenge."
text2 = "I just wonder what is next."

print(text1+"\n"+text2)
print()

# Use a tab escape sequence to write the following lines

print("Name\t"+" Age\t"+"Country\t"+"  City\t\n" +
      "Asabeneh "+"250\t"+"Finland\t"+"  Helsinki")

print()

# Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
text_format = "The area of a circle with radius {} is {} meters square.".format(
    radius, area)
print(text_format)

print()

# Make the following using string formatting methods
'''
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''

a = 8
b = 6

print("{} - {} = {}".format(a, b, a+b))
print("{} + {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
print("{} / {} = {}".format(a, b, a/b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a//b))
print("{} ** {} = {}".format(a, b, a**b))

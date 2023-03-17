# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words


import csv
from exercises_files.module import count_languages, most_population, regex_list


import json


def count_nums_lines_and_words(txt):
    res = ""

    count_words = 0

    with open("30 dias Python/dia_19_File_Handling/exercises_files/{}".format(txt)) as f:
        txt = f.read().splitlines()

        for char in txt:
            for _ in char:
                count_words += 1

        res = "cantindad de lineas {}, cantidad de letras {}".format(
            len(txt), count_words)

        return res


print(count_nums_lines_and_words("oabama_speech.txt"))
print()

# HARVESTELLA

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
'''
# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]

'''


file = "30 dias Python\dia_19_File_Handling\exercises_files\countries_data.json"


def most_spoken_languages():
    with open(file, "r", encoding="utf-8") as f:
        txt = json.load(f)
        res = count_languages(txt)

        return res


print(most_spoken_languages())
print()


# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_population_json():
    with open(file, "r", encoding="utf-8") as f:
        txt = json.load(f)
        res = most_population(txt)

        return res


print(most_population_json())
print()


# ind the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order.
'''
print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]
'''


def find_most_common_words(file, num):
    with open("30 dias Python/dia_19_File_Handling/exercises_files/{}".format(file)) as f:
        txt = f.read(num)
        res = regex_list(txt)

        return res


print(find_most_common_words("oabama_speech.txt", 450))
print()


# Read the hacker news csv file and find out:

# a) Count the number of lines containing python or Python
# b) Count the number lines containing javascript or Javascript
# c) Count the number lines containing Java and not JavaScript

def hacker_count(fname):
    csvFile = csv.reader(open(fname, mode="r"))
    count_a = 0
    count_b = 0
    count_c = 0
    for lines in csvFile:
        plain_text_line = " ".join(lines)
        if "python" in plain_text_line or "Python" in plain_text_line:
            count_a += 1
        if (
                "JavaScript" in plain_text_line
                or "Javascript" in plain_text_line
                or "javascript" in plain_text_line
        ):
            count_b += 1
        if not (not ("Java" in plain_text_line) or "Javascript" in plain_text_line):
            print(plain_text_line)
            count_c += 1
    print(count_a, count_b, count_c)


hacker_count(
    '30 dias Python/dia_19_File_Handling/exercises_files/hacker_news.csv')

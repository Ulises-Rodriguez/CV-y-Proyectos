import re


def languages(lst):
    res = []

    for country in range(len(lst)):

        for language in range(len(lst[country]["languages"])):
            res.append(lst[country]["languages"][language])

    return res


def count2(inicial, lst):
    amount = 0
    res = []

    for i in lst:
        if inicial == i:
            amount += 1

    return amount


def big_ten(lst):
    aux = []
    lst.sort(key=lambda x: x[1], reverse=True)

    for i in range(0, 10):
        aux.append(lst[i])

    return aux


def count_languages(lst):
    languages_list = []
    languages_list = languages(lst)

    amount = 0
    res = []

    for language in languages_list:
        amount = count2(language, languages_list)

        if (language, amount) not in res:
            res.append((language, amount))

    res = big_ten(res)

    return res


def most_population(lst):
    res = sorted(lst,
                 key=lambda population: population["population"], reverse=True)

    res = res[0:10]

    for item in res:
        country = item["name"]
        population = item["population"]
        print("{} tiene una pobalcion de {}".format(country, population))


def count_words(word, txt):

    aux = re.findall(r"\b{}\b".format(word), txt)
    res = 0

    for i in aux:
        if word == i:
            res += 1

    return res


def regex_list(txt):
    array_regex = re.split(" ", txt)
    a = []
    aux = []
    count = 0

    for i in array_regex:
        if "." not in i and i not in a:
            a.append(i)

    for word in a:
        if word not in aux and word != " ":
            if "." in word:
                word = word[:-1]
            count = count_words(word, txt)
            print((word, count))
        count = 0

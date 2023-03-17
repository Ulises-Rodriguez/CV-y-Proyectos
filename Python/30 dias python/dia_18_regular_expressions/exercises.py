import re

# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

'''
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
'''


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


regex_list(paragraph)
print()


# Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(word):

    if re.search(r"\d|-|\?|\¡|\!", word):
        return False

    return True


print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))  # True
print(is_valid_variable('f!irstname'))
print()


# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


def clean_text(txt):

    return re.sub("\%|\$|\%|\@|\&|\.|\;|\,|\!|\?|#", "", txt)


print(clean_text(sentence))
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher

print()
cleaned_text = clean_text(sentence)


def most_frequent_words(cleaned_text):
    res = 0
    split_array = re.split(" ", cleaned_text)
    aux = []
    aux2 = []

    for word in split_array:

        if word not in aux:
            aux.append(word)
            res = count_words(word, cleaned_text)

            if res > 1:
                aux2.append((res, word))

    return aux2


print(most_frequent_words(cleaned_text))

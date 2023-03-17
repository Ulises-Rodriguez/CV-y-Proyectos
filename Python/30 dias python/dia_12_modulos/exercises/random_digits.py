import random
import string

chars = string.ascii_letters
char_digits = string.digits

combinacion = chars + char_digits

lst = []
lst[:0] = combinacion


def random_id():
    id = ""
    for i in range(0, len(lst)):  # aca podes ponerle 6 de rengo maximo y listo
        # y esto te lo podes usar usando choice()
        random_position = random.randint(0, 61)
        if i <= 6:
            id += lst[random_position]
        else:
            break
    return id


def user_id_gen_by_user():
    nums_chars = int(input("cuantos caracteres queres q tengas los ids: "))
    nums_ids = int(input("Cuantos ids queres generar: "))
    for _ in range(nums_ids):  # el i q soles poner no lo usas para nada por eso es mejor poner _ q te sirve para evitar crear una variable q no va a usar
        id = ""
        for _ in range(nums_chars):
            # solucion cool --> identity = ''.join([random.choice(char_list) for _ in range(charsize)])
            selected = random.choice(lst)
            id += selected
        print(id)


def rgb_color_gen():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)

    return "rgb({},{},{})".format(a, b, c)


def list_of_hexa_colors(cantidad=0):
    hexa = "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f".split(",")
    lst_hexa_colors = []
    aux = "#"
    for _ in range(cantidad):
        for _ in range(6):
            aux = aux + random.choice(hexa)
        lst_hexa_colors.append(aux)
        aux = "#"
    return lst_hexa_colors


def list_of_rgb_colors():
    random_amount = random.randint(1, 100)
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    lst_rgb = []
    aux = ""

    for i in range(random_amount):
        aux = "rgb({},{},{})".format(a, b, c)
        lst_rgb.append(aux)

    return lst_rgb


def add_colors_hexa_to_list(lst, num):
    aux = "#"
    hexa = "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f".split(",")

    for _ in range(num):
        for _ in range(6):
            aux = aux + random.choice(hexa)
        lst.append(aux)
        aux = "#"

    return lst


def add_colors_rgb_to_list(lst, num):
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    aux = ""

    for _ in range(num):
        aux = "rgb({},{},{})".format(a, b, c)
        lst.append(aux)

    return lst


def generate_colors(selector, num):

    selector = selector.lower()
    lst_colors = []

    if selector == "hexa":
        aux = add_colors_hexa_to_list(lst_colors, num)
        lst_colors = aux.copy()

    elif selector == "rgb":
        lst_colors = add_colors_rgb_to_list(lst_colors, num)

    return lst_colors


def shuffle_list(lst):
    aux = []

    while lst != []:
        item = random.choice(lst)
        aux.append(item)
        lst.remove(item)

    return aux

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.


def unique_items():
    lst = []

    while len(lst) < 7:
        num = random.randint(0, 9)
        if not (num in lst):
            lst.append(num)
        else:
            continue

    return lst

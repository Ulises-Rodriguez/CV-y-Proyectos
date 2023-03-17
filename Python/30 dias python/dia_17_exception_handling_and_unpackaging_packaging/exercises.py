# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.


names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']

*nordic_countries, es, ru = names

print(nordic_countries, es, ru)


def packing_person_info(**kwargs):
    for key, value in kwargs.items():
        print("{} = {}".format(key, value))


print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

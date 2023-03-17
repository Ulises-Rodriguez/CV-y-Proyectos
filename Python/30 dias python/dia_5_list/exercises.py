# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
list_more_five_items = [4, 5, "hola", "comida",
                        True, {"nombre": "tino"}, ["fruta", 8, False]]

# Find the length of your list
print(len(list_more_five_items))

print()

# Get the first item, the middle item and the last item of the list
last = len(list_more_five_items)-1
middle = (len(list_more_five_items)) / 2

first_item = list_more_five_items[0]
middle_item = list_more_five_items[int(middle)]
last_item = list_more_five_items[last]
print(first_item)
print(middle_item)
print(last_item)

print()

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Uli", 25, 1.84, "soltero", "mi casa"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

print()

# Print the number of companies in the list
print(len(it_companies))

print()

# Print the first, middle and last company
first_company = it_companies[0]
middle_company = len(it_companies) / 2
last_company = len(it_companies) - 1

print(first_company)
print(it_companies[int(middle_company)])
print(it_companies[last_company])

print()

# Print the list after modifying one of the companies
it_companies[0] = "Modificacion"
print(it_companies)

print()

# Add an IT company to it_companies
it_companies.append("compania agregada")
print(it_companies)

print()

# Insert an IT company in the middle of the companies list
it_companies.insert(4, "compania agrada en posicion 4")
print(it_companies)
print()

# Change one of the it_companies names to uppercase(IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)
print()

# Join the it_companies with a string '#;  '
res = "#; ".join(it_companies)
print(res)
print()

# Check if a certain company exists in the it_companies list.
is_in = "IBM" in it_companies
print(is_in)
print()

# Sort the list using sort() method
it_companies.sort()
print(it_companies)
print()

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
print()

# Slice out the first 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[0:3])

# Slice out the last 3 companies from the list
print(it_companies[4:])
print()

# Slice out the middle IT company or companies from the list
print(it_companies.pop(3))
print()

# Remove the first IT company from the list
it_companies.remove("Facebook")
print(it_companies)
print()

# Remove the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(3)
print(it_companies)
print()

# Remove the last IT company from the list
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]
last = len(it_companies) - 1
it_companies.pop(last)
print(it_companies)
print()

# Remove all IT companies from the list
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)
print()

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
f_and_b = front_end + back_end
print(f_and_b)
print()

# Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack = front_end + back_end
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)
print()

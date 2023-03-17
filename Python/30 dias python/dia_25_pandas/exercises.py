import pandas as pd

# pd.set_option("display.max_rows", None) # esto para mostrar todo el contenido xq sino por defecto pandas solo muestra las 10 filas

# Read the hacker_news.csv file from data directory
csv_pd = pd.read_csv("30 dias python\dia_25_pandas\hacker_news.csv")
print(csv_pd)
print()

# Get the first five rows
print(csv_pd.head())
print()

# Get the last five rows
print(csv_pd.tail())
print()

# Get the title column as pandas series
title = csv_pd["title"]
print(title)
print()

# Count the number of rows and columns
num_rows = csv_pd.shape
num_columns = csv_pd.columns

print("rows nums :", num_rows[0])
print()

print("colums elems :", num_columns)
print("colums nums :", len(num_columns))
print()

df = pd.DataFrame(num_columns)
print(df)
print()

# Filter the titles which contain python


def title_py():
    aux = [title for title in csv_pd["title"]]
    aux_filter = filter(lambda x: "python" in x, aux)

    return list(aux_filter)


print(title_py())
print()


# Filter the titles which contain JavaScript
def title_js():
    aux = [title for title in csv_pd["title"]]
    aux_filter = filter(lambda x: "JavaScript" in x, aux)

    return list(aux_filter)


print(title_js())
print()

# Explore the data and make sense of it
data = {
    "id": csv_pd["id"],
    "title": csv_pd["title"],
    "url": csv_pd["url"],
    "num_points": csv_pd["num_points"],
    "num_comments": csv_pd["num_comments"],
    "author": csv_pd["author"],
    "created_at": csv_pd["created_at"],
}

data_df = pd.DataFrame(data)
print(data_df)

import pandas as pd

df = pd.read_csv("ejer_de_archivos\\datos.csv")
# print(df)

# 1) cambiar el tipo de dato de una columna
# astype te lo convierte al tipo q le pases
df["edad"] = df["edad"].astype(str)
print(df["edad"])
print(type(df["edad"][0]))
print()
print()

# 2) reemplazar valores
df["edad"][0] = "te cambie el valor"
print(df)
print()
print()

# otra forma es usando replace
# lo q pasa aca es q le decis anda a la columna de "edad" y ahi remplaza el primer valor q encuentres q diga "te cambie el valor" y cambialo por "78" con el "inplace" es para modificar el DataFrame en lugar de crear uno nuevo.
# .replace("te cambie el valor", 78, 2, inplace=True) si yo le pasaba un 2 esto iba a reeplazar las primeras 2 ocurrencias
df["edad"].replace("te cambie el valor", 78, inplace=True)
print(df)
print()
print()

# 3) ahora en datos.csv (para poder hacerlo agrega a datos.csv --> "algo", y deja el resto sin completar) una fila con datos incompletos y tenemos q eliminarla

# dropna te elimina las filas o columnas con datos faltantes
print(df)
df = df.dropna()
# con esto eliminas las columnas con datos faltantes
# df = df.dropna(axis=1)
print(df)
print()
print()

# 4) eliminar filas repetidas
print(df)
df = df.drop_duplicates()
print(df)

# 5) crear un df con el resultado
df.to_csv("ejer_de_archivos\\datos_resultado_final.csv")

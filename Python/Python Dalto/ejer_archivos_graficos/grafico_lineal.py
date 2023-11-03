import pandas as pd
# esto es una libreria de visualicion de datos
import matplotlib.pyplot as plt
# libreria de graficos estadisticos
import seaborn as sns

df = pd.read_csv("ejer_archivos_graficos\\tino_machichitas.csv")
print(df)

# creando un grafico de lineas
# encotra la columna fecha y esa es el eje x, encontra la columna machichitas y esa el eje y, toda esta info sacala de df
sns.lineplot(x="fechas", y="machichitas", data=df)

# para hacer un punto le pasas la fecha, el numero (osea coordenada x,y) y la "o" es para q te dibuje el puntito
plt.plot("03/04/23", 8, "o")

# mostrando el grafico
plt.show()

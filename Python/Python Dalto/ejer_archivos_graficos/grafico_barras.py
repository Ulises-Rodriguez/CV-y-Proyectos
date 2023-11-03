import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ejer_archivos_graficos\\ingrsos_cofla.csv")

# barplot es para graficos de barras
sns.barplot(x="fuente", y="ingresos", data=df)

total_ingresos = df["ingresos"].sum()
print(total_ingresos)

plt.show()

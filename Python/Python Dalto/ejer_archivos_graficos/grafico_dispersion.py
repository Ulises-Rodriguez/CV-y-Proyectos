import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ejer_archivos_graficos\\ingrsos_cofla.csv")

# scatterplot es para graficos de dispersion
sns.scatterplot(x="tiempo", y="dinero", data=df)

plt.show()

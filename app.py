import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

notas = pd.read_csv("arquivos/ratings.csv")

notas.columns = "usuarioId", "filemID", "nota", "momento"
print(notas["nota"].unique())
print(notas["nota"].value_counts())

notas["nota"].plot(kind='hist')
plt.show()

media = notas["nota"].mean()
mediana = notas["nota"].median()

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(notas["nota"].describe())

sns.boxplot(notas["nota"])
plt.show()


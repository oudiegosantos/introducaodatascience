import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)

notas = pd.read_csv("arquivos/ratings.csv")
filmes = pd.read_csv("arquivos/movies.csv")
filmes.columns = ["filmeId", "titulo", "genero"]

notas.columns = "usuarioId", "filmeID", "nota", "momento"
print(notas["nota"].unique())
print(notas["nota"].value_counts())

# notas["nota"].plot(kind='hist')
# plt.show()

media = notas["nota"].mean()
mediana = notas["nota"].median()

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(notas["nota"].describe())

# sns.boxplot(notas["nota"])
# plt.show()

print(notas.head())
print(filmes.head())

print(notas.query("filmeID==1")["nota"].mean())
print(notas.query("filmeID==2")["nota"].mean())
medias_por_filme = notas.groupby("filmeID")["nota"].mean()

print(medias_por_filme.head())
#medias_por_filme.plot(kind="hist")
# plt.show()
# sns.boxplot(medias_por_filme)
# plt.show()
sns.displot(medias_por_filme, kde=True)
plt.title("Histograma de média por filmes")
plt.show()

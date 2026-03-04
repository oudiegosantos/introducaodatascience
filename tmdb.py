
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.expand.frame.repr', False)
tmdb = pd.read_csv("tmdb/tmdb_5000_movies.csv")
movies = pd.read_csv("arquivos/movies.csv")
notas = pd.read_csv("arquivos/ratings.csv")



print(tmdb.head())
#sns.displot(tmdb["revenue"])
plt.title("Distribuição de receitas dos filmes")
#plt.show()
#sns.displot(tmdb["budget"])
plt.title("Distribuição de orçamento dos filmes")
#plt.show()

com_faturamento = tmdb.query("revenue > 0")
#sns.displot(com_faturamento["revenue"])
#plt.show()

print(tmdb["original_language"].unique())
#print(tmdb["original_language"].value_counts())

#tipos de variaveis
#budget (orçamento) => quantitativa continua

#nota do movielens => 0.5, 1.5,1 ... não possui 0.25
#quantidade de votos => 1,2,3,4,5 ... não existe 2.5


# mais_10_votos = tmdb.query("vote_count > 10")
# sns.displot(mais_10_votos["vote_average"], kde=True)
#plt.show()

contagem_de_linguas = tmdb["original_language"].value_counts().to_frame().reset_index()
contagem_de_linguas.columns = ["original_language", "total"]
print(contagem_de_linguas.head())
#sns.countplot(data=tmdb, x="original_language")
#plt.show()

#contagem_de_linguas.plot(kind="pie", y="total", labels=contagem_de_linguas["original_language"])
#plt.show()

total_por_linguas = tmdb["original_language"].value_counts()
total_de_en = total_por_linguas.loc["en"]
total_geral = total_por_linguas.sum()
total_resto = total_geral - total_de_en
print(f"Total de Inglês é: {total_de_en} geral é: {total_geral} e restante é: {total_resto}")

dados = {
    "lingua" : ["Ingles", "Outros"],
    "total" : [total_de_en, total_resto],
}

dados = pd.DataFrame(dados)
print(dados)

#sns.barplot(data=dados, x="lingua", y="total")
#plt.show()
# dados.plot(kind="pie", y="total", labels=dados["lingua"])
# plt.show()

total_de_outros_filmes_por_lingua = tmdb.query("original_language != 'en'")["original_language"].value_counts()
#print(total_de_outros_filmes_por_lingua.head())
#sns.countplot(data=tmdb.query("original_language != 'en'"), x="original_language")
#plt.show()

#plt.figure(figsize = (16, 8))
sns.countplot(data=tmdb.query("original_language != 'en'"), x="original_language", order=total_de_outros_filmes_por_lingua.index, hue="original_language", hue_order=total_de_outros_filmes_por_lingua.index,
 stat="percent",
 palette="mako")
#plt.title("Distribuição da lingua original dos filmes exceto em Inglês")
#plt.show()



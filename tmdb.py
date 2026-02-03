import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.expand.frame.repr', False)
tmdb = pd.read_csv("tmdb/tmdb_5000_movies.csv")
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
# plt.show()

contagem_de_linguas = tmdb["original_language"].value_counts().to_frame().reset_index()
contagem_de_linguas.columns = ["original_language", "total"]
print(contagem_de_linguas.head())
sns.countplot(data=tmdb, x="original_language")
plt.show()
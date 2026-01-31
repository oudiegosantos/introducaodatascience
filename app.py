import pandas as pd

notas = pd.read_csv("arquivos/ratings.csv")

notas.columns = "usuarioId", "filemID", "nota", "momento"
print(notas["nota"].unique())
print(notas["nota"].value_counts())


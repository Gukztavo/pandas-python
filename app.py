import pandas as pd 

# Importando um dataset

data = pd.read_csv('./dataset/2004-2021.tsv', sep=';')
data.head()
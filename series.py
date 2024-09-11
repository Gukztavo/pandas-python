import pandas as pd 

# Importando um dataset

data = pd.read_csv('./dataset/2004-2021.tsv', delimiter='\t')

#SELECIONA UMA COLUNA INTEIRA
# print(data.columns)
print(data['ESTADO'])

type(data['ESTADO'])

#selecionando a  observação indexada no indici [1] do dataframe
di = data.iloc[1]
print(di)

#criando series

series1 = pd.Series([5.5,6.0,9.5], index=['PROVA1','PROVA2','PROJETO'], name = 'Notas do Gustavo')
print(series1)
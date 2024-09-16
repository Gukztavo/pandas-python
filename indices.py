import pandas as pd 

# Importando um dataset

data = pd.read_csv('./dataset/2004-2021.tsv', delimiter='\t')


pesquisa_de_satisfacao = pd.DataFrame({

    'bom':[50,21,100],
    'ruim':[131,2,30],
    'pessimo':[30,20,1]
}, index=['XboxOne', 'Playstation4','Switch'])

# print(pesquisa_de_satisfacao.index)
# pesquisa_de_satisfacao.index

data.iloc[[1,5,10,15]]  #slice

#selecionaar linhas/obs de indices 5,1,15,10  

data.iloc[[5,1,15,10]]

#retonar valor indice 1 e coluna 4
data.iloc[1,4]


print(pesquisa_de_satisfacao.iloc[0,1])

print(pesquisa_de_satisfacao.loc['XboxOne'])
import pandas as pd 


data = pd.read_csv('./dataset/2004-2021.tsv', sep=';')

type(data)
data.shape

#print(f'o data fra possui {data.shape[0]} linha/observação/registros e {data.shape[1]} colunas/ atributos/variaveiss.')

#criando dataFrame

personagfens_df = pd.DataFrame({
    'nome': ['Luke','yoda','robo'],
    'idade':[10,20,30],
    'peso':[70.5,60.5,100.02],
    'ehjedi': [True, True, False]
})
#personagfens_df.info()
#personagfens_df.columns
#print(personagfens_df)
lista = list(personagfens_df.columns)
print(lista) 

# perosnagens_df_renomeado = personagfens_df.rename(columns={
#         'nome': 'Nome Completo',  # renomeia a coluna de nome 'nome' para 'Nome completo
#         'idade': 'Idade'

# })

# print(perosnagens_df_renomeado)

# personagfens_df.rename(columns={'nome': 'Nome Completo','idade': 'Idade'}, inplace=True)
# print(personagfens_df)

personagfens_df.columns = ['NOME','IDADE','PESO', 'EH JEDI']  #altera todo os nomes das colunas
print(personagfens_df)
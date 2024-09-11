import pandas as pd 


data = pd.read_csv('./dataset/2004-2021.tsv', sep='\t')

data.head()

produto_bkp = data['PRODUTO'].copy()
# print(produto_bkp)

data['PRODUTO'] = 'Combustível'

nrows, ncols = data.shape
nrows, ncols

novos_produtos = [f'Produto {i}'for i in range(nrows)]
data['PRODUTO']= novos_produtos

data['PRODUTO'] = produto_bkp
print(data['PRODUTO'])

import pandas as pd# Importando base de dados 
endereco_dados = 'BASES\Financeira.csv'

df_financeira = pd.read_csv(endereco_dados, sep=',' ,encoding='iso-8859-1')

print('------Financeira------')
print(df_financeira.head())
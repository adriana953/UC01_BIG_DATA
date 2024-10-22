# pip install xrld - biblioteca para manipular arquivos do Excel:
# pip install openpyxl - biblioteca para manipular arquivos xlsx :
import pandas as pd

endereco_dados = 'BASES\ENEM_2020_2023.xlsx'

df_enem = pd.read_excel(endereco_dados)

print('------ BASE DE DADOS ENEM ------')
print(df_enem.head())

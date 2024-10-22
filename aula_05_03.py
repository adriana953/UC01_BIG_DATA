import pandas as pd# Importando base de dados

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';' ,encoding='iso-8859-1')

print(df_ocorrencias.head())


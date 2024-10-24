import pandas as pd
import numpy as np

# Importando a Base de Dados
endereco_dados = 'BASES\Funcionarios.csv'

# Criando o DataFrame 
df_funcionarios = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')

# Exibindo a base de dados funcionarios
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_funcionarios.head())

# Criando o array do salário dos funcionários
array_salario = np.array(df_funcionarios["Salário"])

# Obtendo a média do salário dos funcionários
media_salario = np.mean(array_salario)

# Obtendo a mediana do salário dos funcionários
mediana_salario = np.median(array_salario)

# Obtendo a distância entre a média e a mediana do salário dos funcionários
distancia_salario = abs((media_salario - mediana_salario) / mediana_salario) * 100

# Obtendo o máximo e o mínimo do valor do salário dos funcionários
maximo_salario = np.max(array_salario)
minimo_salario = np.min(array_salario)

# Obtendo a amplitude do valor do salário dos funcionários
amplitude_salario = maximo_salario - minimo_salario

# Exibindo os dados solicitados
print("\n-- OBTENDO INFORMAÇÕES SOBRE OS SALÁRIOS DOS FUNCIONÁRIOS --")
print(f"A média dos salários é R$ {media_salario:.2f}")
print(f"A mediana dos salários é R$ {mediana_salario:.2f}")
print(f"A distância entre a média e a mediana é {distancia_salario:.2f} %")
print(f"O menor valor dos salários é R$ {minimo_salario:.2f}")
print(f"O maior valor dos salários é R$ {maximo_salario:.2f}")
print(f"A amplitude dos valores dos salários é {amplitude_salario:.2f}")
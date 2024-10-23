import pandas as pd
# Importando a Base de Dados
endereco_dados = 'BASES\Funcionarios.csv'
# Criando o DataFrame 
df_funcionarios = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')

# Gerando os Dados Solicitados 
media_salario = df_funcionarios['Salário'].mean(axis=0)
media_idade = df_funcionarios['Idade'].mean(axis=0)
maior_tempo = df_funcionarios['Tempo'].max(axis=0)
menor_tempo = df_funcionarios['Tempo'].min(axis=0)
diferenca_tempo = maior_tempo - menor_tempo
media_tempo = df_funcionarios['Tempo'].mean(axis=0)
func_tempo_velho = df_funcionarios[df_funcionarios['Tempo'] == maior_tempo]['Nome']
func_tempo_novo = df_funcionarios[df_funcionarios['Tempo'] == menor_tempo]['Nome']
qtd_func = df_funcionarios['Nome'].count()

# Exibindo os Dados do DataFrame 
print('\n---------- DADOS DOS FUNCIONÁRIOS -----------')
print(df_funcionarios.head())
print('\n----------- DADOS SOLICITADOS ------------')
print(f"O Salário médio da empresa é R$ {media_salario:.2f}")
print(f"A Média das idades dos funcionários é {media_idade:.0f} anos.")
print(f"O Maior tempo de empresa é {maior_tempo} anos.")
print(f"O Menor tempo de empresa é {menor_tempo} anos.")
print(f"A Diferença de tempo de empresa é {diferenca_tempo} anos.")
print(f"A Média de tempo de empresa é {media_tempo:.0f} anos.")
print(f"O(A) Funcionário(a) mais novo(a) na empresa é {func_tempo_novo.to_string(index=False)}")
print(f"O(A) Funcionário(a) mais antigo(a) na empresa é {func_tempo_velho.to_string(index=False)}")
print(f"A Quantidade de funcionários na empresa são {qtd_func}")
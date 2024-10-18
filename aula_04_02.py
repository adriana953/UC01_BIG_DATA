# Dados dos Vendedores
dados_vendedores = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena', 'Igor', 'Juliana'],
    'Sexo': ['F', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'Idade': [28, 34, 45, 30, 40, 29, 38, 31, 27, 33],
    'Qtd_vendas': [120, 150, 110, 95, 130, 140, 105, 125, 100, 135]
}

# Total e média de vendas
total_vendas = sum(dados_vendedores['Qtd_vendas'])
media_vendas = total_vendas / len(dados_vendedores['Qtd_vendas'])

# Média das idades, maior e menor idade
media_idade = sum(dados_vendedores['Idade']) / len(dados_vendedores['Idade'])
maior_idade = max(dados_vendedores['Idade'])
menor_idade = min(dados_vendedores['Idade'])

# Vendedor com maior e menor quantidade de vendas
indice_maior_vendas = dados_vendedores['Qtd_vendas'].index(max(dados_vendedores['Qtd_vendas']))
indice_menor_vendas = dados_vendedores['Qtd_vendas'].index(min(dados_vendedores['Qtd_vendas']))

vendedor_maior_vendas = dados_vendedores['Nome'][indice_maior_vendas]
vendedor_menor_vendas = dados_vendedores['Nome'][indice_menor_vendas]

# Quantidade de vendas por sexo
vendas_masculinas = sum(qtd for sexo, qtd in zip(dados_vendedores['Sexo'], dados_vendedores['Qtd_vendas']) if sexo == 'M')
vendas_femininas = sum(qtd for sexo, qtd in zip(dados_vendedores['Sexo'], dados_vendedores['Qtd_vendas']) if sexo == 'F')

# Resumo final
print("Resumo do Relatório:")
print(f"Total de Vendas: {total_vendas}")
print(f"Média de Vendas: {media_vendas:.2f}")
print(f"Média das Idades: {media_idade:.2f}")
print(f"Maior Idade: {maior_idade}")
print(f"Menor Idade: {menor_idade}")
print(f"Vendedor com Maior Vendas: {vendedor_maior_vendas} ({max(dados_vendedores['Qtd_vendas'])} vendas)")
print(f"Vendedor com Menor Vendas: {vendedor_menor_vendas} ({min(dados_vendedores['Qtd_vendas'])} vendas)")
print(f"Vendas Masculinas: {vendas_masculinas}")
print(f"Vendas Femininas: {vendas_femininas}")

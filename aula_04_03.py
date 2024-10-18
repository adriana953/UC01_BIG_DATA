# Dados dos Municípios
dados_municipios = {
    'Município': ['Rio de Janeiro', 'Niterói', 'São Gonçalo', 'Duque de Caxias', 'Nova Iguaçu', 
                  'Belford Roxo', 'São João de Meriti', 'Petrópolis', 'Volta Redonda', 'Campos dos Goytacases'],
    'Habitantes': [7775561, 515317, 1091737, 924624, 821128, 513118, 472906, 306678, 273988, 507548],
    'Roubos a Pedestres': [35000, 2500, 15000, 12000, 9000, 10000, 8500, 1000, 2000, 4000]
}

# Cálculos
total_roubos = sum(dados_municipios['Roubos a Pedestres'])
media_roubos = total_roubos / len(dados_municipios['Roubos a Pedestres'])

total_populacao = sum(dados_municipios['Habitantes'])
media_populacao = total_populacao / len(dados_municipios['Habitantes'])

maior_roubo = max(dados_municipios['Roubos a Pedestres'])
menor_roubo = min(dados_municipios['Roubos a Pedestres'])

maior_populacao = max(dados_municipios['Habitantes'])
menor_populacao = min(dados_municipios['Habitantes'])

indice_maior_roubo = dados_municipios['Roubos a Pedestres'].index(maior_roubo)
indice_menor_roubo = dados_municipios['Roubos a Pedestres'].index(menor_roubo)

municipio_maior_roubo = dados_municipios['Município'][indice_maior_roubo]
municipio_menor_roubo = dados_municipios['Município'][indice_menor_roubo]

indice_maior_populacao = dados_municipios['Habitantes'].index(maior_populacao)
indice_menor_populacao = dados_municipios['Habitantes'].index(menor_populacao)

municipio_maior_populacao = dados_municipios['Município'][indice_maior_populacao]
municipio_menor_populacao = dados_municipios['Município'][indice_menor_populacao]

# Cálculo da taxa de roubos a pedestres por município
taxas_roubos = [roubos / habitantes for roubos, habitantes in zip(dados_municipios['Roubos a Pedestres'], dados_municipios['Habitantes'])]

# Resumo final
print("Resumo do Relatório:")
print(f"Total de Roubos a Pedestres: {total_roubos}")
print(f"Média de Roubos a Pedestres: {media_roubos:.2f}")
print(f"Total da População: {total_populacao}")
print(f"Média da População: {media_populacao:.2f}")
print(f"Maior Número de Roubos: {maior_roubo} (em {municipio_maior_roubo})")
print(f"Menor Número de Roubos: {menor_roubo} (em {municipio_menor_roubo})")
print(f"Maior População: {maior_populacao} (em {municipio_maior_populacao})")
print(f"Menor População: {menor_populacao} (em {municipio_menor_populacao})")

# Taxas de roubos a pedestres por município
for municipio, taxa in zip(dados_municipios['Município'], taxas_roubos):
    print(f"Taxa de Roubos a Pedestres em {municipio}: {taxa:.6f}")

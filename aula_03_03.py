# Dados das vendas dos vendedores
vendas = {
    "Maria": [800, 700, 1000, 900, 1200, 600, 600],
    "João": [900, 500, 1100, 1000, 900, 500, 700],
    "Manuel": [700, 600, 900, 1200, 900, 700, 400]
}

# Função para calcular média, maior e menor valor
def analisar_vendas(vendas):
    resultados = {}
    for vendedor, valores in vendas.items():
        media_vendas = sum(valores) / len(valores)
        maior_venda = max(valores)
        menor_venda = min(valores)
        resultados[vendedor] = {
            "Média": media_vendas,
            "Maior Venda": maior_venda,
            "Menor Venda": menor_venda
        }
    return resultados

# Análise
resultados_vendas = analisar_vendas(vendas)

# Resultados
print("Resultados de Vendas dos Últimos 7 Dias:")
for vendedor, resultados in resultados_vendas.items():
    print(f"{vendedor}:")
    print(f"  Média de Venda: R$ {resultados['Média']:.2f}")
    print(f"  Maior Valor Vendido: R$ {resultados['Maior Venda']}")
    print(f"  Menor Valor Vendido: R$ {resultados['Menor Venda']}")

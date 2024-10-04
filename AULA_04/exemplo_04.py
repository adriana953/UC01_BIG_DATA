def calcular_salario_vendedor():
    # Constantes
    salario_minimo = 1212.00  # Valor do salário mínimo
    salario_fixo = 3 * salario_minimo  # Salário fixo do vendedor

    # Leitura dos dados
    nome_vendedor = input("Digite o nome do vendedor: ")
    quantidade_vendida = int(input("Digite a quantidade de carros vendidos: "))
    valor_total_vendas = float(input("Digite o valor total das vendas mensais: "))

    # Cálculo da comissão
    if quantidade_vendida < 10:
        comissao = valor_total_vendas * 0.05  # 5% de comissão
    elif quantidade_vendida <= 20:
        comissao = valor_total_vendas * 0.10  # 10% de comissão
    else:
        comissao = valor_total_vendas * 0.20  # 20% de comissão

    # Cálculo do salário final
    salario_final = salario_fixo + comissao

    # Exibindo os resultados
    print(f"\nVendedor: {nome_vendedor}")
    print(f"Quantidade de carros vendidos: {quantidade_vendida}")
    print(f"Valor total das vendas: R${valor_total_vendas:.2f}")
    print(f"Salário final: R${salario_final:.2f}")

# Chama a função para executar o programa
calcular_salario_vendedor()

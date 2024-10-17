def main():
    # Dados fornecidos
    roubos = [100, 90, 80, 120, 110, 90, 70]
    furtos = [80, 60, 70, 60, 100, 50, 30]
    recuperacoes = [70, 50, 90, 80, 100, 70, 50]

    # Calculando a quantidade total de roubos e furtos
    total_diario = [roubos[i] + furtos[i] for i in range(7)]

    # Calculando a taxa de recuperação
    taxa_recuperacao = []
    for i in range(7):
        if roubos[i] > 0:  # Evitando divisão por zero
            taxa = recuperacoes[i] / roubos[i]
        else:
            taxa = 0
        taxa_recuperacao.append(taxa)

    # Exibindo os resultados
    print("Quantidade de roubos e furtos diários dos últimos 7 dias:", total_diario)
    print("Taxa de recuperação de automóveis diária (últimos 7 dias):", taxa_recuperacao)

if __name__ == "__main__":
    main()

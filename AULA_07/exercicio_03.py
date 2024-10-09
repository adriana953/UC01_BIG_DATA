# Inicializando as listas para armazenar os dados
dados_habitantes = []

# Função para coletar dados dos habitantes
def coletar_dados():
    while True:
        sexo = input("Informe o sexo (masculino/feminino) ou 'sair' para encerrar: ").strip().lower()
        if sexo == 'sair':
            break

        cor_olhos = input("Informe a cor dos olhos (azuis/verdes/castanhos): ").strip().lower()
        cor_cabelos = input("Informe a cor dos cabelos (louros/castanhos/pretos): ").strip().lower()
        idade = int(input("Informe a idade: "))

        dados_habitantes.append({
            'sexo': sexo,
            'cor_olhos': cor_olhos,
            'cor_cabelos': cor_cabelos,
            'idade': idade
        })

# Função para realizar as análises
def analisar_dados():
    if not dados_habitantes:
        print("Nenhum dado foi coletado.")
        return

    idades = [hab['idade'] for hab in dados_habitantes]
    maior_idade = max(idades)
    menor_idade = min(idades)
    media_idade = sum(idades) / len(idades)

    quantidade_feminino_18_35 = sum(1 for hab in dados_habitantes if hab['sexo'] == 'feminino' and 18 <= hab['idade'] <= 35)
    quantidade_olhos_verdes_cabelos_louros = sum(1 for hab in dados_habitantes if hab['cor_olhos'] == 'verdes' and hab['cor_cabelos'] == 'louros')

    # Resultados
    print(f"A maior idade é: {maior_idade}")
    print(f"A menor idade é: {menor_idade}")
    print(f"A média das idades é: {media_idade:.2f}")
    print(f"Quantidade de indivíduos do sexo feminino entre 18 e 35 anos: {quantidade_feminino_18_35}")
    print(f"Quantidade de indivíduos com olhos verdes e cabelos louros: {quantidade_olhos_verdes_cabelos_louros}")

# Execução do programa
coletar_dados()
analisar_dados()


# Função para verificar a aposentadoria
def verificar_aposentadoria():
    # Leitura dos dados
    nome_empregado = input("Digite o nome do empregado: ")
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_entrada = int(input("Digite o ano que entrou na empresa: "))
    
    # Cálculo da idade e do tempo trabalhado
    ano_atual = 2024  # Você pode usar datetime para obter o ano atual dinamicamente
    idade = ano_atual - ano_nascimento
    tempo_trabalhado = ano_atual - ano_entrada
    
    # Verificando se está apto à aposentadoria
    apto = (
        idade >= 65 or
        tempo_trabalhado >= 30 or
        (idade >= 60 and tempo_trabalhado >= 25)
    )
    
    # Exibindo os resultados
    print(f"\nEmpregado: {nome_empregado}")
    print(f"Idade: {idade} anos")
    print(f"Tempo trabalhado: {tempo_trabalhado} anos")
    
    if apto:
        print("Apto a Aposentadoria")
    else:
        print("Inapto a Aposentadoria")

# Chama a função para executar o programa
verificar_aposentadoria()

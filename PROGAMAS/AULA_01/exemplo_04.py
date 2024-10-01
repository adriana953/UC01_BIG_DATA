# Calcular a idade de uma pessoa a partir do ano de nascimento
nome = input("Informe o nome da pessoa: ")
ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = int(input("Informe o ano atual: "))
idade = ano_atual - ano_nascimento
print(f"{nome} tem {idade} anos.")
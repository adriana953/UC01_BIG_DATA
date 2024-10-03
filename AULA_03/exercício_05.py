def pode_doar_sangue(idade, peso, horas_dormidas):
    if 16 <= idade <= 69 and peso > 50 and horas_dormidas >= 6:
        return "Você pode doar sangue."
    else:
        return "Você NÃO pode doar sangue."

# Entrada de dados
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg: "))
horas_dormidas = float(input("Quantas horas você dormiu nas últimas 24 horas? "))

# Chamada da função e exibição do resultado
resultado = pode_doar_sangue(idade, peso, horas_dormidas)
print(resultado)
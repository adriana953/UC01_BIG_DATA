def ler_series():
    serie = []
    for i in range(10):
        numero = int(input(f"Digite o {i + 1}º número: "))
        serie.append(numero)
    return serie

def calcular_operacoes(serie1, serie2):
    soma = []
    subtracao = []
    multiplicacao = []
    divisao = []

    for a, b in zip(serie1, serie2):
        soma.append(a + b)
        subtracao.append(a - b)
        multiplicacao.append(a * b)
        if b != 0:
            divisao.append(a / b)
        else:
            divisao.append("Divisão por zero")

    return soma, subtracao, multiplicacao, divisao

def main():
    print("Digite a primeira série de 10 números:")
    serie1 = ler_series()
    
    print("Digite a segunda série de 10 números:")
    serie2 = ler_series()

    soma, subtracao, multiplicacao, divisao = calcular_operacoes(serie1, serie2)

    print("\nResultados:")
    print("Soma:", soma)
    print("Subtração:", subtracao)
    print("Multiplicação:", multiplicacao)
    print("Divisão:", divisao)

if __name__ == "__main__":
    main()

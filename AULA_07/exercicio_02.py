def main():
    temperaturas = []

    while True:
        entrada = input("Digite uma temperatura (ou 'sair' para finalizar): ")
        
        if entrada.lower() == 'sair':
            break
        
        try:
            temperatura = float(entrada)
            temperaturas.append(temperatura)
        except ValueError:
            print("Por favor, insira um número válido ou 'sair' para finalizar.")

    if temperaturas:
        menor = min(temperaturas)
        maior = max(temperaturas)
        media = sum(temperaturas) / len(temperaturas)

        print(f"\nMenor temperatura: {menor:.2f}°C")
        print(f"Maior temperatura: {maior:.2f}°C")
        print(f"Média das temperaturas: {media:.2f}°C")
    else:
        print("Nenhuma temperatura foi registrada.")

# Chamada da função
main()

# Calcular a idade de uma pessoa a partir do ano de nascimento
def calcular_peso_ideal(altura, sexo):
    if sexo.lower() == 'homem':
        peso_ideal = (72.7 * altura) - 58
    elif sexo.lower() == 'mulher':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        return "Sexo inválido. Por favor, insira 'homem' ou 'mulher'."
    
    return round(peso_ideal, 2)

altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (homem ou mulher): ")

peso_ideal = calcular_peso_ideal(altura, sexo)
print(f"O peso ideal para uma pessoa de {altura}m e sexo {sexo} é: {peso_ideal} kg.")

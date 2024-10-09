def calcular_salario():
    # Entrada de dados
    valor_por_hora = float(input("Digite o valor recebido por hora: R$ "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

    # Cálculo do salário bruto
    salario_bruto = valor_por_hora * horas_trabalhadas

    # Cálculo dos descontos
    irrf = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05

    # Cálculo do salário líquido
    salario_liquido = salario_bruto - (irrf + inss + sindicato)

    # Resultados
    print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
    print(f"Desconto do IRRF: R$ {irrf:.2f}")
    print(f"Desconto do INSS: R$ {inss:.2f}")
    print(f"Desconto do Sindicato: R$ {sindicato:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Chamada da função
calcular_salario()

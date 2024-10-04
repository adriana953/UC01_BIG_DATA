try:
    nome = input("Informe o nome do produto: ")
    qtd = int(input("Informe a quantidade desejada: "))
    valor = float(input("Informe o valor unitário: "))
except ValueError:
    print("Verifique os valores informados")
else:    
    total = valor * qtd
print(f"O valor total sem desconto é R$ {total:.2f}")
if qtd <= 5:
    desc = total * 0.98
elif qtd > 5 and qtd <= 10:
    desc = total * 0.97
else:
    desc = total * 0.95
print(f"O valor total com desconto é R$ {desc:.2f}")    
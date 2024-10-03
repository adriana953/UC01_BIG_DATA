idade = int(input("Informe a idade: "))
if idade < 18:
    print("Você é menor de idade")
elif idade == 18:
    print("Quase lá")
elif idade > 18 and idade < 65:
    print("Acesso Liberado")
else:
    print("Acesso Liberado - Aprecie com Moderação")


 
def verificar_numeros(num1, num2):
    if num1 == num2:
        return "Os números são iguais."
    else:
        return "Os números são diferentes."

# Entrada de dados
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
resultado = verificar_numeros(numero1, numero2)
print(resultado)
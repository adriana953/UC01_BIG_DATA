def ler_notas():
    notas = []
    for i in range(10):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        notas.append(nota)
    return notas

def separar_notas(notas):
    acima_da_media = []
    abaixo_da_media = []
    
    for nota in notas:
        if nota >= 70:
            acima_da_media.append(nota)
        else:
            abaixo_da_media.append(nota)
    
    return acima_da_media, abaixo_da_media

def main():
    print("Digite 10 notas:")
    notas = ler_notas()
    
    acima_da_media, abaixo_da_media = separar_notas(notas)

    print("\nNotas acima ou iguais a 70:", acima_da_media)
    print("Notas abaixo de 70:", abaixo_da_media)

if __name__ == "__main__":
    main()


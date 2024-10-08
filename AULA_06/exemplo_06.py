usuarios = ["Pedro", "Maria", "Jose", "Eduarda", "Dirceu", "Elvis"]
senhas = ["123","345","567","@@2$$$","8919"]
usuario = input("Informe o nome de acesso ao sistema: ")
for i in range(len(usuarios)):
    if usuarios[i] == usuario:
        senha = input("Informe a senha de acesso: ")
        if senhas[i] == senha:
            resp = "Acesso Liberado"
        else:
          resp = ("Senha não confere")
        break
    else:
        resp = "Usuário não Encontrado"
print(resp)
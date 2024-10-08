# Dicionário de usuários e suas senhas
usuarios = {
    "Maria Santos": "senha123",
    "Andrea Campos": "senha345",
    "Marcos Silva": "senha678",
    "Lene Souza": "senha910",
    "Lucas Vianna": "senha911"
}

# Solicitar o nome de usuário
usuario_input = input("Digite seu nome de usuário: ")

# Verificar se o usuário existe
if usuario_input in usuarios:
    # Solicitar a senha
    senha_input = input("Digite sua senha: ")
    
    # Verificar se a senha está correta
    if senha_input == usuarios[usuario_input]:
        print("Acesso liberado")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")

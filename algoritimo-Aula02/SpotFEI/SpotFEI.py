def carregar_usuarios():
    usuarios = {}
    try:
        with open("usuarios.txt", "r") as file:
            for linha in file:
                usuario, senha = linha.strip().split(":")
                usuarios[usuario] = senha  
    except FileNotFoundError:
        pass
    return usuarios

def salvar_usuarios(usuarios):
    with open("usuarios.txt", "w") as file:
        for usuario, senha in usuarios.items():
            file.write(f"{usuario}:{senha}\n")

usuarios = carregar_usuarios()






print("Bem-vindo ao SpotFEI!")

acesso = input("Você deseja se cadastrar (C) ou fazer login (L)? ").upper()

if acesso == 'L':
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Usuário autenticado com sucesso!")
    else:
        print("Usuário não encontrado ou senha incorreta!")

elif acesso == 'C':
    novo_usuario = input("Digite seu novo usuário: ")
    
    if novo_usuario in usuarios:
        print("Usuário já existe!")
    else:
        nova_senha = input("Digite sua nova senha: ")
        usuarios[novo_usuario] = nova_senha
        print("Usuário cadastrado com sucesso!")
        
        salvar_usuarios(usuarios)

else:
    print("Opção inválida!")
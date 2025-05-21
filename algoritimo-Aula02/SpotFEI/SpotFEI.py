import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def carregar_usuarios():
    usuarios = {}
    with open("usuarios.txt", "r") as file:
        for linha in file:
            partes = linha.strip().split(":")
            if len(partes) == 2:
                usuario, senha = partes
                usuarios[usuario] = senha
            else:
                print(f"Linha ignorada (formato inválido): {linha.strip()}")
    return usuarios

def salvar_usuarios(usuarios):
    with open("usuarios.txt", "w") as file:
        for usuario, senha in usuarios.items():
            file.write(f"{usuario}:{senha}\n")

def carregar_musicas():
    musicas = []
    if not os.path.exists("musics.txt"):                        # [ADICIONADO]
        print("Arquivo de músicas não encontrado. Crie um arquivo chamado 'musics.txt'.")  # [ADICIONADO]
        return musicas                                          # [ADICIONADO]
    with open("musics.txt", "r") as file:                       # [MODIFICADO]
        for linha in file:
            linha = linha.strip()
            if linha:
                musicas.append(linha)
    return musicas                                              # [MODIFICADO]

def buscar_musica(musicas, termo):
    resultado = []
    termo = termo.lower()
    for musica in musicas:
        if termo in musica.lower():
            resultado.append(musica)
    return resultado

def carregar_musicas_curtidas():
    curtidas = set()                                            # [MODIFICADO]
    if not os.path.exists("musicas_curtidas.txt"):              # [ADICIONADO]
        open("musicas_curtidas.txt", "w").close()               # [ADICIONADO]
        return curtidas                                         # [ADICIONADO]
    with open("musicas_curtidas.txt", "r") as file:
        for linha in file:
            curtidas.add(linha.strip())
    return curtidas

def salvar_musica_curtida(musica, curtidas):
    with open("musicas_curtidas.txt", "w") as file:
        for m in curtidas:
            file.write(m + "\n")

def carregar_musicas_descurtidas():
    descurtidas = set()                                         # [MODIFICADO]
    if not os.path.exists("musicas_descurtidas.txt"):           # [ADICIONADO]
        open("musicas_descurtidas.txt", "w").close()            # [ADICIONADO]
        return descurtidas                                      # [ADICIONADO]
    with open("musicas_descurtidas.txt", "r") as file:
        for linha in file:
            descurtidas.add(linha.strip())
    return descurtidas

def salvar_musicas_descurtidas(descurtidas):
    with open("musicas_descurtidas.txt", "w") as file:
        for m in descurtidas:
            file.write(m + "\n")

def menu_curtir_musicas(musicas):
    curtidas = carregar_musicas_curtidas()
    descurtidas = carregar_musicas_descurtidas()

    for musica in musicas:
        while True:
            print(f"\nMúsica: {musica}")
            if musica in curtidas:
                print("1. Descurtir")
                print("2. Manter curtida")
                escolha = input("Escolha uma opção: ")
                if escolha == "1":
                    curtidas.remove(musica)
                    descurtidas.add(musica)
                    salvar_musica_curtida(musica, curtidas)
                    salvar_musicas_descurtidas(descurtidas)
                    print("Música descurtida!\n")
                    break
                elif escolha == "2":
                    print("Música permanece curtida.\n")
                    break
                else:
                    print("Opção inválida! Tente novamente.")
            elif musica in descurtidas:
                print("1. Curtir")
                print("2. Manter descurtida")
                escolha = input("Escolha uma opção: ")
                if escolha == "1":
                    descurtidas.remove(musica)
                    curtidas.add(musica)
                    salvar_musica_curtida(musica, curtidas)
                    salvar_musicas_descurtidas(descurtidas)
                    print("Música curtida!\n")
                    break
                elif escolha == "2":
                    print("Música permanece descurtida.\n")
                    break
                else:
                    print("Opção inválida! Tente novamente.")
            else:
                print("1. Curtir")
                print("2. Não curtir")
                escolha = input("Escolha uma opção: ")
                if escolha == "1":
                    curtidas.add(musica)
                    salvar_musica_curtida(musica, curtidas)
                    print("Música curtida!\n")
                    break
                elif escolha == "2":
                    descurtidas.add(musica)
                    salvar_musicas_descurtidas(descurtidas)
                    print("Música não curtida.\n")
                    break
                else:
                    print("Opção inválida! Tente novamente.")

def menu_historico():
    while True:
        print("\n--- GERENCIAR HISTÓRICO ---")
        print("1. Ver músicas curtidas")
        print("2. Ver músicas descurtidas")
        print("3. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            curtidas = carregar_musicas_curtidas()
            if curtidas:
                print("\nMúsicas Curtidas:")
                for m in curtidas:
                    print(f"• {m}")
            else:
                print("\nNenhuma música curtida ainda.")
        elif opcao == "2":
            descurtidas = carregar_musicas_descurtidas()
            if descurtidas:
                print("\nMúsicas Descurtidas:")
                for m in descurtidas:
                    print(f"• {m}")
            else:
                print("\nNenhuma música descurtida ainda.")
        elif opcao == "3":
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_principal(nome_usuario):
    musicas = carregar_musicas()

    while True:
        print(f"\n--- MENU PRINCIPAL ({nome_usuario}) ---")
        print("1. Buscar música")
        print("2. Gerenciar histórico")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            termo = input("Digite o nome da música ou artista para buscar: ")
            resultados = buscar_musica(musicas, termo)
            if resultados:
                print("\nResultados encontrados:")
                for r in resultados:
                    print(f"• {r}")
                menu_curtir_musicas(resultados)
            else:
                print("Nenhuma música encontrada com esse termo.")
        elif opcao == "2":
            menu_historico()
        elif opcao == "3":
            print("Saindo do SpotFEI. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

usuarios = carregar_usuarios()

print("Bem-vindo ao SpotFEI!")

acesso = input("Você deseja se cadastrar (C) ou fazer login (L)? ").upper()

if acesso == 'L':
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Usuário autenticado com sucesso!")
        menu_principal(usuario)
    else:
        print("Usuário não encontrado ou senha incorreta!")

elif acesso == 'C':
    novo_usuario = input("Digite seu novo usuário: ")

    if novo_usuario in usuarios:
        print("Usuário já existe!")
    else:
        nova_senha = input("Digite sua nova senha: ")
        usuarios[novo_usuario] = nova_senha
        salvar_usuarios(usuarios)
        print("Usuário cadastrado com sucesso!")
        menu_principal(novo_usuario)

else:
    print("Opção inválida!")


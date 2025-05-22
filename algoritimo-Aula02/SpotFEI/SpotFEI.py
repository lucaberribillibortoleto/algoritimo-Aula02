import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def carregar_usuarios():
    usuarios = {}
    try:
        arquivo = open("usuarios.txt", "r")
        linhas = arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split(":")
            if len(partes) == 2:
                usuario, senha = partes
                usuarios[usuario] = senha
        arquivo.close()
    except:
        arquivo = open("usuarios.txt", "w")
        arquivo.close()
    return usuarios

def salvar_usuarios(usuarios):
    arquivo = open("usuarios.txt", "w")
    for usuario, senha in usuarios.items():
        linha = "%s:%s\n" % (usuario, senha)
        arquivo.write(linha)
    arquivo.close()

def carregar_musicas():
    musicas = []
    arquivo = open("musics.txt", "r")
    linhas = arquivo.readlines()
    for linha in linhas:
        linha = linha.strip()
        if linha:
            musicas.append(linha)
    arquivo.close()
    return musicas

def buscar_musica(musicas, busca):
    resultado = []
    busca = busca.lower()
    for musica in musicas:
        if busca in musica.lower():
            resultado.append(musica)
    return resultado

def carregar_musicas_curtidas():
    curtidas = set()
    try:
        arquivo = open("musicas_curtidas.txt", "r")
        linhas = arquivo.readlines()
        for linha in linhas:
            curtidas.add(linha.strip())
        arquivo.close()
    except:
        arquivo = open("musicas_curtidas.txt", "w")
        arquivo.close()
    return curtidas

def salvar_musica_curtida(musica, curtidas):
    arquivo = open("musicas_curtidas.txt", "w")
    for m in curtidas:
        arquivo.write("%s\n" % m)
    arquivo.close()

def carregar_musicas_descurtidas():
    descurtidas = set()
    try:
        arquivo = open("musicas_descurtidas.txt", "r")
        linhas = arquivo.readlines()
        for linha in linhas:
            descurtidas.add(linha.strip())
        arquivo.close()
    except:
        arquivo = open("musicas_descurtidas.txt", "w")
        arquivo.close()
    return descurtidas

def salvar_musicas_descurtidas(descurtidas):
    arquivo = open("musicas_descurtidas.txt", "w")
    for m in descurtidas:
        arquivo.write("%s\n" % m)
    arquivo.close()

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
                    print(f"- {m}")
            else:
                print("\nNenhuma música curtida.")
        elif opcao == "2":
            descurtidas = carregar_musicas_descurtidas()
            if descurtidas:
                print("\nMúsicas Descurtidas:")
                for m in descurtidas:
                    print(f"- {m}")
            else:
                print("\nNenhuma música descurtida.")
        elif opcao == "3":
            break

def carregar_playlists(usuario):
    playlists = {}
    nome_arquivo = "playlists_" + usuario + ".txt"
    try:
        arquivo = open(nome_arquivo, "r")
        linhas = arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split(":")
            if len(partes) == 2:
                nome = partes[0]
                musicas = partes[1].split(",") if partes[1] else []
                playlists[nome] = musicas
        arquivo.close()
    except:
        arquivo = open(nome_arquivo, "w")
        arquivo.close()
    return playlists

def salvar_playlists(usuario, playlists):
    nome_arquivo = "playlists_" + usuario + ".txt"
    arquivo = open(nome_arquivo, "w")
    for nome, musicas in playlists.items():
        linha = nome + ":" + ",".join(musicas) + "\n"
        arquivo.write(linha)
    arquivo.close()

def menu_playlists(usuario, musicas_disponiveis):
    playlists = carregar_playlists(usuario)

    while True:
        print("\n--- GERENCIAR PLAYLISTS ---")
        print("1. Ver playlists")
        print("2. Criar nova playlist")
        print("3. Excluir playlist")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if not playlists:
                print("\nNenhuma playlist criada.")
            else:
                for nome, musicas in playlists.items():
                    print(f"\nPlaylist: {nome}")
                    if musicas:
                        for m in musicas:
                            print(f"- {m}")
                    else:
                        print("  (nenhuma musica)")
        elif opcao == "2":
            nome_playlist = input("Nome da playlist: ")
            if nome_playlist in playlists:
                print("Essa playlist já existe.")
            else:
                nova = []
                while True:
                    busca = input("Buscar música para a playlist: ")
                    if not busca:
                        break
                    resultados = buscar_musica(musicas_disponiveis, busca)
                    if resultados:
                        print("Resultados:")
                        for m in resultados:
                            print(f"- {m}")
                        escolha = input("Digite o nome da música para adicionar: ")
                        if escolha in resultados:
                            nova.append(escolha)
                        else:
                            print("Música não encontrada.")
                playlists[nome_playlist] = nova
                salvar_playlists(usuario, playlists)
                print("Playlist criada!")
        elif opcao == "3":
            nome = input("Nome da playlist que o usuario quer excluir: ")
            if nome in playlists:
                del playlists[nome]
                salvar_playlists(usuario, playlists)
                print("Playlist excluída.")
        elif opcao == "4":
            break

def menu_principal(nome_usuario):
    musicas = carregar_musicas()

    while True:
        print(f"\nMENU PRINCIPAL ({nome_usuario})")
        print("1. Buscar música")
        print("2. Gerenciar histórico")
        print("3. Gerenciar playlists")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            busca = input("Digite o nome da música ou artista para buscar: ")
            resultados = buscar_musica(musicas, busca)
            if resultados:
                print("\n Músicas encontradas:")
                for r in resultados:
                    print(f"- {r}")
                menu_curtir_musicas(resultados)
            else:
                print("Nenhuma música encontrada.")
        elif opcao == "2":
            menu_historico()
        elif opcao == "3":
            menu_playlists(nome_usuario, musicas)
        elif opcao == "4":
            print("Saindo do SpotFEI.")
            break

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
        print("Este usuário não existe!")

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

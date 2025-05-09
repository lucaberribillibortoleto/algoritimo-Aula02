print("Bem vindo ao SpotFEI!")
acesso = (input("você deseja se cadastrar 'C' ou fazer login 'L'? "))
senhas = ['123']

if acesso == 'L':
    senha = (input("Digite sua senha: "))
    if senha in (senhas):
        print("usuario existente!")
    else:
        print("usuario não encontrado!")
elif acesso == 'C':
    usuario = (input("Digite seu usuario: "))
    senha = (input("Digite sua senha: "))
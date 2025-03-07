ano_atual = int(input("Ano Atual:"))
ano_nascimento = int(input("Ano Nascimento:"))

idade = ano_atual - ano_nascimento

if idade >= 18:
    print ("Ja pode tirar CNH")

M= []

for num_linha in range(10):
    linha = []
    for num_coluna in range(15):
        linha.append(num_linha + num_coluna)
    M.append(linha)

for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print("%4d" % M[linha][coluna], end=" ")
    print()
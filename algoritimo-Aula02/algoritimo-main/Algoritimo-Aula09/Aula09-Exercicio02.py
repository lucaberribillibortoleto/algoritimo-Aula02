from random import randint, random
M = []

for num_linha in range(10):
    matriz = [] 
    for num_coluna in range(15):
        matriz.append(randint(0,10))
    M.append(matriz)

for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print("%4d" %M[linha][coluna], end=" ")
    print()
for linha in range(len(M)):
    print("%4d" %M[linha][0])
    


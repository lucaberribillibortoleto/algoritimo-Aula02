import random
M = []
for num_linha in range(12):
    linha = []
    for num_coluna in range(12):
        linha.append(random.randint(0, 10))  
    M.append(linha)
ask = input('').strip().upper()
print("Matriz criada:")
for linha in M:
    for elemento in linha:
        print("%3d" % elemento, end=" ")
    print()

soma = 0
contador = 0

for i in range(12):
    for j in range(12):
        if i + j > 11:
            soma += M[i][j]
            contador += 1

if ask == 'S':
    print(f"Resultado da conta: {soma}")
elif ask == 'M':
    media = soma // contador 
    print(f"Resultado da conta: {media}")
else:
    print("Operação inválida. Digite apenas 'S' ou 'M'.")
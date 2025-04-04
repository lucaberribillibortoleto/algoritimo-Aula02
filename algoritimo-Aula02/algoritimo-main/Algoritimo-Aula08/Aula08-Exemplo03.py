z = []
for i in range (10):
    numero = int(input("Digite um número: "))
    z.append(numero)
    lista = sorted(z)
for indice in range(len(z)):
    if z[indice] == lista[9]:
        print(z)
        print("Maior valor: ", lista[9])
        print("indice maior valor: ", indice)


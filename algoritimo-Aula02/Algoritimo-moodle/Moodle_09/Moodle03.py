def media(lista):
    if len(lista) == 0:
        return 0  
    return sum(lista) / len(lista)  


valores = []


quantidade = int(input("Quantos números você quer inserir? "))

for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    valores.append(numero)


resultado = media(valores)
print(f"A média dos valores é: {resultado:.2f}")
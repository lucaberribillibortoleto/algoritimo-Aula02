distancia = float(input("distancia que deseja percorrer?:"))

if distancia <= 200:
    preco = distancia * 0.50
    print (f"O preco sera:{preco:.2f}")

else:
    preco = distancia * 0.45
    print (f"O preco sera:{preco:.2f}")
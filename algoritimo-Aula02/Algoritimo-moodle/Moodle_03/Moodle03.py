a = (input("Você deseja calcular o volume do dodecaedro ou icosaedro: "))
aresta = float(input("Digite o valor da aresta a em metros: "))

if a == "dodecaedro":
    dodecaedro = ((15+7*5**0.5)/4)*aresta**3
    print(f"O volume de um dodecaedro regular com {aresta:.2f} de aresta é: {dodecaedro:.2f}")
   
if a == "icosaedro":
    icosaedro = 5/12*(3+5**0.5)*aresta**3
    print(f"O volume de um icosaedro regular com {aresta:.2f} de aresta é: {icosaedro:.2f}")

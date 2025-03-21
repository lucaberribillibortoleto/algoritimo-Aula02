preço_produto = float(input("digite o preço do produto:"))
codigo_origem = int(input("digite o codigo de origem:"))

if codigo_origem == 1: 
    print (f"o produto é do Sul e seu preço é: R${preço_produto}") 
elif codigo_origem == 2:
    print (f"o produto é do Norte e seu preço é: R${preço_produto}")
elif codigo_origem == 3:
    print (f"o produto é do Leste e seu preço é: R${preço_produto}")
elif codigo_origem == 4:
     print (f"o produto é do Oeste e seu preço é: R${preço_produto}")
elif codigo_origem == 5 or codigo_origem == 6:
     print (f"o produto é do Nordeste e seu preço é: R${preço_produto}")
elif codigo_origem == 7 or codigo_origem == 8 or codigo_origem == 9:
    print (f"o produto é do Sudeste e seu preço é: R${preço_produto}")
elif codigo_origem >= 10 or codigo_origem <= 20:
     print (f"o produto é do Centro-Oeste e seu preço é: R${preço_produto}")
elif codigo_origem >= 25 or codigo_origem <= 30:
     print (f"o produto é do Nordeste e seu preço é: R${preço_produto}")

else: 
     print (f"O produto é importado: R${preço_produto}")





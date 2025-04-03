def area(base,altura):
    return(base * altura)/2

while(True):
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))

    print("A  area desse triangulo será: ", area(base,altura))

    continua = input("Quer calcular a area de mais um triangulo? S / N ")

    if continua != 'S':
        break


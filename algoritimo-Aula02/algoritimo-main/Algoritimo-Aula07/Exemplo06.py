def valor(n1,n2,n3):
    num = (n1**0.5) + (n2**0.5) + (n3**0.5) + (n1 + n2)/2 + (n2 + n3)/2 + (n1 + n3)/2
    return  num

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

print("o resultado do cálculo será: ", valor(n1,n2,n3))
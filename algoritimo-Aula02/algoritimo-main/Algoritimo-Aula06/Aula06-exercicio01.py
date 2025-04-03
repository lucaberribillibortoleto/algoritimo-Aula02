qtde = int(input("Digite a quantidade de numeros a serem testados:"))
cont_primos = 0

for i in range(0,qtde):
    num = int(input(f"digite o numero{i}: "))
    if num > 1:
        eh_primo = True 
        for j in range(2,num):
            if num % j == 0:
                eh_primo = False
                break
        if eh_primo:
            cont_primos = cont_primos + 1

print("Total de numeros: ", qtde)
print("Total de primos: ", cont_primos)
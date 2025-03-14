p1=float(input("Digite o valor do primeiro produto: "))
p2=float(input("Digite o valor do segundo produto: "))
p3=float(input("Digite o valor do terceiro produto: "))

somatoria = p1 + p2 + p3

if somatoria > 500:
    total = somatoria * 20/100
    print(f"Desconto: {total:.2f}")

if somatoria <= 500:
    total = somatoria * 10/100
    print(f"Desconto: {total:.2f}")
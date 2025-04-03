salario = int(input("Valor do salario?:"))

if salario > 1250:
    salario = salario * 1.1
    print(f"O salario sera:{salario:.2f}")

else:
    salario = salario * 1.15
    print(f"O salario sera:{salario:.2f}")

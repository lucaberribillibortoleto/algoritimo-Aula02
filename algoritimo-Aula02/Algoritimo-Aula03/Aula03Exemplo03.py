salario = float(input("Digite o valor do salario atual: "))
if salario < 1800:
    novo_salario = salario * 1.1
    print("O funcionario tem direito a 10% de aumento")
    print("O novo salario ser de R$ %.2f" % novo_salario)
    print("Parabens pelo novo salario!!!")
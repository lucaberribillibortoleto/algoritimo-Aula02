def data_magica(dia,mes,ano):
    ano2 = ano % 100
    multi = dia * mes
    if ano2 == multi:
        return True
    else:
        return False
    
d = int(input("Digite o dias: "))
m = int(input("Digite o mes: "))
a = int(input("Digite o ano: "))

if data_magica(d,m,a):
    print(F"Data Magica: {d}/{m}/{a}")
else:
    print(F"Não é Data Magica: {d}/{m}/{a}")
    
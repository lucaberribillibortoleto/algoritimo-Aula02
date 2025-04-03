def data_magica(dia,mes,ano):
    ano2 = ano % 100
    multi = dia * mes
    if ano2 == multi:
        return True
    else:
        return False


for ano in range(1901,2001):
    for mes in range(1,13):
        for dia in range(1,32):
            if data_magica(dia,mes,ano):
                print(F"Data Magica: {dia}/{mes}/{ano}")


    
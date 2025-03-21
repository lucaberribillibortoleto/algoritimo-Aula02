dias = int(input("a quantidade de dias:"))
horas = int(input("quantidade de horas:"))
min = int(input("quantidade de minutos:"))
sec = int(input("quantidade de segundos"))
total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (min *  60) + sec
print ("Tempo total é:", total)

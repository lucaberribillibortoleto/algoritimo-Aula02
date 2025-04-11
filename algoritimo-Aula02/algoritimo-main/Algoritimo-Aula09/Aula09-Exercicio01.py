from random import randint, random
listaInt = []
listaReais = []
listaString = ["sla", "ae", "sol", "nael", "nick", "luar", "marlon"]
for x in range(10):
    listaInt.append(randint(0, 10))
for x in range(5):
     listaReais.append(random() * 10)
listaFinal = [listaInt, listaReais, listaString]
del listaInt
del listaReais
del listaString
print(listaFinal)

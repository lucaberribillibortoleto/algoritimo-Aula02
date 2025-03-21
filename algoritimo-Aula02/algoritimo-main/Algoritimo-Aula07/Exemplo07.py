def doador(genero,peso):
    if (genero == "F" and peso >= 50) or (genero == "M" and peso >= 60):
        return True
    else:
        return False
    
g = input("Informe o genero (F / M): ")
p = int(input("Informe o peso: "))

if doador(g,p):
    print("Pode doar!")
else:
     print("Não pode doar!")

       
        

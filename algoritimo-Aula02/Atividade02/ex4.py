valor = float(input("Digite o valor da compra: "))
quant_parcelas = int(input("Digite a quantidade de parcelas: "))

if valor > 5000:
    isc_total = valor * (5/100)
    if quant_parcelas == 1:
         disc_total = valor * (1/10) 
         total = valor - disc_total
         print(f"Valor final da compra com desconto: {total:.2f}")
         print(f"Desconto total: {disc_total:.2f}")
         print(f"Desconto total: {disc_total:.2f}") 

    elif quant_parcelas == 2 or 3:
         disc_total = valor * (5/100)
         total = valor - disc_total
         parcela = total / quant_parcelas
         print(f"Desconto total: {disc_total:.2f}")
         print(f"Valor final da compra com desconto: {total:.2f}")
         print(f"Cada parcela será de: {parcela:.2f}")
    


    elif quant_parcelas >= 4:
      disc_total = valor *  (5/100)
      total =  valor - disc_total
      parcela = total - disc_total
      print(f"Desconto total: {disc_total:.2f}")
      print(f"Cada parcela será de: {parcela:.2f}")
      print(f"Valor final da compra com desconto: {total:.2f}")


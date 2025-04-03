L = int(input("numero de linhas: "))
C = int(input("numero de colunas: "))

for i in range (L):
 for j in range (C):
    if i == 0 or i == (L-1) or j == 0 or j ==(C-1):
        #
       print(" * "  end='')  #
    else:
      print("  ", end='')
 print()
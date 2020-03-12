line1 = input().split()

codigo = int(line1[0])
quantidade = int(line1[1])

if codigo == 1:
    valorTotal = quantidade * 4.00
elif codigo == 2:
    valorTotal = quantidade * 4.50
elif codigo == 3:
    valorTotal = quantidade * 5.00
elif codigo == 4:
    valorTotal = quantidade * 2.00
elif codigo == 5:
    valorTotal = quantidade * 1.50

print("Total: R$ {:.2f}".format(valorTotal))

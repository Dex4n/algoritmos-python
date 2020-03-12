qntDias = int(input())

ano = int(qntDias / 365)
qntDias = int(qntDias % 365)
mes = int(qntDias / 30)
dias = int(qntDias % 30)

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dias))

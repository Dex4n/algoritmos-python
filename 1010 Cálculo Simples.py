
line1 = input().split()
cod1 = int(line1[0])
nump1 = float(line1[1])
valor1 = float(line1[2])


line2 = input().split()
cod2 = int(line2[0])
nump2 = float(line2[1])
valor2 = float(line2[2])


xt = (nump1 * valor1) + (nump2 * valor2)


print('VALOR A PAGAR: R$','{:.2f}'.format(xt))


'''

12 1 5.30
16 2 5.10

VALOR A PAGAR: R$ 15.50

13 2 15.30
161 4 5.20

VALOR A PAGAR: R$ 51.40

1 1 15.10
2 1 15.10

VALOR A PAGAR: R$ 30.20

'''
valor = float(input())


aumentar = valor * 100
nota100 = int(aumentar / 10000)
aumentar = aumentar % 10000
nota50 = int(aumentar / 5000)
aumentar = aumentar % 5000
nota20 = int(aumentar / 2000)
aumentar = aumentar % 2000
nota10 = int(aumentar / 1000)
aumentar = aumentar % 1000
nota05 = int(aumentar / 500)
aumentar = aumentar % 500
nota02 = int(aumentar / 200)
aumentar = aumentar % 200


moeda1 = int(aumentar / 100)
aumentar = aumentar % 100
moeda050 = int(aumentar / 50)
aumentar = aumentar % 50
moeda025 = int(aumentar / 25)
aumentar = aumentar % 25
moeda010 = int(aumentar / 10)
aumentar = aumentar % 10
moeda005 = int(aumentar / 5)
aumentar = aumentar % 5
moeda001 = int(aumentar / 1)
aumentar = aumentar % 1


print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(nota100))
print("{} nota(s) de R$ 50.00".format(nota50))
print("{} nota(s) de R$ 20.00".format(nota20))
print("{} nota(s) de R$ 10.00".format(nota10))
print("{} nota(s) de R$ 5.00".format(nota05))
print("{} nota(s) de R$ 2.00".format(nota02))


print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(moeda1))
print("{} moeda(s) de R$ 0.50".format(moeda050))
print("{} moeda(s) de R$ 0.25".format(moeda025))
print("{} moeda(s) de R$ 0.10".format(moeda010))
print("{} moeda(s) de R$ 0.05".format(moeda005))
print("{} moeda(s) de R$ 0.01".format(moeda001))

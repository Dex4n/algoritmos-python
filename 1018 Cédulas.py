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
nota01 = int(aumentar / 100)
aumentar = aumentar % 100


print("{:.0f}".format(valor))
print("{} nota(s) de R$ 100,00".format(nota100))
print("{} nota(s) de R$ 50,00".format(nota50))
print("{} nota(s) de R$ 20,00".format(nota20))
print("{} nota(s) de R$ 10,00".format(nota10))
print("{} nota(s) de R$ 5,00".format(nota05))
print("{} nota(s) de R$ 2,00".format(nota02))
print("{} nota(s) de R$ 1,00".format(nota01))

from math import sqrt

line1 = input().split()
px1 = float(line1[0])
py1 = float(line1[1])

line2 = input().split()
px2 = float(line2[0])
py2 = float(line2[1])

diferenca = (px1 - px2) ** 2 + (py1 - py2) ** 2

print("{:.4f}".format(sqrt(diferenca)))

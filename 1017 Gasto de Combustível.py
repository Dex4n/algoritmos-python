AUTONOMIA = 12

horasViagem = int(input())
velocidadeMedia = int(input())

quantidadeLitros = (horasViagem * velocidadeMedia) / AUTONOMIA

print("{:.3f}".format(quantidadeLitros))

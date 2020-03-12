


for valor in range(1,6):
    print("Valor na posição ({}) {}".format(valor-1,valor))


for valor2 in range(2,102,2):
    print("Valor 2 na posição ({}) {}".format(valor2 - 1, valor2))





Valores = [9,8,7,12,0,13,21]

Pares = []
Impares = []

for elementos in Valores:
    if elementos % 2 == 0:
        Pares.append(elementos)
    else: Impares.append(elementos)
print("Pares: {}".format(Pares))
print("Ímpares: {}".format(Impares))




notaAluno = [7.5, 8.5, 9.0, 10.0, 4.0]
mediaAluno = sum(notaAluno) / len(notaAluno)
print("Média do aluno é: {}".format(mediaAluno))
print(5 * "---X---")



notaAluno2 = [0,0,0,0,0]
contador = 0
somaNota = 0


for x in range(0,5):
    notaAluno2[x] = float(input("Digite a nota na posição ({}): ".format(x)))
    somaNota += notaAluno2[x]
    contador+=1


mediaAluno2 = somaNota / contador

print("Média do aluno é: {}".format(mediaAluno2))



notasTeste = [0,0,0]

notasTeste[0] = eval(input("Digite nota1: "))
notasTeste[1] = eval(input("Digite nota2: "))
notasTeste[2] = eval(input("Digite nota3: "))


print(notasTeste[0])
print(notasTeste[1])
print(notasTeste[2])

Compras = []
Valor = []

while True:
    produto = input("Produto: ")
    valor = eval(input("Digite o valor do produto: "))


    if produto == "fim":
        break
    Compras.append(produto)
    Valor.append(valor)


for produtos in Compras:
    print(produtos)

for produtos in Valor:
    print(produtos)






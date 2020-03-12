x = 1

while (3 >= x):
    print(x)
    x = x+1

fim=int(input("Digite o último número a ser impresso: "))
x=1
while (x <= fim):
    print(x)
    x=x+1

numero = int(input("Tabuada de: "))
x = 1
while (x <= 10):
    print(x*numero)
    x=x+1

soma = 0

while True:
    valor = int(input("Digite um número a somar ou 0 para sair: "))
    if valor == 0:
        break
    soma = soma + valor
print(soma)


tabuada = 1

while (tabuada <= 10):
    numero = 1
    while (numero <= 10):
        print("%d x %d = %d"%(tabuada, numero, tabuada * numero))
        numero+=1
    tabuada+=1












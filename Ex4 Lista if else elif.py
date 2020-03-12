valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

print("(%d) Primeiro valor \n"
      "(%d) Segundo valor"%(valor1,valor2))

valor1, valor2 = valor2, valor1

print("(%d) Primeiro valor após troca \n"
      "(%d) Segundo valor após troca"%(valor1,valor2))
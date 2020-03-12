salarioBruto = 0.00
calculoIRRF = 0.00
calculoINSS = 0.00
calculoFGTS = 0.00
totalDesconto = 0.00
totalLiquido = 0.00



valorHora = float(input("Digite o valor por hora: "))
quantidadeHora = float(input("Digite a quantidade de horas: "))

salarioBruto = valorHora * quantidadeHora

if salarioBruto <= 900:
    calculoIRRF = 0
    calculoINSS = (salarioBruto * 0.10)
    calculoFGTS = (salarioBruto * 0.11)
    totalDesconto = calculoIRRF + calculoINSS
    totalLiquido = salarioBruto - totalDesconto
    print("Salário bruto: ({:.2f} * {:.2f}): R$ {:.2f}".format(valorHora, quantidadeHora, salarioBruto))
    print("(-) IR (ISENTO)     : R$ {:.2f}".format(calculoIRRF))
    print("(-) INSS (10%)      : R$ {:.2f}".format(calculoINSS))
    print("FGTS (11%)          : R$ {:.2f}".format(calculoFGTS))
    print("Total de descontos  : R$ {:.2f}".format(totalDesconto))
    print("Salário líquido     : R$ {:.2f}".format(totalLiquido))

elif salarioBruto > 900 and salarioBruto <= 1500:
    calculoIRRF = (salarioBruto * 0.05)
    calculoINSS = (salarioBruto * 0.10)
    calculoFGTS = (salarioBruto * 0.11)
    totalDesconto = calculoIRRF + calculoINSS
    totalLiquido = salarioBruto - totalDesconto
    print("Salário bruto: ({:.2f} * {:.2f}): R$ {:.2f}".format(valorHora, quantidadeHora, salarioBruto))
    print("(-) IR (5%)         : R$ {:.2f}".format(calculoIRRF))
    print("(-) INSS (10%)      : R$ {:.2f}".format(calculoINSS))
    print("FGTS (11%)          : R$ {:.2f}".format(calculoFGTS))
    print("Total de descontos  : R$ {:.2f}".format(totalDesconto))
    print("Salário líquido     : R$ {:.2f}".format(totalLiquido))

elif salarioBruto > 1500 and salarioBruto <= 2500:
    calculoIRRF = (salarioBruto * 0.10)
    calculoINSS = (salarioBruto * 0.10)
    calculoFGTS = (salarioBruto * 0.11)
    totalDesconto = calculoIRRF + calculoINSS
    totalLiquido = salarioBruto - totalDesconto
    print("Salário bruto: ({:.2f} * {:.2f}): R$ {:.2f}".format(valorHora, quantidadeHora, salarioBruto))
    print("(-) IR (10%)        : R$ {:.2f}".format(calculoIRRF))
    print("(-) INSS (10%)      : R$ {:.2f}".format(calculoINSS))
    print("FGTS (11%)          : R$ {:.2f}".format(calculoFGTS))
    print("Total de descontos  : R$ {:.2f}".format(totalDesconto))
    print("Salário líquido     : R$ {:.2f}".format(totalLiquido))

elif salarioBruto > 2500:
    calculoIRRF = (salarioBruto * 0.20)
    calculoINSS = (salarioBruto * 0.10)
    calculoFGTS = (salarioBruto * 0.11)
    totalDesconto = calculoIRRF + calculoINSS
    totalLiquido = salarioBruto - totalDesconto
    print("Salário bruto: ({:.2f} * {:.2f}): R$ {:.2f}".format(valorHora, quantidadeHora, salarioBruto))
    print("(-) IR (20%)        : R$ {:.2f}".format(calculoIRRF))
    print("(-) INSS (10%)      : R$ {:.2f}".format(calculoINSS))
    print("FGTS (11%)          : R$ {:.2f}".format(calculoFGTS))
    print("Total de descontos  : R$ {:.2f}".format(totalDesconto))
    print("Salário líquido     : R$ {:.2f}".format(totalLiquido))




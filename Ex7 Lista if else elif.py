AUMENTO20 = 0.20
AUMENTO15 = 0.15
AUMENTO10 = 0.10
AUMENTO05 = 0.05
percentualAumento = ""
aumentoSalario = 0.0
salarioAjustado = 0.0



salarioAnterior = float(input("Digite o salário: "))

if salarioAnterior <= 280:
    percentualAumento = "20%"

    aumentoSalario = (salarioAnterior * AUMENTO20)

    salarioAjustado = salarioAnterior + aumentoSalario

elif salarioAnterior > 280 and salarioAnterior <= 700:
    percentualAumento = "15%"

    aumentoSalario = (salarioAnterior * AUMENTO15)

    salarioAjustado = salarioAnterior + aumentoSalario

elif salarioAnterior > 700 and salarioAnterior < 1500:
    percentualAumento = "10%"

    aumentoSalario = (salarioAnterior * AUMENTO10)

    salarioAjustado = salarioAnterior + aumentoSalario

elif salarioAnterior >= 1500:
    percentualAumento = "05%"

    aumentoSalario = (salarioAnterior * AUMENTO05)

    salarioAjustado = salarioAnterior + aumentoSalario

print("Salário anterior: ",salarioAnterior)
print("Percentual de ajuste: ",percentualAumento)
print("Valor do ajuste: ",aumentoSalario)
print("Novo salário: ",salarioAjustado)
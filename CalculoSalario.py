#Recebe o valor pago ao trabalhador por hora trabalhada.
valor_por_hora=0.0
#Recebe o valor da quantidade de horas trabalhadas pelo trabalhador no mês.
numero_horas_trabalhadas=0.0
#Esta variável irá fazer a operação de cálculo (multiplicação) entre a variável valor_por_hora e a variável numero_horas_trabalhadas.
calculo_salario=0.0


valor_por_hora=float(input('Quanto você ganha por hora? \n'))
numero_horas_trabalhadas=float(input('Diga a quantidade de horas trabalhadas no mês: \n'))

#Implementação do cálculo (multiplicação) entre as variáveis valor_por_hora e a variável numero_horas_trabalhadas.
calculo_salario = valor_por_hora * numero_horas_trabalhadas


INSS=0.08
FGTS=0.11


calculo_inss = calculo_salario * INSS
calculo_fgts = calculo_salario * FGTS
descontoTotal = calculo_fgts + calculo_inss
salarioLiquido = calculo_salario - descontoTotal

print('Salário bruto: %.2f' %(calculo_salario))
print('Total de desconto INSS: %.2f' %(calculo_inss))
print('Total de desconto FGTS: %.2f' %(calculo_fgts))
print('Total de descontos: %.2f' %(descontoTotal))
print('Total salário líquido: %.2f' %(salarioLiquido))
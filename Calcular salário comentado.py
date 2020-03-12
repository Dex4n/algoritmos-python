'''
8 - Faça um programa que pergute quanto você ganhe por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''



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


print ('O seu salário mensal é de R$ {0} reais mensal.'.format(calculo_salario))


espaco=input('     ')

#Ou breakpoint()



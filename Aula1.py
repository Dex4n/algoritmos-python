'''

print ('Olá \n Mundo')
print ('\n')
print ((12+5)*9)
print ('\n')
print (13*5/12)
print ('\n')
print ((13*5)/12)
print ('\n')
print ('7'+'4')
print ('\n')
print ('Olá', 5)
print ('\n')

nome='Alexandre'
idade=21
peso=60

print (nome, idade, peso)
print ('\n')

'''


#Comentário simples

'''
Comentário 
Grande
'''
print ('\n')
nome=input('Qual seu nome? ')
idade=input('Qual sua idade? ')
peso=input('Qual seu peso? ')

print ('Prazer, ',nome,', sua idade é: ',idade,' e seu peso é: ', peso)

dia='13'
mes='03'
ano='2019'

print ('Hoje é dia {1}/{0}/{2}'.format(dia,mes,ano))

'''
Gosto de pizza, mas r$ 50 reais é muito caro para uma pizza. Um valor aceitável
para uma pizza seria r$30 reais.
Índices: a=pizza b=50 c=30
'''

alimento='pizza'
valor_alimento=50
valor_aceitavel=30

print ('Gosto de {0}, mas R$ {1} reais é muito caro para uma {0}. Um valor aceitável para uma {0} seria R$ {2} reais.'.format(alimento, valor_alimento,valor_aceitavel))

nota_1=int(input('Digite a primeira nota: '))
nota_2=int(input('Digite a segunda nota: '))

soma_das_notas=nota_1+nota_2
print('A soma da primeira nota com a segunda nota é: ', soma_das_notas)

nome_pg_19=input('Qual seu nome? ')
print ('%s é seu nome!' %(nome_pg_19))




numero1=0.00
numero2=0.00
soma_numero1_numero2=0.00



numero1=float(input('Digite um número: \n'))
numero2=float(input('Digite outro número: \n'))


soma_numero1_numero2 = numero1 + numero2

print('A soma entre %.2f e %.2f é: %.2f' %(numero1,numero2,soma_numero1_numero2))






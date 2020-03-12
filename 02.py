'''4) Escreva uma TAD que implemente uma lista circular ordenada
duplamente encadeada que armazena em cada nó uma chave inteira e um
nome. As seguintes operações abaixo devem ser definidas: a)Buscar um
nome dado o valor da chave;
b) Inserir um novo elemento na lista mantendo a ordem;
c) Remover um elemento da lista;
d) Imprimir os valores da lista;
e) Copiar uma lista l1 para uma lista l2;
f) Concatenar uma lista l1 com uma lista l2;
g) Intercalar l1 e l2;'''

from os import system

chave = 0
lista1 = []
lista2 = []

while True:
   print('Menu:\n'
         '1 - Buscar um nome dado o valor da chave\n'
         '2 - Inserir um novo elemento na lista mantendo a ordem\n'
         '3 - Remover um elemento da lista pelo CPF\n'
         '4 - Imprimir os valores da lista\n'
         '5 - Buscar um nome pelo valor do CPF\n'
         '6 - Transformar a lista circular em duas listas L1 e L2, listando-as\n'   
         '7 - Intercalar l1 e l2\n'
         '8 - Sair')

   op = input('Sérgio, Escolha a opcao desejada: ')
   if int(op) == 1:
       try:
           buscaChave = input('Sérgio, agora digite a chave para busca, por gentileza: ')
           for i in range(len(lista1)):
               if int(buscaChave) == lista1[i][0]:
                   print('Nome: {}'.format(lista1[i][1]))
                   print('--------------------------')

           if len(lista1) == 0:
               print('Lista vazia, Sérgio! Escolha a opção 2!\n')

       except ValueError:
           print('Essa chave digitada está inválida Sérgio!')

   elif int(op) == 2:
       aux = []
       aux.append(chave)
       aux.append(input('Nome: '))
       aux.append(int(input("CPF: ")))
       print('Chave: {}'.format(aux[0]))
       print('Nome: {}'.format(aux[1]))
       print('CPF: {}'.format(aux[2]))
       print('Cadastro efetuado Sr. Sérgio!')
       print('-------------------------')
       lista1.append(aux[:])
       lista2.append(aux[:])
       chave += 1

   elif int(op) == 3:
       try:
           buscaCPF = input('Digite o CPF para busca: ')
           for i in range(len(lista1)):
               if int(buscaCPF) == lista1[i][2]:
                   del lista1[i]
                   del lista2[i]
                   print('Removido com sucesso, Sérgio!')
                   break

           if len(lista1) == 0:
               print('Lista vazia!')

           print('-----------------------------------')

       except ValueError:
           print('Chave inválida!')

   elif int(op) == 4:

       for i in range(len(lista1)):
           print('Código : {} nome: {} CPF: {}'.format(lista1[i][0], lista1[i][1], lista1[i][2]))

       for i in range(len(lista3)):
           print('Código : {} nome: {} CPF: {}'.format(lista3[i][0], lista3[i][1], lista3[i][2]))

       for i in range(len(lista5)):
           print('Código: {} nome: {} CPF: {}'.format(lista5[i][0], lista5[i][1], lista5[i][2]))

       for i in range(len(lista7)):
           print('Código : {} nome: {} CPF: {}'.format(lista7[i][0], lista7[i][1], lista7[i][2]))

       print('------------------------------------')

   elif int(op) == 5:
       try:
           buscaPeloCPF = input('Sérgio, agora digite o CPF para busca, por gentileza: ')
           for i in range(len(lista1)):
               if int(buscaPeloCPF) == lista1[i][2]:
                   print('Nome: {}'.format(lista1[i][1]))
                   print('--------------------------')

           if len(lista1) == 0:
               print('Lista vazia, Sérgio!')

       except ValueError:
           print('Essa chave digitada está inválida Sérgio!')

       print('-------------------------------------')

   elif int(op) == 6:
       listaAUX1 = []
       listaAUX2 = []
       for i in range(len(lista1)):
           if (i % 2 == 0):
               listaAUX1.append(lista1[i])
           else:
               listaAUX2.append(lista1[i])

       print('Lista1: {}'.format(listaAUX1))
       print('Lista2: {}'.format(listaAUX2))

       print('--------------------------------------')

   elif int(op) == 7:
       lista3 = []
       for i in range(len(listaAUX1)):
           lista3.append(listaAUX1[i])
           if (i < len(listaAUX2)):
               lista3.append(listaAUX2[i])
           else:
               break

       print('Lista intercalada:')
       for i in range(len(lista3)):
           print('Lista intercalada: chave: {} nome: {} CPF: {}'.format(i, lista3[i][0], lista3[i][1], lista3[i][2]))

       print('--------------------------------------')

   elif int(op) == 8:
       print('Fim do programa!')
       system('pause')
       exit()

   else:
       print('Opção inválida!')
       continue


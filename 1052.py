'''
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

Entrada
A entrada contém um único valor inteiro.

Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

Exemplo de Entrada
4

Exemplo de Saída
April












'''



valor = int(input())

if valor == 1:
    print('January')
    elif valor == 2:
        print('February')
        if valor == 3:
            print('March')
            if valor == 4:
                print('April')
                if valor == 5:
                    print('May')
                    if valor == 6:
                        print('June')
                        if valor == 7:
                            print('July')
                            if valor == 8:
                                print ('August')
                                if valor == 9:
                                    print('September')
                                    if valor == 10:
                                        print('October')
                                        if valor == 11:
                                            print('November')
                                            if valor == 12:
                                                print('December')

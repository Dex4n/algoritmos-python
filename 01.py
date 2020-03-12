from random import randint

def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False

    return lista

class No(object):

    def __init__(self, dado, anterior, proximo):
        self.dado = dado
        self.anterior = anterior
        self.proximo = proximo


class ListaDuplamenteEncadeada(object):
    cabeca = None
    rabo = None

    def acrescentar(self, dado):
        novo_no = No(dado, None, None)
        if self.cabeca is None:
            self.cabeca = novo_no
            self.rabo = novo_no
        else:
            novo_no.anterior = self.rabo
            novo_no.proximo = None
            self.rabo.proximo = novo_no
            self.rabo = novo_no

    def remover(self, dado):
        no_atual = self.cabeca

        while no_atual is not None:

            if no_atual.dado == dado:
                if no_atual.anterior is None:
                    self.cabeca = no_atual.proximo
                    no_atual.proximo.anterior = None
                else:
                    no_atual.anterior.proximo = no_atual.proximo
                    no_atual.proximo.anterior = no_atual.anterior

            no_atual = no_atual.proximo

    def mostrar(self):
        no_atual = self.cabeca
        no = ""
        while no_atual is not None:
            if no_atual.anterior is None:
                no += "None "
            no += "<---> | " + str(no_atual.dado) + " | "
            if no_atual.proximo is None:
                no += "<---> None"
            no_atual = no_atual.proximo
        print(no)
        print("=" * 160)

#CRIANDO 3 LISTAS DUPLAMENTE ENCADEADAS
lista1 = ListaDuplamenteEncadeada()
lista2 = ListaDuplamenteEncadeada()
lista3 = ListaDuplamenteEncadeada()

#GERANDO 10 NÚMEROS ALEATÓRIOS PARA AS 3 LISTA
for i in range(10):
    lista1.acrescentar(randint(0, 250))
    lista2.acrescentar(randint(0, 250))
    lista3.acrescentar(randint(0, 250))

#APRESENTANDO AS LISTAS
print("\nLISTA UM\n")
lista1.mostrar()

print("\nLISTA DOIS\n")
lista2.mostrar()

print("\nLISTA TRES\n")
lista3.mostrar()

#ORDENANDO AS LISTAS

print("\nA) As listas não estão ordenadas! 1 ponto pra mim! :)\n")
print("\nB) Ordenando as 3 listas: mais 1 ponto pra mim! :D\n")
listaAux1 = []
aux1 = lista1.cabeca
for i in range(10):
    listaAux1.append(aux1.dado)
    aux1 = aux1.proximo
print("\nLista 1 não ordenada:\n")
print(listaAux1)

print("\nLista 1 ordenada:\n")
print(bubble_sort(listaAux1))


listaAux2 = []
aux2 = lista2.cabeca
for i in range(10):
    listaAux2.append(aux2.dado)
    aux2 = aux2.proximo
print("\nLista 2 não ordenada:\n")
print(listaAux2)

print("\nLista 2 ordenada:\n")
print(bubble_sort(listaAux2))

listaAux3 = []
aux3 = lista3.cabeca
for i in range(10):
    listaAux3.append(aux3.dado)
    aux3 = aux3.proximo
print("\nLista 3 não ordenada:\n")
print(listaAux3)

print("\nLista 3 ordenada:\n")
print(bubble_sort(listaAux3))

lista4 = []
for i in range(10):
        lista4.append(listaAux1[i])
        lista4.append(listaAux2[i])
        lista4.append(listaAux3[i])

print("C) Lista mesclada desordenada: Valendo o 3º pontos! ")
print(lista4)

print("Lista 4 ordenadinha, conforme solicitado!")
print(bubble_sort(lista4))
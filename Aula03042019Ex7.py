#Programe um script em Python que calcule a média de uma turma, não importa o número de alunos que ela tenha,
# seu único script serve para todos os casos.

contadorTemporario = 0
somaTotalNotas = 0

print("00 - para encerrar o programa! / 0 - para mostrar média da turma.")

while True:
    notaAluno = int(input("Digite a nota do aluno: "))

    if (notaAluno != 0):

        somaTotalNotas += notaAluno
        contadorTemporario += 1

    else:
        mediaTotalTurma = somaTotalNotas / contadorTemporario
        print("Média da turma é: ", mediaTotalTurma)
        print("Sistema finalizado com sucesso!")
        break


nota1 = 0.0
nota2 = 0.0

mediaAluno = 0.0

nota1=float(input("Digite a 1ª nota do aluno: "))
nota2=float(input("Digite a 2ª nota do aluno: "))

mediaAluno = (nota1 + nota2) / 2

if (mediaAluno >= 7 and mediaAluno < 10):
    print("Aprovado")
elif (mediaAluno < 7):
    print("Reprovado")
elif (mediaAluno == 10):
    print("Aprovado com distinção")
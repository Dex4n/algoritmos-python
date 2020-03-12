nota1Aluno = float(input("Digite a primeira nota:\t"))
nota2Aluno = float(input("Digite a segunda nota:\t"))

mediaAluno = (nota1Aluno + nota2Aluno) / 2


if mediaAluno >= 9.0 and mediaAluno <= 10.0:
    print("Nota 1 do aluno: ",nota1Aluno)
    print("Nota 2 do aluno: ",nota2Aluno)
    print("Média do aluno:  ",mediaAluno)
    print("APROVADO! Conceito: (A)")
elif mediaAluno >= 7.5 and mediaAluno < 9.0:
    print("Nota 1 do aluno: ",nota1Aluno)
    print("Nota 2 do aluno: ",nota2Aluno)
    print("Média do aluno:  ",mediaAluno)
    print("APROVADO! Conceito: (B)")
elif mediaAluno >= 6.0 and mediaAluno < 7.5:
    print("Nota 1 do aluno: ",nota1Aluno)
    print("Nota 2 do aluno: ",nota2Aluno)
    print("Média do aluno:  ",mediaAluno)
    print("APROVADO! Conceito: (C)")
elif mediaAluno >= 4.0 and mediaAluno < 6.0:
    print("Nota 1 do aluno: ",nota1Aluno)
    print("Nota 2 do aluno: ",nota2Aluno)
    print("Média do aluno:  ",mediaAluno)
    print("REPROVADO! Conceito: (D)")
elif mediaAluno >= 0.0 and mediaAluno < 4.0:
    print("Nota 1 do aluno: ",nota1Aluno)
    print("Nota 2 do aluno: ",nota2Aluno)
    print("Média do aluno:  ",mediaAluno)
    print("REPROVADO! Conceito: (E)")




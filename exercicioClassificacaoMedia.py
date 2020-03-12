
nota1 = float(input("Digite o valor para a 1ª nota: "))
nota2 = float(input("Digite o valor para a 2ª nota: "))

media_aluno = (nota1 + nota2)/2

if media_aluno >= 9.0 and media_aluno <= 10.0:
    print("Nota 1 do aluno: %.2f"%(nota1))
    print("Nota 2 do aluno: %.2f"%(nota2))
    print("Média do aluno:  %.2f"%(media_aluno))
    print("Aluno com classificação A: APROVADO!")
if media_aluno >= 7.5 and media_aluno < 9.0:
    print("Nota 1 do aluno: %.2f"%(nota1))
    print("Nota 2 do aluno: %.2f"%(nota2))
    print("Média do aluno:  %.2f"%(media_aluno))
    print("Aluno com classificação B: APROVADO!")
if media_aluno >= 6.0 and media_aluno < 7.5:
    print("Nota 1 do aluno: %.2f"%(nota1))
    print("Nota 2 do aluno: %.2f"%(nota2))
    print("Média do aluno:  %.2f"%(media_aluno))
    print("Aluno com classificação C: APROVADO!")
if media_aluno >= 4.0 and media_aluno < 6.0:
    print("Nota 1 do aluno: %.2f"%(nota1))
    print("Nota 2 do aluno: %.2f"%(nota2))
    print("Média do aluno:  %.2f"%(media_aluno))
    print("Aluno com classificação D: REPROVADO!")
if media_aluno >= 0 and media_aluno < 4.0:
    print("Nota 1 do aluno: %.2f"%(nota1))
    print("Nota 2 do aluno: %.2f"%(nota2))
    print("Média do aluno:  %.2f"%(media_aluno))
    print("Aluno com classificação D: REPROVADO!")

turnoEstudo = input("Digite: \n "
                    "(M) Matutino \n "
                    "(V) Vespertino \n "
                    "(N) Noturno \n -> ")

if turnoEstudo != 'M' and turnoEstudo != 'V' and turnoEstudo != 'N':
    print("Valor inválido!")
if turnoEstudo == 'M':
    print("Bom dia!")
elif turnoEstudo == 'V':
    print("Boa tarde!")
elif turnoEstudo == 'N':
    print("Boa noite!")



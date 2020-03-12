senhaValidaUsuario = "cesusc2019"


while True:
    senhaDigitada = input("Digite sua senha: ")
    
    if (senhaDigitada == senhaValidaUsuario):
        print("Senha correta, sistema liberado!")
        break
    else:
        print("Senha incorreta, digite novamente. ")
        senhaDigitada=input("Digite sua senha: ")
breakpoint()
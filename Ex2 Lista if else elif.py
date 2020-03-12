numero1 = int(input("Diga o primeiro número: "))
numero2 = int(input("Diga o segundo número: "))
numero3 = int(input("Diga o terceiro número: "))


if (numero1 > numero2 and numero1 > numero3):
    print("Número 1: (%d) é o maior!"%(numero1))
elif (numero2 > numero1 and numero2 > numero3):
    print("Número 2: (%d) é o maior!"%(numero2))
elif (numero3 > numero1 and numero3 > numero2):
    print("Número 3: (%d) é o maior!"%(numero3))

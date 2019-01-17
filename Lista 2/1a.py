numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
escolha = int(input("Digite a opção desejada: \n (1): Média \n (2): Diferença \n (3): Produto \n (4): Divisão \nOpção: "))

if (escolha == 1):
    resultado = (numero1+numero2)/2
    print ("A média é: ",resultado)
elif (escolha == 2):
    resultado = numero1-numero2
    print ("A diferença é: ",resultado)
elif (escolha == 3):
    resultado = numero1*numero2
    print ("O produto é: ",resultado)
elif (escolha == 4):
    if (numero2!=0):
        resultado = numero1/numero2
        print("A divisão é: ", resultado)
    else:
        print("Não é possível dividir por 0")
else:
    print ("Opção desejada incorreta")
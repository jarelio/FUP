tipo_investimento = int(input("Digite o tipo do investimento: \n (1): Poupança \n (2): Fundo de renda fixa \nTipo: "))
if (tipo_investimento!= 1 and tipo_investimento != 2):
    print ("Opção inválida")
else:
    valor_investimento = float(input("Digite o valor do investimento: "))

    if (tipo_investimento==1):
        valor_investimento = valor_investimento + (valor_investimento*0.1)
        tipo_investimento  = "Poupança"
    else:
        valor_investimento = valor_investimento + (valor_investimento*0.15)
        tipo_investimento = "Fundo de Renda Fixa"

    print("O tipo de investimento foi: ", tipo_investimento)
    print("O valor corrigido é: ", valor_investimento)


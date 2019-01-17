cpf = input("Digite o número do CPF (9 digitos): ")
multiplicador = 10
multiplicador_digito2 = 11
soma = 0
soma_2 = 0
verifica_resto = 2
if len(cpf)==9:
    lista_cpf = list(cpf)

    #PRIMEIRO DIGITO VERIFICADOR DO CPF
    for i in lista_cpf:
        while multiplicador > 1:
            i = int(i)
            soma = soma + multiplicador*i
            multiplicador -=1
    resto = soma%11
    if resto == 0 or resto == 1:
        j = "0"
    else:
        while verifica_resto<11:
            if resto == verifica_resto:
                j = str(11-resto)
            verifica_resto+=1
    lista_cpf.append(j)

    #SEGUNDO DIGITO VERIFICADOR DO CPF
    print(lista_cpf)
else:
    print("Numero inválido de CPF")
for digitos in lista_cpf:
    print(digitos,end='')

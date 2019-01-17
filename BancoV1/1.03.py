import os
lista = []
contas = {}
#Loop Operações
seletor = 1
while seletor != 0:
    
    print("\nSelecione uma das Opções a Seguir: ")
    print("\n0 - Sair \n")
    print("1 - Creditar\n2 - Debitar")
    print("3 - Transferir\n4 - Consultar Saldo \n")
    print("5 - Criar Conta\n6 - Excluir Conta \n")
    opcao = int(input("Escolha: "))
	
    if opcao == 1:
        numero_conta = input("Digite o número da conta para creditar: ")
        continua = True
        i = 0
        while i <= len(lista) and continua:
            if (i == len(lista)):
                print("Conta Inexistente")
                continua = False
            else:
                if numero_conta in lista[i]:
                    valor = eval(input("Digite o valor a ser creditado: "))
                    if valor < 0:
                        print("Não é possível creditar valores negativos!")
                        continua = False
                    else:
                        lista[i][numero_conta] += valor
                        print("Operação realizada com sucesso! ")
                        continua = False
                else:
                    i +=1
    elif opcao == 2:
        numero_conta = input("Digite o número da conta: ")
        continua = True
        i = 0
        while i <= len(lista) and continua:
            if (i == len(lista)):
                print("Conta Inexistente")
                continua = False
            else:
                if numero_conta in lista[i]:
                    valor = eval(input("Digite o valor a ser debitado: "))
                    if valor < 0:
                        print("Não é possível debitar valores negativos")
                        continua = False
                    elif valor > lista[i][numero_conta]:
                        print("Saldo Insuficiente")
                        continua = False
                    else:
                        lista[i][numero_conta] -= valor
                        print("Operação realizada com sucesso! ")
                        continua = False
                else:
                    i +=1
	    
    elif opcao == 3:
        conta_origem = input("Digite o número da conta de origem: ")
        conta_destino = input("Digite o número da conta de destino: ")
        continua = True
        i = 0
        verifica_origem = False
        verifica_destino = True
        while i <= len(lista) and continua:
            if (i == len(lista)):
                print("Conta Inexistente")
                continua = False
            else:
                if conta_origem in lista[i]:
                    verifica_origem = True
                    posicao1 = i
                    continua = False
                else:
                    i +=1
        continua = True
        i = 0
        while i <= len(lista) and continua:
            if (i == len(lista)):
                print("Conta Inexistente")
                continua = False
            else:
                if conta_destino in lista[i]:
                    verifica_destino = True
                    posicao2 = i
                    continua = False
                else:
                    i +=1
        if verifica_origem and verifica_destino:
            valor = eval(input("Digite o valor para transferir: "))
            if valor < 0:
                print("Não é possível transferir valores negativos")
            elif valor > lista[posicao1][conta_origem]:
                print("Saldo Insuficiente")
            else:
                lista[posicao1][conta_origem] -= valor
                lista[posicao2][conta_destino] += valor
                print("Operação realizada com sucesso! ")
    elif opcao == 4:
        numero_conta = input("Digite o número da conta: ")
        continua = True
        i = 0
        while i <= len(lista) and continua:
            if (i == len(lista)):
                print("Conta Inexistente")
                continua = False
            else:
                if numero_conta in lista[i]:
                    print("Saldo: %.2f" %(lista[i][numero_conta]))
                    continua = False    
    elif opcao == 5:
        numero_conta = input("Digite o número da conta a ser criada: ")
        if len(lista) == 0:
            contas = {numero_conta:0}
            lista.append(contas)
            print("Operação realizada com sucesso! ")
        else:
            continua = True
            i = 0
            while i <= len(lista) and continua:
                if numero_conta not in lista[i]:
                    i+=1
                else:
                    print("Conta existente")
                    continua = False
                if(i == len(lista)):
                    contas = {numero_conta:0}
                    lista.append(contas)
                    continua = False
                    print("Operação realizada com sucesso! ")
    elif opcao == 6:
        numero_conta = input("Digite o número da conta a ser excluida: ")
        continua = True
        i = 0
        while i <= len(lista) and continua:
            if (i == len(lista)):
                print("Conta Inexistente")
                continua = False
            elif numero_conta in lista[i]:
                lista.remove(lista[i])
                print("Operação realizada com sucesso! ")
                continua = False
            else:
                i +=1
    elif opcao == 0:
        print("Programa Fechado")
        seletor = 0
    else:
        print("Opção Inválida, escolha novamente")
    
#Printa Saldos Finais
print("\n")
i = 0
if len(lista) == 0:
    print("O Banco não possui alguma conta")
else:
    while i <= len(lista)-1:
        for b in lista[i]:
            print("Conta: %s Saldo: %.2f" %(b,lista[i][b]))
        i+=1                 

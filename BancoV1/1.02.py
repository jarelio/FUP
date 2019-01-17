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
        numero_conta = input("Digite o número da conta: ")
        if numero_conta in contas:
            valor = eval(input("Digite o valor a ser creditado: "))
            if valor < 0:
                print("Não é possível creditar valores negativos!")
            else:
                contas[numero_conta] += valor
                print("Operação realizada com sucesso! ")
        else:
           print("Conta Inexistente")
    elif opcao == 2:
        numero_conta = input("Digite o número da conta: ")
        if numero_conta in contas:
            valor = eval(input("Digite o valor a ser creditado: "))
            if valor < 0:
                print("Não é possível debitar valores negativos")
            elif valor > contas[numero_conta]:
                print("Saldo Insuficiente")
            else:
                contas[numero_conta] -= valor
                print("Operação realizada com sucesso! ")
        else:
            print("Conta Inexistente")
	    
    elif opcao == 3:
        conta_origem = input("Digite o número da conta de origem: ")
        conta_destino = input("Digite o número da conta de destino: ")
        if conta_origem and conta_destino in contas:
            valor = eval(input("Digite o valor para transferir: "))
            if valor < 0:
                print("Não é possível transferir valores negativos")
            elif valor > contas[conta_origem]:
                print("Saldo Insuficiente")
            else:
                contas[conta_origem] -= valor
                contas[conta_destino] += valor
                print("Operação realizada com sucesso! ")
        else:
            print("Conta Inexistente")
		
    elif opcao == 4:
        numero_conta = input("Digite o número da conta: ")
        if numero_conta in contas:
            print("Saldo: %.2f" %(contas[numero_conta]))
        else:
            print("Conta Inexistente")
    
    elif opcao == 5:
        numero_conta = input("Digite o número da conta a ser criada: ")
        if numero_conta not in contas:
            contas[numero_conta] = 0
            print("Operação realizada com sucesso! ")
        else:
           print("Conta Existente")
           
    elif opcao == 6:
        numero_conta = input("Digite o número da conta a ser excluida: ")
        if numero_conta in contas:
            del contas[numero_conta]
            print("Operação realizada com sucesso! ")
        else:
           print("Conta Inexistente")
    elif opcao == 0:
        print("Programa Fechado")
        seletor = 0
    
    else:
        print("Opção Inválida, escolha novamente")
    
#Printa Saldos Finais
print("\n")
for i in contas:
    print("Conta: %s Saldo: %.2f" %(i,contas[i]))
                                        

continua = True
soma_produtos = 1
while (continua):
    numero = float(input("Digite um número: "))
    soma_produtos = soma_produtos * numero
    fechar = input("Digite Y para parar a execução: ")
    if (fechar == "Y"):
        continua = False
print (soma_produtos)
            

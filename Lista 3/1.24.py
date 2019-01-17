N = int(input("Digite a quantidade de termos: "))
if (N<3):
    print("É necessário pelo menos 3 termos para fazer a série")
else:
    primeiro = int(input("Digite o primeiro termo: "))
    segundo = int(input("Digite o segundo termo: "))
    print("A série de Fetuccine é:",end=' ')
    print(primeiro,end=' ')
    print(segundo,end=' ')
    proximo = segundo + primeiro
    print(proximo,end=' ')
    for i in range(4,N+1):
        if (i%2 == 0 ):
            primeiro = segundo
            segundo = proximo
            proximo = segundo - primeiro
            print(proximo,end=' ')
        else:
            primeiro = segundo
            segundo = proximo
            proximo = segundo + primeiro
            print(proximo,end=' ')

N = int(input("Digite um número para ser o fim da série: "))
proximo_numero = 0
soma_termos = 0
if (N < 3):
    print("Para existir a série são necessarios pelo menos 3 termos")
else:
    primeiro_numero = int(input("Digite o primeiro número da série: "))
    segundo_numero = int(input("Digite o segundo número da série: "))
    proximo_numero = primeiro_numero + segundo_numero
    print(primeiro_numero)
    print(segundo_numero)
    print(proximo_numero)
    soma_numeros = primeiro_numero + segundo_numero + proximo_numero
    for i in range(3,N):
        primeiro_numero = segundo_numero
        segundo_numero = proximo_numero
        proximo_numero = primeiro_numero+segundo_numero
        print(proximo_numero)
        soma_numeros = soma_numeros + proximo_numero
    print("A soma dos termos é: ",soma_numeros)


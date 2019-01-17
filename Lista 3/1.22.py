N = int(input("Digite um número: "))
primeiro_numero = 1
segundo_numero = 0
proximo_numero = 0
for i in range(0,N):
    segundo_numero = primeiro_numero
    primeiro_numero = proximo_numero
    proximo_numero = primeiro_numero+segundo_numero
    print(proximo_numero)

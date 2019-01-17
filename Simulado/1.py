soma = 0
denominador = 1
troca = 1
for numero in range(1,21):
    contador = 1
    numero_fatorial = 1
    while contador<=numero:
        numero_fatorial = numero_fatorial * contador
        contador+=1
    if troca == 1:
        soma = soma+(numero_fatorial/denominador)
        troca = 0
    else:
        soma = soma-(numero_fatorial/denominador)
        troca = 1
    denominador = 2*denominador+1
print("A soma dos 20 primeiros termos é:",soma)

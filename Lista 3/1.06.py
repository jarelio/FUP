numero = int(input("Digite um número não-nulo inteiro: "))
contador = 1
numero_fatorial = 1
while contador<=numero:
    numero_fatorial = numero_fatorial * contador
    contador+=1
print("%d! = %d" %(numero,numero_fatorial))

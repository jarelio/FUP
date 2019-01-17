'''Implementar um programa para calcular o sen(X). O valor de X deverá ser digitado
em graus. O valor do seno de X será calculado pela soma dos 15 primeiros termos da
série a seguir:
Os termos da série devem ser armazenados em um vetor.'''

X = float(input("Digite o valor dos graus: "))
lista = []
expoente = 1
contador = 1
soma_dos_termos = 0
while contador !=16:
    
    #CALCULO_FATORIAL
    numero_fatorial = 1
    numero = 1
    while(numero<=expoente):
        numero_fatorial = numero_fatorial * numero
        numero +=1
    #FIM_CALCULO_FATORIAL
    termo = ((X**expoente)/numero_fatorial)
    #CALCULO DOS TERMOS E ACRESCENTAR NA LISTA
    if (contador%2==0):
        lista.append(-termo)
    else:
        lista.append(termo)
    #FIM_ACRESCENTAR
        
    #CONTADORES   
    contador +=1
    expoente +=2
    #FIM_CONTADORES
    
#FAZER A SOMA DOS TERMOS DA LISTA E PRINTAR
for termos in lista:
    soma_dos_termos = soma_dos_termos + termos
print(soma_dos_termos)

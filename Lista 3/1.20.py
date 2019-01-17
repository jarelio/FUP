N = int(input("Digite a quantidade de números primos: "))
print ("Os %d menores números primos são:" %N)
contador_primo = 0
numero = 2
while (contador_primo < N):
    primo = 1
    contador = 2
    while (primo == 1 and contador < numero):
        if (numero % contador == 0):
            primo = 0
        contador +=1
    if (primo == 1):
        print(numero,end=' ')
        contador_primo+=1
    numero+=1

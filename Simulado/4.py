numero = int(input("Digite um número: "))
teste = 0
contador = 1
sequencia = 0
while sequencia<=numero:
    sequencia = contador*(contador+1)*(contador+2)
    if numero == sequencia:
        print(numero,"é triangular pois: %d * %d * %d = %d" %(contador,contador+1,contador+2,numero))
        teste = 1
    contador = contador+1
if teste == 0:
    print(numero,"não é triangular")

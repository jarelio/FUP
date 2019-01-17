numero = int(input("Digite os N primeiros termos: "))
def somatorio(numero):
    if numero == 0:
        return numero
    else:
        return(somatorio(numero-1) + numero)

numeros = ""
for i in range(1,numero+1):
    if i == numero:
        numeros = numeros + str(i) + "="
    else:
        numeros = numeros + str(i) + "+"
print(numeros,end=" ")
print(somatorio(numero))

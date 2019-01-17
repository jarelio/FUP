numero = 0
continua = 0
numeromaior= 0
while continua!="Y":
    numero = float(input("Digite um número: "))
    if (numero>numeromaior):
        numeromaior = numero
    continua = input("Deseja parar de digitar os números digite Y: ")
print (numeromaior)

for numero in range(1000,10000):
    inteiro = int(numero/100)
    segundo_inteiro = (numero - inteiro*100)
    if(inteiro+segundo_inteiro)**2==numero:
        print(numero,"atende esta caracteristica!") 

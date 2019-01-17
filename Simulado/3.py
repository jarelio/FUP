continua = True
while continua:
    sexo = int(input("Digite o sexo (1):Feminino (2):Masculino: "))
    if sexo!=1 and sexo!=2:
        continua = False
        print("Sexo inválido")  
    else:
        idade = float(input("Digite a idade: "))
        valor = float(input("Digite o valor do automóvel: "))
        apolice_itau = valor*0.04
        apolice_bradesco = valor*0.06
#Itau Seguros
        if idade<30 and idade>=18:
            apolice_itau = apolice_itau + (apolice_itau*((30-idade)/100))
        elif(idade>50):
            apolice_itau = apolice_itau - (apolice_itau*((65-idade)/100))
#Bradesco Seguros
        if sexo == 1:
            apolice_bradesco = apolice_bradesco - (apolice_bradesco*0.05)
        if idade>30:
            apolice_bradesco = apolice_bradesco - (apolice_bradesco*0.1)
        print(apolice_itau)
        print(apolice_bradesco)

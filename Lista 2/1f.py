altura = float(input("Digite o valor da sua altura em metros: "))
sexo = input("Digite o seu sexo: ")
if (sexo!="Masculino" and sexo!="Feminino"):
    print("Opção inválida")
else:
    if (sexo == "Masculino"):
        peso_ideal = ((72.7*altura)-58)
    else:
        peso_ideal = ((62.1*altura)-44.7)

    print ("O seu peso ideal é: ",peso_ideal)
salario = float(input("Digite o valor do salário (R$): "))
if (salario<900):
    salario_maior = (salario + (salario*0.3))
    print ("O valor do salário reajustado é: ",salario_maior,"R$")
else:
    print ("Este salário não tem direito a aumento")

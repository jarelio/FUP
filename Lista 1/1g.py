salario = float(input("Digite o valor do salário (Em R$): "))
salariomin = float(input("Digite o valor do salário mínimo (Em R$): "))

quantidade = int(salario/salariomin)
quantidade2 = ((salario/salariomin)-(quantidade))*salariomin

print ("Esse funcionário recebe",quantidade,"salários mínimos de",salariomin,"e salário de",quantidade2)

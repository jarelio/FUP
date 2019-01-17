#coding: utf-8

salario = float(input("Digite o valor do salário do funcionário: "))
vendas = float(input("Digite o valor das vendas do funcionário: "))

comissao = vendas * 0.04
salariofinal = salario + comissao

print "O valor da comissão é: %.2f" %comissao, "R$"
print "O valor do salário final é: %.2f" %salariofinal , "R$"

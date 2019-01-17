num_horatrab = int(input("Digite o número de horas trabalhadas: "))
salariomin = float(input("Digite o valor do salário mínimo: "))
num_horaext = int(input("Digite o número de horas extras: "))

hora_trab = salariomin/8
hora_extra = salariomin/4
salario_bruto = (num_horatrab * hora_trab)
receber_hora_extra = (num_horaext * hora_extra)
salario_receber = (salario_bruto + receber_hora_extra)

print ("O valor do salário a receber é: ",salario_receber)

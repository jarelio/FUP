#Criação do DIcionário
cidade = []
while len(cidade) < 20:
	habitantes = {}
	habitantes["nome"] = input("Digite seu nome: ")
	habitantes["salario"] = eval(input("Digite seu salário: "))
	habitantes["idade"] = int(input("Digite sua idade: "))
	habitantes["sexo"] = input("Digite seu sexo (F ou M): ")
	habitantes["nfilho"] = int(input("Digite o número de filhos: "))
	cidade.append(habitantes)

#Média Salarial Population
soma = 0
cont = 0
for k in cidade:
        soma += k["salario"]
        cont +=1
print("Média salarial: %.2f" %(soma/cont))

#Média Número de Filhos
soma = 0
cont = 0
for k in cidade:
        soma += k["nfilho"]
        cont +=1
print("Média de Filhos: %d" %(soma/cont))

#Maior Salário
maior = cidade[0]["salario"]
for k in cidade:
        if k["salario"] > maior:
                maior = k["salario"]
print("Maior salario: %.2f" %maior)

#Percentual Mulheres Salário > 10.000
cont = 0
cont2 = 0
for k in cidade:
        if k["sexo"] == "F":
                cont2 +=1
                if k["salario"] > 10000:
                        cont +=1
percentual = (cont/cont2)*100
print("Percentual de Mulheres Salário > 10000: %.2f" %percentual)

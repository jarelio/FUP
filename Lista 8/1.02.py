'''1.2. Faça um programa contendo os serviços que uma oficina mecânica realiza. Uma

ordem se serviço é composta pelas seguintes informações: número da OS, data, valor,

descrição do serviço realizado e nome do cliente. Leia as informações sobre várias

ordens de serviço e determine, ao final:

a) a média dos valores dos serviços realizados e

b) o nome do cliente que realizou o serviço mais caro, juntamente com a descrição

desse serviço e a data de sua realização.'''

oficina = []
escolha = 1
while escolha != 0:
    ordemservico = {}
    ordemservico["numero"] = input("Digite o número da OS: ")
    ordemservico["data"] = int(input("Digite a data da OS (DDMMAAAA): "))
    ordemservico["valor"] = float(input("Digite o valor da OS: "))
    ordemservico["descricao"] = input("Digite a descrição da OS: ")
    ordemservico["cliente"] = input("Digite o nome do cliente: ")
    oficina.append(ordemservico)
    escolha = int(input("Digite 0 para sair: "))

soma = 0
cont = 0
for i in oficina:
    soma += i["valor"]
    cont +=1
print("\nA Média dos valores dos serviços realizados é: %.2f " %(soma/cont))

maior = oficina[0]["valor"]
for i in oficina:
    if i["valor"] > maior:
        maior = i["valor"]

i = 0
continua = True
while i < len(oficina) and continua:
    if maior == oficina[i]["valor"]:
        continua = False
    else:
        i += 1
print("\n >>> Serviço mais caro: <<< \n")
print("Nome do Cliente: %s \nDescrição do Serviço: %s \nData do Serviço: %s " %(oficina[i]["cliente"],oficina[i]["descricao"],oficina[i]["data"]) )

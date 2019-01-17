'''1.7. Uma empresa deseja fazer um programa para armazenar as informações referentes à

propina paga aos políticos. Para cada propina paga pela empresa ela deseja armazenar: a

data do pagamento, o valor da propina, a descrição da obra relacionada a propina, o

nome do político que recebeu a propina e a sigla do seu partido. Faça um programa que

leia um conjunto de pagamentos, até que o usuário informe que não deseja mais

cadastrar pagamentos de propina. Em seguida, o programa deverá imprimir a sigla do

partido que mais recebeu propina.'''

lista_propinas = []
escolha = 1
cont = 0
while escolha !=0:
    propinas = {}
    cont +=1
    print("\nDigite os dados da propina %d\n" %cont)
    propinas["datapagamento"] = int(input("Digite a data do Pagamento: "))
    propinas["valorpropina"] = float(input("Digite o valor da propina: "))
    propinas["descricao"] = input("Digite a descrição da obra relacionada a propina: ")
    propinas["nomepolitico"] = input("Digite o nome do político que recebeu a propina: ")
    propinas["sigla"] = input("Digite a sigla do partido do político: ")
    escolha = int(input("Deseja continuar ? Digite 0 para parar: "))
    lista_propinas.append(propinas)

i = 0
maior_propina = 0
while i < len(lista_propinas):
    partido = lista_propinas[i]["sigla"]
    soma = 0
    for propinas in lista_propinas:
        if propinas["sigla"] == partido:
            soma += propinas["valorpropina"]
    if soma > maior_propina:
        partido_maior = partido
        maior_propina = soma
    i+=1
print("\nPartido que mais recebeu propina: %s Valor da propina: %.2fR$" %(partido_maior,maior_propina))


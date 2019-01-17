'''1.4. Uma empresa armazena informações sobre as contas a receber de seus clientes.

Cada uma dessas contas possui as seguintes informações: número do documento,

código do cliente, data de vencimento, data de pagamento, valor da conta de valor de

juros. Faça um programa para ler as informações sobre 15 documentos (contas a

receber) e exibir o total geral arrecadado com juros. Se a data de pagamento for maior

que a data de vencimento, em um determinado documento, o programa deverá calcular

o valor do campo “juros”, o qual corresponde a 0,02% do valor do documento para cada

dia em atraso.'''

lista_contas = []

while len(lista_contas) < 15:
    contas = {}
    print("\nDigite os dados da conta a pagar %d \n" %(len(lista_contas)+1))
    contas["numero"] = int(input("Digite o número do documento: "))
    contas["codigo"] = input("Digite o código do cliente: ")
    contas["datavenci"] = int(input("Digite a data do vencimento: "))
    contas["datapaga"] = int(input("Digite a data do pagamento: "))
    contas["valorconta"] = float(input("Digite o valor da conta a pagar: "))
    contas["valorjuros"] = 0
    lista_contas.append(contas)
    
for contas in lista_contas:
    if contas["datapaga"] > contas["datavenci"]:
        dias_atraso = contas["datapaga"] - contas["datavenci"]
        juros = 0.02 * dias_atraso
        contas["valorjuros"] = contas["valorconta"] * juros
print("\n")
for contas in lista_contas:
    dias_atraso = contas["datapaga"] - contas["datavenci"]
    print("Valor da Conta %d: %.2f -- %d Dias de Atraso -- " %(contas["numero"],contas["valorconta"],dias_atraso),end="")
    print("Valor do Juros: %.2f " %(contas["valorjuros"]))

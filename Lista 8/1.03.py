'''1.3. Faça um programa que leia o código, a descrição, o valor e a quantidade em estoque

de 10 produtos comercializados por uma papelaria. Essas informações devem ser

armazenadas em um registro do tipo vetor em ordem crescente de código.'''

lista_produtos = []

while len(lista_produtos) < 10:
    produtos = {}
    print("\nDigite os dados do produto %d \n" %(len(lista_produtos)+1))
    produtos["codigo"] = int(input("Digite o codigo do produto: "))
    produtos["descricao"] = input("Digite a descricao do produto: ")
    produtos["valor"] = float(input("Digite o valor do produto: "))
    produtos["quantidade"] = int(input("Digite a quantidade do produto: "))
    lista_produtos.append(produtos)
i = 0
j = 0
o = 0
while o < len(lista_produtos):
    i = 0
    j = o
    while j < len(lista_produtos):
        if lista_produtos[i]["codigo"] > lista_produtos[j]["codigo"]:
            a = lista_produtos[i]
            b = lista_produtos[j]
            lista_produtos[i] = b
            lista_produtos[j] = a
            i+=1
        else:
            i+=1
            j = i + 1
    o +=1
print(lista_produtos)

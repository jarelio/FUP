nome = input("Digite a primeira cadeia: ")
nome2 = input("Digite a segunda cadeia: ")
nome = list(nome)
nome2 = list(nome2)
cont2 = len(nome)
cont = 0
if len(nome) == len(nome2):
        for letter in nome2:
                if letter in nome:
                        nome.remove(letter)
                        cont +=1

if cont == cont2:
        print("É anagrama")
else:
        print("Não é anagrama")

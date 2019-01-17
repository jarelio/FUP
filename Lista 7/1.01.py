maiu = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
minu = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nome = input("Digite um nome: ")
nome = list(nome)
for i in range(0,len(nome)):
	for j in range(0,len(maiu)	):
		if nome[i] == minu[j]:
			nome[i] = maiu[j]
		elif nome[i] == maiu[j]:
			nome[i] = minu[j]
print(''.join(nome))
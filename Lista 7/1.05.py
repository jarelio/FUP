parar = True
cadeia = input("Digite a cadeia: ")
while parar:
	carac = input("Digite o caractere a ser removido: ")
	if len(carac)==1:
		parar = False
	else:
		print("Digite novamente")
cadeia = list(cadeia)
for i in cadeia:
	if i == carac:
		cadeia.remove(i)
print("\nNova cadeia sem o %s: %s" %(carac,''.join(cadeia)))
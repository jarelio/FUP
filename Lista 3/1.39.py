habitantes_a = 5000000
habitantes_b = 7000000
contador = 0
while (habitantes_b>=habitantes_a):
	contador = contador+1
	habitantes_a = habitantes_a+(3*50000)
	habitantes_b = habitantes_b+(2*70000)
	print("População de A: ",habitantes_a)
	print("População de B: ",habitantes_b)
	print("Tempo percorrido: ",contador)
print("A população do país A precisou de %d anos para ultrapassar a população de B" %contador)
continua = True
votos_ze = 0
votos_gal = 0
votos_gil = 0
print("Digite: \n (1): Para votar no Zé \n (2): Para votar na Gal \n (3): Para votar na Gil \n")
print("\n Digite 0 para encerrar a votação \n")
while continua:
    print ("Voto: ",end='')
    voto = int(input())
    if (voto == 0):
        continua = False
    elif(voto == 1):
        votos_ze +=1
    elif(voto == 2):
        votos_gal +=1
    elif(voto == 3):
        votos_gil +=1
    else:
        print("Digitou alguma opção errada, continue votando, os votos foram contabilizados")
if (votos_ze > votos_gal and votos_ze > votos_gil):
    print("Zé foi o ganhador da eleição")
elif(votos_gal > votos_ze and votos_gal > votos_gil):
    print("Gal foi o ganhador da eleição")
elif(votos_gil > votos_ze and votos_gil > votos_gal):
    print("Gil foi o ganhador da eleição")
else:
    print("Houve um empate na eleição")
    

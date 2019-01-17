velocidade_tartaruga = float(input("Digite a velocidade da tartaruga: "))
velocidade_aquiles = velocidade_tartaruga*10
posicao_tartaruga = 100
posicao_aquiles = 0
tempo = 0
while(posicao_tartaruga > posicao_aquiles):
    if(posicao_tartaruga == posicao_aquiles):
        print("Aquiles alcançou a tartaruga! ")
    posicao_tartaruga = posicao_tartaruga + velocidade_tartaruga
    posicao_aquiles = posicao_aquiles + velocidade_aquiles
    tempo = tempo+1
print("Aquiles ultrapassou a tartaruga em: %.2f unidades de tempo" %tempo) 

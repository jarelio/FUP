#1.13. Invertaos elementos de um vetor.
vetor = [9,8,7,6,5]
tamanho = 0
tamanho2 = len(vetor)-1
vetor_invertido = [0] * len(vetor)
def inverter(vetor,tamanho,tamanho2,vetor_invertido):
    if tamanho == len(vetor)-1:
        vetor_invertido[tamanho2] = vetor[tamanho]
        return vetor_invertido
    else:
        vetor_invertido[tamanho2] = vetor[tamanho]
        return inverter(vetor,tamanho+1,tamanho2-1,vetor_invertido)
    
print("Vetor:",vetor)
print("Vetor Invertido:",inverter(vetor,tamanho,tamanho2,vetor_invertido))

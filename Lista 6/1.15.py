'''1.15. Um palíndromo é uma palavra que é igual a si mesma lida de trás para frente.

Escreva uma solução que determine se uma palavra é um palíndromo.'''

palavra = input("Digite uma palavra: ")
tamanho = 1
def palindromo(palavra,tamanho):
    if tamanho == len(palavra):
        return palavra[tamanho-1]
    else:
        return palindromo(palavra,tamanho+1) + palavra[tamanho-1]

palav = palindromo(palavra,tamanho)
if palav == palavra:
    print(palavra,"é palíndromo pois sua inversa é",palav)
else:
    print(palavra,"não é palíndromo pois sua inversa é",palav)

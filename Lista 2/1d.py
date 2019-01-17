preco_produto = float(input("Digite o preço do produto: "))

if (preco_produto<=50):
    novo_preco = preco_produto+(preco_produto*0.05)
elif(preco_produto>50 and preco_produto<=100):
    novo_preco = preco_produto+(preco_produto*0.1)
elif(preco_produto>100):
    novo_preco = preco_produto+(preco_produto*0.15)

if (novo_preco<=80):
    classificacao = "D"
elif (novo_preco>80 and novo_preco<=120):
    classificacao = "C"
elif (novo_preco>120 and novo_preco<=200):
    classificacao = "B"
elif (novo_preco>200):
    classificacao = "A"

print ("O novo preço do produto é",novo_preco,"e a classificação dele é",classificacao)
saldo_medio = float(input("Digite o valor do saldo médio: "))

if (saldo_medio>400):
    credito_especial = saldo_medio*0.3
elif(saldo_medio>300 and saldo_medio<=400):
    credito_especial = saldo_medio*0.25
elif(saldo_medio>200 and saldo_medio<=300):
    credito_especial = saldo_medio*0.2
elif(saldo_medio<=200):
    credito_especial = saldo_medio*0.1

print ("O valor do saldo médio é: ",saldo_medio)
print ("O valor do crédito especial é: ",credito_especial)
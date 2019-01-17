numero = int(input("Digite um número: "))
l_binario = []
l_hexa = []
chars = ['A','B','C','D','E','F']
numero2 = numero
numero3 = numero
while numero2 != 0:
    numero_bin = numero2%2
    l_binario.insert(0,numero_bin)
    numero2 = int(numero2/2)
while numero3 != 0:
    numero_hex = numero3%16
    if numero_hex>9:
        numero_hex = chars[numero_hex-10]
    l_hexa.insert(0,numero_hex)
    numero3 = int(numero3/16)
print("Binário: ",end='')
for binario in l_binario:
    print(binario,end='')    
print(" \nHexadecimal: ",end='')
for hexadecimal in l_hexa:
    print(hexadecimal,end='')
    

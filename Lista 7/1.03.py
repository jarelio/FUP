'''1.3. Escreva um programa que leia uma cadeia de caracteres (string) que represente o
nome completo de uma pessoa e imprima o mesmo nome no formato indicado nos
exemplos a seguir. Se a String recebida for “Maria de Sá Santos” o programa deve
imprimir “Santos, Maria de Sá” . Se a String recebida for “Pedro de Souza” o programa
deve imprimir “Souza, Pedro de”.'''

nome = input("Digite seu nome: ")
nome = nome.split()
nome.insert(0,nome[len(nome)-1]+",")
nome.pop(len(nome)-1)
print(" ".join(nome))

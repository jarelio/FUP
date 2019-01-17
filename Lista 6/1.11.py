array = [12,3.2,3.8,2,3.2,4.8]
tamanho_array = len(array)

def somaarray(array,tamanho_array):
    if tamanho_array == 1:
        return array[0]
    else:
        return somaarray(array,tamanho_array-1) + array[tamanho_array-1]
    
for i in range(0,len(array)):
    if i == len(array)-1:
        print (str(array[i]),"=",end=" ")
    else:
        print (str(array[i]),"+",end=" ")
        
print("Soma:",somaarray(array,tamanho_array))

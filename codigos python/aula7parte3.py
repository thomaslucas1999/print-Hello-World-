matriz = [
 [3,5,6],
 [4,2,9],
 [9,7,5],
 [1,1,1]   
]    
soma = 0
for linhas in matriz:
    print(linhas)
    soma_linha = 0
    
    for coluna in linhas:
        print(coluna)
        soma_linha =  soma_linha + coluna
        soma = soma + coluna
    print('soma linha',soma_linha)    
print('soma é: ',soma)    

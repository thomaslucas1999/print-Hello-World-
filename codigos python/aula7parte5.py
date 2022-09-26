matriz = [
 ['andre',3,5,6], 
 ['joao',4,2,9], 
 ['pedro',9,7,5], 
 ['jose',1,1,1]  
]    

for l in range (len(matriz)):
    soma = 0
#para começar do indicie [1] -> for c in range(1,len(matriz[l]))
    for c in range(1,len(matriz[l])):
       #print(matriz[l][c])
        soma = soma + matriz[l][c]
print (f' o aluno {matriz[l][0]} tem a soma {soma}')



            
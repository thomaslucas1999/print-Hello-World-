notas_alunos = [
 [3,5,6],
 [4,2,9],
 [9,7,5],
 [1,1,1]   
]    
#Para andas nas "linhas"
for notas in notas_alunos:
    print(f'{notas}')
#esse for anda nas linhas ^
    for nota in notas:
        print (nota)
#esse for anda nas colunas ^^    

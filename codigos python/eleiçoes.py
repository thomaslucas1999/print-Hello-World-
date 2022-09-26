# Construa um algoritmo de votação para a Prefeitura Municipal de VoltaRedonda. 
# Os votos serão computados da seguinte maneira:
# + O número do candidato vencedor
# + O número de votos em branco
# + O número de votos nulos
# + o número de eleitores

print ('Escolha o numero do candidato:')
print ('Para Samuca digite 1')
print ('Para Neto digite 2')
print ('Para Baltazar digite 3')
print ('Se deseja votar em Branco digite 0')
print ('Em nulo digite 4, ou maior:')
votos = []
while True:
    candidatos = int(input ('Digite um candidato: '))
    if candidatos <4:
        candidato = 4
    if candidatos == -1:
        break
    votos.append(candidatos)
for a in votos:
    print (a)   
samuca = votos.count(1)
neto = votos.count(2)
baltazar = votos.count(3)
branco = votos.count(0)
nulo = votos.count(4)
eleitores = samuca+neto+baltazar+branco+nulo
print(f'Total de eleitores foi de:{eleitors}')
if votos == 1:
    samuca +=1
elif votos == 2:
    neto +=1
elif votos == 3:
    baltazar =+1
elif branco == 0:
    branco +=1
else:
    nulo +=1      

print(f'Total de eleitos foi: {eleitores}')
print(f'Total de votos em branco: {branco}')
print(f'Total de votos nulos foi de: {nulo}')

if neto < baltazar < samuca:
    print ('Neto venceu')
elif baltazar < neto < samuca:
    print ('Baltazar venceu')
else:
    print('Samuca venceu')
'''
Construa um algoritmo de votação para a
Prefeitura Municipal de Volta Redonda.
Os votos serão computados da seguinte maneira:
-1 - sair
0 - branco
1 - Samuca
2 - Neto
3 - Baltazar
>=4 - Nulo
A saída deverá ser:
+ O número do candidato vencedor
+ O número de votos em branco
+ O número de votos nulos
+ o número de eleitores
'''

print('''
-1 - sair
0 - branco
1 - Samuca
2 - Neto
3 - Baltazar
>=4 - Nulo
''')
'''
votos = [0, 0, 0, 0, 0]
while True:
    voto = int(input("entre com seu voto: "))
    if voto == -1:
        break
    elif voto == 0:
        votos[0] += 1 # branco
    elif voto == 1:
        votos[1] += 1 # samuca
    elif voto == 2:
        votos[2] += 1 # neto
    elif voto == 3:
        votos[3] += 1 # baltazar
    else:
        votos[4] += 1 # nulos

if votos[1] > votos[2] and votos[1] > votos[3]:
    vencedor = 1
elif  votos[2] > votos[1] and votos[2] > votos[3]:
    vencedor = 2
elif votos[3] > votos[2] and votos[3] > votos[1]:
    vencedor = 3

eleitores = votos[4] + votos[0] + votos[1] + votos[2] + votos[3]
print('O número do candidato vencedor', vencedor)
print('O número de votos em branco', votos[0])
print('O número de votos nulos', votos[4])
print('O número de eleitores', eleitores)

print(votos)
'''
'''
vencedor = 'sem vencedor'
branco = 0
nulos = 0
eleitores = 0
samuca = neto = baltazar = 0

while True:
    voto = int(input("entre com seu voto: "))
    if voto == -1:
        break
    elif voto == 0:
        branco += 1
    elif voto == 1:
        samuca += 1
    elif voto == 2:
        neto += 1
    elif voto == 3:
        baltazar += 1

if samuca > neto and samuca > baltazar:
    vencedor = 1
elif  neto > samuca and neto > baltazar:
    vencedor = 2
elif baltazar > neto and baltazar > samuca:
    vencedor = 3

eleitores = nulos + branco + samuca + neto + baltazar
print('O número do candidato vencedor', vencedor)
print('O número de votos em branco', branco)
print('O número de votos nulos', nulos)
print('O número de eleitores', eleitores)
'''
'''

vogal = ('a','e','i','o','u')
#lista = ['andre', 'carmem', 'joao', 'iraci']
lista = []
while True:
    nome = input('Entre com seu nome')
    if nome.upper() == 'SAIR':
        break
    lista.append(nome)

for i in lista:
    if i[0].lower() in vogal:
        print('O {} começa com a vogal {}'.format(i,i[0]))
    else:
        print('O {} começa com a consoante {}'.format(i,i[0]))
'''
'''
numero_funcionario =  int(input('Entre com o número do funcionário: '))
hora_trabalhada = int(input('Entre com a hora trabalhada: '))
valor_hora = float(input('Entre com o valor hora: '))

lst.append((numero_funcionario, hora_trabalhada, valor_hora))
salario = hora_trabalhada * valor_hora

print(f'NUMBER = {numero_funcionario}')
print(f'SALARY = {salario:.2f}')
'''

lst = [
    (25, 100, 5.5),
    (1, 200, 20.50),
    (6, 145, 15.50)
]

for i in lst:
    print(i)
    salario = i[1] * i[2]
    print(f'NUMBER = {i[0]}')
    print(f'SALARY = {salario:.2f}')


lst_c = [i[1] * i[2] for i in lst]
print(lst_c)
print(lst)
for i in range(len(lst)):
    print(f'NUMBER_c = {lst[i][0]}')
    print(f'SALARY_c = {lst_c[i]:.2f}')
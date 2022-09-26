faturamento = 0
vezes = 0
lista = []
while True:
    produto = input('Digite o produto: ')
    if produto.upper() == 'SAIR':
        break
    quantidade = int(input('Informe a quantidade: '))
    valor = float (input('Infome o valor: '))
    lista.append((produto,quantidade,valor))
for i in lista:
    faturamento += (i[1]*i[2])
    vezes += i[1]    
print (f'O faturamento foi de {faturamento}.')


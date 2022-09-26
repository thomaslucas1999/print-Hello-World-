lista = []
while True:
    produto = input('Selecione o produto o produto:')
    if produto.upper() == 'SAIR':
        break
    valores = []
    valor = float(input('Digite o valor:'))
    valores.append(valor)
    total = (produto, valores)
    lista.append(total)
    

print('_'*10)

print(f'a lista é {lista}')

print('_'*10)

print(f'{valores}')

print('_'*10)

print(f'{total}')

print('_'*10)

print(f'{valor}')


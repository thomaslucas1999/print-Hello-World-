lista = []
while True:
    produto = input('Entre com o produto:')
    if produto.upper() == 'SAIR':
        break
    valores = []
    while True:
        valor = float(input('Entre com sua nota:'))
        if valor == -1:
            break
    valores.append(valor)
    total = (produto, valores)
    lista.append(total)
    
print(f'a lista é {lista}')
print(f'{valores}')
print(f'{total}')
print(f'{valor}')


'''
nome == produto
valores == notas
valor == nota
'''
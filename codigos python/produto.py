lista = []
while True:
    produto = input('Digite o produto: ')
    if produto.upper() == 'SAIR':
        break
    
    quantidade = []
    numero = float(input('Digite a quantidade: '))
    
    valores = []
    valor = float(input('Digite o valor: '))
    print('-'*20)
    
    quantidade.append (numero)
    valores.append (valor)
    total = (produto, valores, quantidade)
    lista.append (total)

print('-'*20)
print(lista)
print('-'*20)

for i in lista:
    nome = i[0]
    print(f'Produto do consumidor: {nome}')
    print()
    custo = i[1]
    print(f'Valor do produto: {custo}')
    print()
    unidades = i[2]
    print(f'Quantidade do produto: {unidades}')
    print('-'*20)
    
 
    
  
      
  
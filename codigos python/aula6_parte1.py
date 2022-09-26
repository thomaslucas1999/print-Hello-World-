lista = []
while True:
    nome = input('Entre com seu nome:')
    if nome.upper() == 'SAIR':
        break
    notas = []
    while True:
        nota = float(input('Entre com sua nota:'))
        if nota == -1:
            break
    notas.append(nota)
    registro = (nome, notas)
    lista.append(registro)
    
'''
lista = [
    ('andre',[2.0 , 6.0 , 8.0 , 4.0 , 9.0])    
    ('pedro',[3.0 , 6.0])    
    ('joao',[2.0 , 6.0 , 8.0 , 3.0 , 2.0])
]
'''    
    
maior = 0
menor = 0
numero = 0
while numero >= 0:
    numero = int(input(informe um numero inteiro, numero negativo encerrara o programa))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
        print (f'maior {maior}')
        print (f'menor{menor}')


        
# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep

def contador(inicio, fim, passo):
    if inicio > fim:
        passo *= -1
    for c in range (inicio, fim+1, passo):
        print (f'{c}',end=' ',flush=True)
        sleep (0.5)
    print (' FIM. ')

print (f'Calculando de 1 a 10, de 1 em 1...')
sleep (1.5)
contador(1, 10, 1)
print ()
print (f'Calculando de 1 a 10, de 2 em 2...')
contador(10,0, 2)
print ()
print (f'Agora é sua vez...')
inicio = int(input('Digite o início da progressão: '))
fim = int(input('Digite o fim da progressão:  '))
passo = int(input('Digite o passo da progressão:  '))
print ('Calculando...')
sleep (2)

contador(inicio, fim+1, passo)
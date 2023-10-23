# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

import random
from time import sleep

def somapar(lista):
    soma = contador = 0
    print ('Calculando a soma dos números pares sorteados...')
    for valor in lista:
        if valor % 2 == 0 and not 0:
            contador += 1
            soma += valor
    print (f'Foram digitados {contador} valores pares e  soma deles é igual a {soma}')

def sorteia(lista):
    print(f'Números sorteados: ', end=' ')
    for numeros in range (0,5):
        n = random.randint(0,10)
        print (f'{n}',end= ' ',flush=True)
        sleep(0.5)
        lista.append(n)
    print ()


lista = []
print ('Sorteando números...')
sleep(1)
sorteia(lista)
print (lista)
somapar(lista)

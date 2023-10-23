# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(* num):
    numeros = []
    for valor in num:
        numeros.append(valor)
    if len(numeros) == 0:
        print ('Não foi informado valor algum. Tente novamente')
    else:
        print (f'Foram digitados {len(numeros)} números e o maior número dos valores digitados foi {max(numeros)}')


maior (2, 1, 31, 45, 1, 6, 34)
maior (1, 5, 3, 1, 4, 6, 2)
maior ()
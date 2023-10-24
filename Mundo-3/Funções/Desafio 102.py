# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.
from time import sleep

def fatorial(num=1, show=False):
    """
-> Calcula o fatorial de um número (num)
    :param num: Número que será fatorizado
    :param show: Mostrar os números em ordem decrescente até o número 1. Opcional.
    :return: Não há função return
    """
    fat = 1
    if show == False:
        for num in range (num, 0, -1):
            fat *= num
        print (fat)
    if show == True:
        print (f'O fatorial de {num} é: ',end='')
        for num in range (num, 0, -1):
            if num > 1:
                print (f'{num} x ',end='',flush=True)
                sleep (0.5)
            if num == 1:
                print (f'{num}',end='',flush=True)
                sleep (0.5)
            fat *= num
        print(f' = {fat}')
fat = 1
fatorial (5, True)
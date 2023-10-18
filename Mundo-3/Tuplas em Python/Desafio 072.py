# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int (input('Digite um número de 0 a 20: '))
    if n >= 0 and n <= 20:
        break
    else:
        print ('Número inválido.')

print (f'O número {n} em extenso é {numeros[n]}')

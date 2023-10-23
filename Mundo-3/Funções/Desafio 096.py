# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(a,b):
    area = a * b
    print (f'A área do terreno de largura {a}m e comprimento {b}m é de {area:.2f}m²')

a = float(input('Digite a largura do terreno em metros:   '))
b = float(input('Digite o comprimento do terreno em metros:  '))
area(a,b)
# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for n in range (0,5):
    lista.append(int(input('Digite um número: ')))
print (f'Os números digitados foram {lista}')
print (f'O maior número dessa lista é {max(lista)} e está na posição {lista.index(max(lista))}')
print (f'O menor número dessa lista é {min(lista)} e está na posição {lista.index(min(lista))}')
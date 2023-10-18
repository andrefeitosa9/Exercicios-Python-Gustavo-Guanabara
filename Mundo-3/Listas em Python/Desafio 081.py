# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
contador = 0
continuar = ' '
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    contador +=1
    continuar = input('Deseja continuar? S/N ').strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = input('Opção inválida. Deseja continuar? S/N ')
    if continuar == 'N':
        break
lista.sort()
# Solução A)
print (f'A) A quantidade de números digitados foi {contador}\n')
# Solução B)
lista.sort(reverse=True)
print (f'B) A lista organizada em ordem decrescente é {lista}\n')
# Solução C)
if 5 in lista:
    print (f'C) O número 5 está presente na lista na posição {lista.index(5)}.')
else:
    print (f'C) O número 5 não está presente na lista.')

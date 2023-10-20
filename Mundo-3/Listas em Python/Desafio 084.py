# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

informacoes = []
cadastro = []
contador = 0
continuar = ' '
maior = menor = 0

#Cadastro das pessoas

while True:
    cadastro.append(input('Nome:  '))
    cadastro.append(float(input('Peso (Em kg):  ')))
    if contador == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro [1] < menor:
            menor = cadastro[1]
    informacoes.append(cadastro[:])
    contador += 1
    cadastro.clear()
    continuar = input('Deseja continuar? S/N ').strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = input('Opção inválida. Deseja continuar? S / N ')
    if continuar == 'N':
        break
print (informacoes)

# Solução item A)
print (f'{contador} pessoas foram cadastradas. \n')

# Solução item B)
print (f'O maior peso é de {maior}kg de ',end='')
for p in informacoes:
    if p[1] == maior:
        print (f'{p[0]}',end=' ')
print ('\n')
print (f'O menor peso é de {menor}kg de ',end='')
for p in informacoes:
    if p[1] == menor:
        print (f'{p[0]}',end=' ')
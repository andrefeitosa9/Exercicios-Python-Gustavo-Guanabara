# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    n = int(input('Digite um número para adicionar à lista: '))
    if n not in lista:
        lista.append(n)
    else:
        print (f'O número {n} já está na lista.')
    continuar = input(f'Deseja continuar? S/N ').upper().strip()[0]
    while continuar not in 'SsNN':
        continuar = input('Opção inválida. Deseja continuar? S/N ')
    if continuar == 'N':
        break
print (f'Os números adicionados foram {sorted(lista)}')
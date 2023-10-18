# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tabela = ('Camisa', 59.95, 'Calça', 79.95, 'Bermuda', 68.7, 'Camisa social', 109, 'Sapato', 129.2, 'Tênis', 138.7, 'Camisa do Fortaleza', 1000)

print ('-'*30)
print (f'{"LISTA DE PRODUTOS":^30}')
print ('-'*30)

for pos in range (0, len(tabela)):
    if pos % 2 == 0:
        print (f'{tabela[pos]:.<40}',end='')
    else:
        print (f'R${tabela[pos]:.>.2f}')
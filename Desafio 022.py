# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome_completo = input('Escreva seu nome completo: ')

nome_completo_maiusculo = nome_completo.upper()
nome_completo_minusculo = nome_completo.lower()

print (f'O nome digitado foi: {nome_completo} \n')
print (f'Esse nome todo em maiúsculo fica: {nome_completo_maiusculo} \n')
print (f'Esse nome todo em minúsculo fica: {nome_completo_minusculo} \n')

numero_caracteres = int(len(nome_completo) - int(nome_completo.count(" ")))

print (f' A quantidade de caracteres nesse nome é de : {numero_caracteres}'\n)

nome_completo_separado = nome_completo.split()
print (f' O primeiro nome é: {nome_completo_separado[0]}')



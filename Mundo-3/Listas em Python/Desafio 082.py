# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.
continuar = ' '
lista = []
lista_par = []
lista_impar = []
while True:
  lista.append(int(input('Digite um número inteiro: ')))
  continuar = input('Deseja Continuar? S / N ').strip().upper()[0]
  while continuar not in "SsNn":
    continuar = input('Opção inválida. Deseja continuar? S / N ').strip().upper()[0]
  if continuar == 'N':
    break
for c in lista:
  if c % 2 == 0:
    lista_par.append(c)
  else:
    lista_impar.append(c)

print (f'A Lista inicial digitada foi: {lista}')
print (f'A lista somente com os números pares é {lista_par}')
print (f'A lista somente com os números ímpares é {lista_impar}')

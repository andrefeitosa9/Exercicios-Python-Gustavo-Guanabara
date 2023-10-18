# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
tupla = (n1, n2, n3, n4)
print (f'Os números digitados foram {tupla}\n')
# Solução A
print (f'O número 9 apareceu {tupla.count(9)} vez(es).\n')
# Solução B
if 3 in tupla:
    print (f'A primeira aparição do número três foi na {tupla.index(3) +1}ª casa \n')
else:
    print ('O valor 3 não foi digitado.\n')
# Solução C
print ('O(s) número(s) par(es) digitado(s) foi(são):  ',end=' ')
for par in tupla:
    if par % 2 == 0:
        print (par,end = '  ')
# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for n in range (0,5):
    num = int(input(f'Digite o {n+1}º número: '))
    if n == 0:
        lista.append(num)
        print ('Número adicionado na posição 0')
    if n == 1:
        if num < lista [0]:
            lista.insert(0,num)
            print(f'Número adicionado na posição 0')
        else:
            lista.insert(1,num)
            print(f'Número adicionado na posição 1')
    if n == 2:
        if num < lista [0]:
            lista.insert(0, num)
            print(f'Número adicionado na posição 0')
        elif num < lista [1]:
            lista.insert(1, num)
            print(f'Número adicionado na posição 1')
        else:
            lista.append(num)
            print ('Número adicionado na posição 2')
    if n == 3:
        if num < lista [0]:
            lista.insert(0,num)
            print(f'Número adicionado na posição 0')
        elif num < lista [1]:
            lista.insert(1, num)
            print(f'Número adicionado na posição 1')
        elif num < lista [2]:
            lista.insert(2,num)
            print ('Número adicionado na posição 2')
        else:
            lista.append(num)
            print ('Número adicionado na posição 3')
    if n == 4:
        if num < lista [0]:
            lista.insert(0,num)
            print(f'Número adicionado na posição 0')
        elif num < lista [1]:
            lista.insert(1, num)
            print(f'Número adicionado na posição 1')
        elif num < lista [2]:
            lista.insert(2,num)
            print ('Número adicionado na posição 2')
        elif num < lista [3]:
            lista.insert(3, num)
            print ('Número adicionado na posição 3')
        else:
            lista.append(num)
            print ('Número adicionado na posição 4')

print ("Lista finalizada!")
print (lista)

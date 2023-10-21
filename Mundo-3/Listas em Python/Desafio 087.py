# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[],[],[]]
pares = 0
terceira_coluna = 0
for a in range (0,3):
    for b in range (0,3):
        num = int(input(f'Digite o {b+1}º valor da {a+1}ª linha: '))
        matriz[a].append(num)
        if num % 2 == 0:
            pares += num
        if b == 2:
            terceira_coluna += num

# Solução A)
print (f'A soma de todos os valores pares digitados foi {pares}')
print (f'A soma dos valores da terceira coluna foi {terceira_coluna}')
print (f'O maior número da segunda linha foi {max(matriz[1])}')





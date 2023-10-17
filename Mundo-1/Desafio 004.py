# Desafio 004 - Dissecando uma variável

algo = input('Digite algo: ')
print (f'Esse algo é um número? {algo.isnumeric()} \n')
print (f'Esse algo é um texto? {algo.isalpha()} \n')
print (f'Esse algo é alfanumérico? {algo.isalnum()} \n')
print (f'Esse algo está maiúsculo? {algo.isupper()} \n')
print (f'Esse algo está minúsculo? {algo.islower()} \n')
print (f'Esse algo está capitalizado? {algo.istitle()}')
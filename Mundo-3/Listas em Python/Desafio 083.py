# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
frase = ' '
while True:
  frase = input('Digite uma frase para análise: ')
  aberturas = frase.count('(')
  fechamentos = frase.count(')')
  if aberturas == 0 and fechamentos == 0:
      print ('Não há parênteses nessa frase')
  elif aberturas < fechamentos:
        print ('Parênteses de abertura faltando na frase.')
  elif fechamentos < aberturas:
    print ('Parênteses de fechamento faltando na frase')
  else:
    print ('As posições dos parêntes estão incorretas')

# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    tam = len(msg)
    print ('~'*(len(msg)+4))
    print (f'   {msg}')
    print ('~'*(len(msg)+4))

msg = input('Digite o texto que deseja formatar: ')
escreva(msg)
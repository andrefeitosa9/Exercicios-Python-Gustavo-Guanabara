# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

moeda.titulo('Calculadora Python')
print()
moeda.opcoes()
opcao = input('Digite a opção desejada:  ')

while True:
    if opcao.isnumeric():
        if int(opcao) == 1:
            moeda.aumentar()
            print()
            moeda.titulo('Calculadora Python')
            print()
            moeda.opcoes()
            opcao = input('Digite a opção desejada:  ')
        elif int(opcao) == 2:
            moeda.diminuir()
            print()
            moeda.titulo('Calculadora Python')
            print()
            moeda.opcoes()
            opcao = input('Digite a opção desejada:  ')
        elif int(opcao) == 3:
            moeda.dobro()
            print ()
            moeda.titulo('Calculadora Python')
            print()
            moeda.opcoes()
            opcao = input('Digite a opção desejada:  ')
        elif int(opcao) == 4:
            moeda.metade()
            print()
            moeda.titulo('Calculadora Python')
            print()
            moeda.opcoes()
            opcao = input('Digite a opção desejada:  ')
        elif int(opcao) == 5:
            moeda.moeda()
            print()
            moeda.titulo('Calculadora Python')
            print()
            moeda.opcoes()
            opcao = input('Digite a opção desejada:  ')
        if int(opcao) == 999:
            print ('CALCULADORA ENCERRADA')
            break
        else:
            print(f'Opção inválida, tente novamente.')
            moeda.titulo('Calculadora Python')
            print()
            moeda.opcoes()
            opcao = input('Digite a opção desejada:  ')

# parei na função formatar em moeda em cada opção
# dar um jeito da função aumentar e subtrair rodar em número e não em lista


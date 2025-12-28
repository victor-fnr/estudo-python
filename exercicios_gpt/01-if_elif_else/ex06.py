# Exercício 6 — Menu de operações
# Crie um menu com as opções:
# Somar
# Subtrair
# Multiplicar
# Dividir
# O usuário escolhe a opção e informa dois números. O programa deve executar a operação escolhida ou exibir uma mensagem de opção inválida.
 
# %%

print('Menu de Operações: ')
print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')

print('Escolha uma opção(Ex: 1): ')
opcao = input()

if opcao == '1':
    print('Selecionado: Soma')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    resultado = n1 + n2

    print(f'Resultado: {resultado}')

elif opcao == '2':
    print('Selecionado: Subtração')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    resultado = n1 - n2

    print(f'Resultado: {resultado}')

elif opcao == '3':
    print('Selecionado: Multiplicação')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    resultado = n1 * n2

    print(f'Resultado: {resultado}')

elif opcao == '4':
    print('Selecionado: Divisão')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    if n2 == 0:
        print('Erro: divisão por zero')
    else:
        resultado = n1 / n2
        print(f'Resultado: {resultado}')

else:
    print('Opção inválida')



    

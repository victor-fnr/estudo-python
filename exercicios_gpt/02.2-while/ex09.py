# %%
# Exercício 9 — Simulação de caixa eletrônico
# Utilize while para simular saques sucessivos de uma conta até que o saldo seja insuficiente ou o usuário decida sair.

saldo = 1000

while True:
    print('''
--- CAIXA ELETRÔNICO ---
1 - SALDO
2 - SAQUE
3 - SAIR
''')

    opcao = input('Digite o número da ação desejada: ')

    if opcao == '1':
        print(f'\nSaldo atual: {saldo:.2f}')

    elif opcao == '2':
        if saldo <= 0:
            print('Saldo insuficiente.')
            continue

        valor = input('Informe o valor que deseja sacar: ')

        try:
            saque = float(valor)

            if saque <= 0:
                print('Valor inválido.')
            elif saque > saldo:
                print('Saldo insuficiente.')
            else:
                saldo -= saque
                print(f'Saque realizado: {saque:.2f}')
                print(f'Saldo atual: {saldo:.2f}')

        except ValueError:
            print('Valor inválido.')

    elif opcao == '3':
        print('Operação encerrada.')
        break

    else:
        print('Opção inválida.')


    


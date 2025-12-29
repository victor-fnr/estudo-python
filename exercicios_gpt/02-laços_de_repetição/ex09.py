# Exercício 9 — Simulação de menu
# Implemente um menu de opções que se repita até o usuário escolher sair.
# Cada opção deve executar uma ação diferente (ex.: somar, subtrair, exibir mensagem, etc.).

# %%

while True:
    print("""Selecione uma opção: 
    1 - Somar
    2 - Subtrair 
    3 - Exibir mensagem
    4 - Sair""")
    opcao = int(input(': '))

    if opcao < 1 or opcao > 4:
        print('Opção inválida')
        continue
    
    if opcao == 1:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite mais um número: '))
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif opcao == 2:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite mais um número: '))
        subtracao = n1 - n2
        print(f'{n1} - {n2} = {subtracao}')
    elif opcao == 3:
        mensagem = (input('Digite a mensagem: '))
        print(mensagem)
    elif opcao == 4:
        print('Programa finalizado')
        break



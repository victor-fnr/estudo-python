
# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

opcao = input("""Qual água você deseja?
(1) Água mineral natural - R$1,50
(2) Água mineral com gás - R$2,50
-> """)

conta = 0

if opcao == '1':
    conta = 1.50
elif opcao == '2':
    conta = 2.50

if conta == 0:
    print('Opção inválida. Digite uma opção existente.')
else:
    qtd = int(input('Quantas garrafas? -> '))
    conta = conta * qtd
    print(f'Sua conta deu: R$ {conta} BRL')

# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

opcao = int(input("""Qual água você deseja?
                 Para comprar 'Água mineral natural' digite: 1.
                 Para comprar 'Água mineral com gás' digite: 2. 
                 -> """))

conta = 0

if opcao == 1:
    conta = 1.50
elif opcao == 2:
    conta = 2.50

if conta == 0:
    ('Opção inválida. Digite uma opção existente.')
else:
    print(f'Sua conta deu R$ {conta} BRL')
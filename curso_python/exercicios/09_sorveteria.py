# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

valor_total = 0

# Tipo de sorvete
tipo_sorvete = input(
    'Escolha o TIPO de sorvete:\n'
    '(1) Casquinha - R$1,00\n'
    '(2) Cascão - R$2,50\n'
    '(3) Cestinha - R$4,00\n'
)

if tipo_sorvete == '1':
    valor_total = 1.00
    tipo = 'Casquinha'
elif tipo_sorvete == '2':
    valor_total = 2.50
    tipo = 'Cascão'
elif tipo_sorvete == '3':
    valor_total = 4.00
    tipo = 'Cestinha'
else:
    print('Opção inválida. Programa encerrado.')
    exit()  # Para o programa

print(f'Tipo de sorvete selecionado: {tipo}')

# Sabor do sorvete
sabor_sorvete = input("""Escolha o SABOR do sorvete:
(1) Morango
(2) Creme
(3) Chocolate
""")

if sabor_sorvete == '1':
    sabor = 'Morango'
elif sabor_sorvete == '2':
    sabor = 'Creme'
elif sabor_sorvete == '3':
    sabor = 'Chocolate'
else:
    print('Opção inválida. Programa encerrado.')
    exit()

print(f'Sabor selecionado: {sabor}')

# Cobertura do sorvete
cobertura_sorvete = input(
    'Escolha a COBERTURA do sorvete:\n'
    '(1) Caramelo - R$1,50\n'
    '(2) Morango - R$1,50\n'
    '(3) Chocolate - R$1,50\n'
    '(4) Sem cobertura - R$0,00\n'
)

if cobertura_sorvete == '1':
    valor_total += 1.50
    cobertura = 'Caramelo'
elif cobertura_sorvete == '2':
    valor_total += 1.50
    cobertura = 'Morango'
elif cobertura_sorvete == '3':
    valor_total += 1.50
    cobertura = 'Chocolate'
elif cobertura_sorvete == '4':
    cobertura = 'Sem cobertura'
else:
    print('Opção inválida. Programa encerrado.')
    exit()

print(f'Cobertura selecionada: {cobertura}')

print(f'Sua conta deu: R${valor_total:.2f}')
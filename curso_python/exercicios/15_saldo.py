# Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”, mas quando o usuário apertar “enter” sem digitar valor algum, o programa para de receber valores, e exibe a soma de todos os valores digitados anteriormente.
# %%

soma = 0

while True:
    entrada = input('Digite o saldo (ENTER para finalizar): R$')

    if entrada == '':
        break

    saldo = float(entrada)
    soma += saldo

print(f'A soma dos saldos é R${soma}')

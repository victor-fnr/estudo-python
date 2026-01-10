# %%
# Exercício 5 — Contador com condição
# Utilize um while para contar quantos números pares o usuário digitar, encerrando quando ele informar -1.
contador = 0
while True:
    entrada = input('Entre com um número (-1 para encerrar): ')
    if entrada == '-1':
        break

    try:
        numero = float(entrada)
        if numero % 2 == 0:
            contador += 1
    except ValueError:
        print('Valor inválido.')

print(f'Quantidade de números pares digitados: {contador}')

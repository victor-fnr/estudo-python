# %%
# Exercício 3 — Soma até parada
# Peça números inteiros ao usuário e utilize um while para somar os valores até que o usuário digite 0.
valores = []
soma = 0

while True:

    numero = input('Digite um número inteiro (0 para finalizar): ')
    if numero == '0':
        break

    try:
        numero = int(numero)
        soma += numero
        valores.append(numero)
    except ValueError:
        print('[ERRO] Valor inválido.')
        continue

print(f'Soma dos valores digitados: {soma}')
print(f'Valores digitados: {valores}')

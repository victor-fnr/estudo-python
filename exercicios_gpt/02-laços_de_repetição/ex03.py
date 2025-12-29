# Exercício 3 — Soma acumulada
# Peça ao usuário 5 números inteiros e utilize um laço de repetição para calcular e exibir a soma total.

# %%
soma = 0

for _ in range(1, 6):
    n = int(input('Digite um número: '))
    soma += n

print(f'Soma total: {soma}')


# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.
# %%
qtd = 4
soma = 0

while qtd > 0:
    altura = float(input('Digite a altura: '))
    soma += altura
    qtd -= 1

print(f'A soma das alturas é {soma}')

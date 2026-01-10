# %%
# Exercício 6 — Contagem condicional
# Utilize um laço para contar quantos elementos da lista são pares.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
count = 0

for i in number_list:
    if i % 2 == 0:
        count += 1

print(f'{count} elementos são pares.')
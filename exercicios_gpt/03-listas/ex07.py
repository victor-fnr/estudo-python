# %%
# Exercício 7 — Remoção de elementos
# Dada uma lista de números, remova todos os valores menores que 0, mantendo apenas os valores válidos.

number_list = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, 7, 8, 9, 0]
new_list = []

for i in number_list:
    if i >= 0:
        new_list.append(i)

print(new_list)
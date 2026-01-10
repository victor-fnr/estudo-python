# %%
# Exercício 3 — Soma dos elementos
# Utilize um laço para calcular a soma de todos os valores de uma lista numérica.
number_list = [5, 4, 3, 2, 1]
soma = 0
for i in number_list:
    soma += i

print(f'A soma de {number_list} é {soma}')

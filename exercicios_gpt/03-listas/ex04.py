# %%
# Exercício 4 — Maior e menor valor
# Utilize um laço para identificar o maior e o menor valor de uma lista, sem usar funções prontas.

number_list = [5, 4, 3, 2, 1]
maior = number_list[0]
menor = number_list[0]

for i in number_list:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f'Maior: {maior}')
print(f'Menor: {menor}')

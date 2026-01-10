# %%
# Exercício 8 — Acumulador com condição
# Utilize um for para percorrer os números de 1 a 100 e calcular a soma apenas dos números ímpares.
soma = 0
for i in range(1, 101):
    if i % 2 == 1:
        soma += i

print(f'Soma dos números ímpares: {soma}')


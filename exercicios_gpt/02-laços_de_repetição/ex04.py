# Exercício 4 — Contador de pares
# Utilizando um laço, percorra os números de 1 a 50 e conte quantos deles são pares.

# %%


pares = 0

for numero in range(1, 51):
    if numero % 2 == 0:
        pares += 1

print(pares)

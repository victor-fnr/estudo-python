# %%
# Exercício 4 — Contagem de valores
# Conte quantas vezes um determinado valor aparece dentro de uma tupla.

tupla = (1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 7, 7)
contagem = {}


for valor in tupla:
    if valor in contagem:
                contagem[valor] += 1
                
    else:
        contagem[valor] = 1

for valor, qtd in contagem.items():
    print(f'{valor}: {qtd}')
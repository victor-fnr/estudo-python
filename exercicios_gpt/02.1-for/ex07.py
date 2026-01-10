# %%
# Exercício 7 — Processamento de strings
# Leia uma palavra do usuário e utilize um for para contar quantas vogais ela possui.

palavra = input('Digite uma palavra: ')
count = 0

for letra in palavra:
    if letra in 'aeiou':
        count += 1

print(f'Total de vogais: {count}')


# %%
 # Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

word = input('Escreva uma palavra: ').lower()
qtd = 0

for i in word:
    if i == 'a':
        qtd += 1

if qtd == 1:
    print(f"A letra 'a' aparece {qtd} vez na palavra {word}.")
else:
    print(f"A letra 'a' aparece {qtd} vezes na palavra {word}.")

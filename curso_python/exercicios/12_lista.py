# %%
# Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

item = input('Qual item você deseja comprar?\n'
             'R: ').strip().lower()

lista = ['laranja', 'cerveja', 'miojo', 'carvão', 'picanha']

if item in lista:
    print(f'O item {item} está na lista.')
else:
    print(f'O item {item} não está na lista.')
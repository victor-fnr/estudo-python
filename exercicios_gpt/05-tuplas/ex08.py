# %%
# Exercício 8 — Tupla imutável
# Crie um programa que demonstre a imutabilidade de uma tupla tentando alterar um de seus valores e tratando o erro corretamente.

linguagens = ("Python", "Java", "Go")

print('Tente alterar o valor da Tupla na posição [0].')
print(f'Tupla: Linguagens = {linguagens}')
try:
    linguagens[0] = input('Digite um valor: ')

except TypeError:
      print(f'Um objeto \'{tuple}\' não suporta atribuição de itens.')

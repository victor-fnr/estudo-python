# %%
# Exercício 5 — Percorrendo dicionários
# Utilize um laço para percorrer um dicionário e exibir todas as chaves e valores.

produto = {
    'nome':'Doritos',
    'preço':7,
    'qntd':10
}

for chave, valor in produto.items():
    print(f'{chave} -> {valor}')

print()

for i in produto:
    print(f'{i} -> {produto[i]}')
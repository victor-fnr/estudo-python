# %%
# Exercício 2 — Acesso por chave
# Dado um dicionário com informações de um produto (nome, preço, quantidade), exiba apenas o preço do produto.

produto = {
    'nome':'Doritos',
    'preço':7,
    'qntd':10
}

print(f'R$ {produto["preço"]:.2f}')
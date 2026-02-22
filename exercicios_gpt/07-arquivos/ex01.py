# Exercício 1 — Leitura simples
# Crie um programa que abra um arquivo de texto (texto.txt) em modo leitura e exiba todo o seu conteúdo na tela.
# %%
nome_arquivo = 'historia.txt'

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

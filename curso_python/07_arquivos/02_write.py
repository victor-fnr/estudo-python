# %%

txt = 'Adicionando caracteres!\n'

nome_arquivo = 'história_02.txt'

with open(nome_arquivo, mode='a') as open_file:
    open_file.write(txt)

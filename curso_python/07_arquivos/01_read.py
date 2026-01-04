# %%

nome_arquivo = 'historia.txt'

# Abre o arquivo em formato de leitura
open_file = open(nome_arquivo)

# Lê os dados do arquivo
conteudo = open_file.read()
print(conteudo)

# Fecha o arquivo
open_file.close()


# %%


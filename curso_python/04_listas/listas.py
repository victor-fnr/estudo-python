# %%

# Uma maneira de definir listas
# Listas não são arrays
idades = [11, 24, 26, 28]

print(idades)

# %%

victor = ['Victor', 'Ribeiro', 26, 'Solteiro', 1999, 'R$999,99 BRL']

print(victor[0])
print(victor[1])
print(victor[2])
print(victor[3])
print(victor[4])
print(victor[5])

# %%
type(victor)

# %%
idades = [10, 11, 12, 13, 14, 15, 7]
# soma
print('soma idades:', sum(idades))
# quantidade
print('qtd idades:', len(idades))
# media
print('média idades:', sum(idades) / len(idades) )
# menor idade
print('menor idade:', min(idades))
# maior idade
print('maior idade:', max(idades))

# %%

victor = ['Victor Ribeiro',
          26,
          False,
          'Solteiro',
          1999,
          'R$999,99 BRL',
          ['games', 'esportes', 'filmes']]


print(len(victor))

print(victor[6][0])

hobbies = victor[6]
primeiro_hobbie = hobbies[0]
print(primeiro_hobbie)

# %%

tamanho = len(victor)
pos = tamanho - 1

hobbies = victor[pos]

victor[pos][len(hobbies) - 1]

# %%

# primeiro
victor[-1][0]
# ultimo
victor[-1][-1]
# penultimo
victor[-1][-2]

# %%
print(victor[:4])
print(victor[6][-2:])

# %%


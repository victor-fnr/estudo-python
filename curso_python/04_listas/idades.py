# %%
idades = [17, 26, 45, 99]
print(idades)

idades.append(101)

print(idades)

# %%

idades = []

while True:
    idade = input('Digite a idade:')

    if idade == '':
        break

    idades.append(int(idade))

print(idades)

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtd = len(idades)

print('Média:', media)
print('Minimo:', minimo)
print('Maximo:', maximo)
print('Quantidade:', qtd)
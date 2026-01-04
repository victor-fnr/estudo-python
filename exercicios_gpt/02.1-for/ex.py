# %%
# Exercício 1 — Repetição básica
# Utilize um for para imprimir os números de 1 a 10, um por linha.

for i in range(1, 11):
    print(i)

# %%
# Exercício 2 — Percorrendo um intervalo
# Utilize um for para imprimir os números pares de 1 a 20.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)
    
# %%
# Exercício 3 — Soma de valores
# Peça ao usuário 5 números inteiros e utilize um for para calcular a soma total.

soma = 0
for i in range(5):
    i = int(input('Digite um número: '))
    soma += i
    
print(soma)

# %%
# Exercício 4 — Contagem condicional
# Utilize um for para percorrer os números de 1 a 50 e conte quantos são múltiplos de 3.

for i in range(1, 51):
    if i % 3 == 0:
        print(i)

# %%
# Exercício 5 — Tabuada com for
# Peça ao usuário um número inteiro e utilize um for para exibir a tabuada completa desse número (1 a 10).

tabuada = int(input('Digite a tabuada a ser exibida: '))
for i in range(1, 11):
    resultado = tabuada * i
    print(f'{tabuada} x {i} = {resultado}')


# %%
# Exercício 6 — Percorrendo listas
# Crie uma lista com valores numéricos e utilize um for para:
# exibir cada elemento,
# calcular o maior valor da lista.

lista = []

while True:
    numero = input('Digite um número (ENTER para sair): ')
    if numero == '':
        break
    numero = int(numero)
    lista.append(numero)

maior = lista[0]

for numero in lista:
    print(numero)

    if numero > maior:
        maior = numero

print(f'Maior número: {maior}')

# %%
# Exercício 7 — Processamento de strings
# Leia uma palavra do usuário e utilize um for para contar quantas vogais ela possui.

palavra = input('Digite uma palavra: ')
count = 0

for letra in palavra:
    if letra in 'aeiou':
        count += 1

print(f'Total de vogais: {count}')

# %%
# Exercício 8 — Acumulador com condição
# Utilize um for para percorrer os números de 1 a 100 e calcular a soma apenas dos números ímpares.
soma = 0
for i in range(1, 101):
    if i % 2 == 1:
        soma += i

print(f'Soma dos números ímpares: {soma}')

# %%
# Exercício 9 — for aninhado
# Utilize dois laços for para exibir:
# uma tabela de multiplicação de 1 a 5.

for i in range(1, 6):
    for j in range(1, 6):
        print(f'{i} x {j} = {i * j:2}  ', end='')
    print()



# %%
# Exercício 10 — Análise de dados
# Crie um programa que utilize um for para percorrer uma lista de pessoas (idade e renda).
# O programa deve:
# classificar cada pessoa com base em regras definidas por você,
# gerar um resumo final com totais ou médias.


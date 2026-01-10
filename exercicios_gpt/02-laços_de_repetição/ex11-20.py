# Exercícios práticos – For e While (progressivo)

#%%
# 1. Contagem simples
# Crie um programa que utilize um for para imprimir os números de 1 a 10, um por linha.

for i in range(1, 11):
    print(i)

# %%
# 2. Soma acumulada
# Utilizando um for, calcule e exiba a soma de todos os números de 1 a 100.
soma = 0
for i in range(1, 101):
    resultado = i + soma
    print(f'{i} + {soma} = {resultado}')
    soma += i

# %%
# 3. Iterando sobre uma string
# Peça ao usuário uma palavra e use um for para imprimir cada caractere em uma linha separada.

palavra = input('Digite uma palavra: ')

for letra in palavra:
    print(letra)
    
print(f'A palavra "{palavra}" tem {len(palavra)} letras.')

# %%
# 4. Números pares
# Utilizando for e range(), imprima apenas os números pares de 0 a 50.

for i in range(0, 51):
    if i % 2 == 0:
        print(i)

# %%
# 5. Repetição com condição
# Crie um programa com while que solicite números ao usuário até que ele digite zero.
# Ao final, exiba quantos números foram digitados (sem contar o zero).
count = 0
while True:
    numero = input('Digite um número (0 para finalizar): ')
    numero = int(numero)
    if numero > 0:
        count += 1
    elif numero == 0:
        break
    else:   
        print('Digite um número válido')
        

print(f'Foram digitados {count} números.')

# %%
# 6. Validação de entrada
# Utilize um while para pedir uma nota entre 0 e 10.
# O programa só deve continuar quando o usuário digitar um valor válido.
notas = []
while True:
    nota = input('Digite a nota ([ENTER] para finalizar): ')
    
    if nota == '':
        break

    nota = float(nota)

    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print('Valor ínvalido.')
        continue

print(f'Notas digitadas: {notas}')
print(f'Qntd de notas: {len(notas)}')


# %%
# 7. Contador e acumulador
# Peça vários números ao usuário usando while até ele digitar um número negativo.
# Ao final, mostre:
# A quantidade de números digitados
# A soma total desses números

numeros = []
soma = 0

while True:
    numero = input('Digite um número (número negativo para finalizar): ')
    numero = float(numero)

    if numero < 0:
        break

    numeros.append(numero)
    soma += numero

print(f'qtd de números: {len(numeros)}')
print(f'Soma: {soma}')


# %%
# 8. Uso de break e continue
# Crie um programa que percorra os números de 1 a 20.
# Ignore os múltiplos de 3
# Pare o laço ao encontrar o número 17
# Explique isso apenas usando código, sem mensagens extras.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    elif i == 17:
        break
    print(i)


# %%
# 9. Laços aninhados
# Utilize dois laços for para imprimir uma tabela de multiplicação de 1 a 5, no formato organizado (ex.: 2 x 3 = 6).

for i in range(1, 6):
    for j in range(1, 6):
        resultado = i * j
        print(f'{i} x {j} = {resultado} ' )
    print()

# %%
# 10. Lógica combinada (nível avançado)
# Crie um programa que:
# Peça números ao usuário indefinidamente
# Use while para controlar a entrada
# Ignore números negativos
# Pare quando o usuário digitar "sair"
# Ao final, exiba:
# Quantos números válidos foram inseridos
# A média desses números
# O maior número digitado

numeros = []

maior = None

while True:
    numero = input('Digite um número: ')
    
    if numero.lower() == 'sair':
        break

    numero = int(numero)

    if numero < 0:
        print('Número inválido')
        print()
        continue
    elif numero > 0:
        numeros.append(numero)

    if numero > maior:
       maior = numero


media = sum(numeros) / len(numeros)

print(f'Números válidos inseridos: {len(numeros)}')
print(f'Média: {media}')
print(f'Maior número: {maior}')

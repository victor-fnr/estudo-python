# %%
# Exercício 1 — Função simples
# Crie uma função que não receba parâmetros e apenas exiba uma mensagem de boas-vindas na tela.

def saudacao():
    print('Seja bem-vindo(a)!')

saudacao()
# %%
# Exercício 2 — Função com parâmetro
# Crie uma função que receba um nome como parâmetro e exiba uma saudação personalizada.

def saudacao_personalizada(nome:str):
    print(f'Seja bem-vindo(a), {nome}!')
    
nome = input('Qual é o seu nome? ')

saudacao_personalizada(nome)

# %%
# Exercício 3 — Retorno de valor
# Crie uma função que receba dois números e retorne a soma deles. Utilize a função e exiba o resultado.

def soma(n1:float, n2:float):
    return n1 + n2

resultado = soma(26, 19)
print(resultado)

# %%
# Exercício 4 — Validação básica
# Crie uma função que receba um número e retorne True se ele for positivo ou False caso contrário.

def validacao(numero:float):
    if numero >= 0:
        return True
    else:
        return False


while True:
    numero = input('Digite um número([ENTER] para finalizar): ')
    if numero == '':
        break

    try:
        numero = float(numero)
    except ValueError:
        print('Valor inválido.')
    else:
        print(f'{numero} -> {validacao(numero)}')


# %%
# Exercício 5 — Função com lógica condicional
# Crie uma função que receba a idade de uma pessoa e retorne uma classificação:
# menor de idade
# adulto
# idoso

def classificacao_idade(idade:int):
    if idade < 0:
        return 'Idade inválida'
    elif idade < 18:
        return 'Menor de idade'
    elif idade < 60:
        return 'Adulto'
    else:
        return 'Idoso'

while True:
    idade = input('Digite uma idade([ENTER] para finalizar): ')
    if idade == '':
        break

    try:
        idade = int(idade)
        resultado = classificacao_idade(idade)
    except ValueError:
        print('Valor inválido.')
    else:
        if resultado == 'Idade inválida':
            print(resultado)
        else:
            print(f'{idade} -> {resultado}')


# %%
# Exercício 6 — Função com laço
# Crie uma função que receba uma lista de números e retorne a soma apenas dos valores pares.

def soma_pares(lista_numeros:list):
    soma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma += numero
    return soma
    
lista = []

while True:
    
    entrada = input('Digite um número ([ENTER] para finalizar): ')
    
    if entrada == '':
        break

    try:
        entrada = int(entrada)
        lista.append(entrada)

    except ValueError:
        print('Valor inválido')
    

resultado = soma_pares(lista)
        
print(f'A soma dos valores pares é: {resultado}')



# %%
# Exercício 7 — Função com múltiplos parâmetros
# Crie uma função que receba:
# salário
# percentual de aumento
# A função deve retornar o novo salário após o reajuste.

def reajuste(salario:float, per_aumento:float):
    novo_salario = salario + (salario * per_aumento)
    return novo_salario

resultado = reajuste(2100, 0.15)
print(f'R$ {resultado:.2f}')


# %%
# Exercício 8 — Função com validação
# Crie uma função que receba uma lista de notas e:
# ignore valores inválidos,
# calcule e retorne a média das notas válidas.

def media_notas(notas:list):
    qtd_notas_validas = 0
    soma_notas_validas = 0
    
    for nota in notas:
        if 0 <= nota <= 10:
            qtd_notas_validas += 1
            soma_notas_validas += nota
    
    if qtd_notas_validas == 0:
        return None
    else:
        return soma_notas_validas / qtd_notas_validas

    

lista = [-1, -1, -1, 5, 10]

print(f'{media_notas(lista)}')

    



# %%
# Exercício 9 — Função reutilizável
# Crie uma função que receba uma lista de pessoas (idades) e retorne:
# quantidade de menores de idade,
# quantidade de adultos.

def pessoas(idades:list):
    
    qtd_menores = 0
    qtd_adultos = 0

    for idade in idades:
        
        if 0 < idade < 18:
            qtd_menores += 1
        
        elif idade >= 18:
            qtd_adultos += 1
        
    return qtd_menores, qtd_adultos

lista = [-1, 2, 19]

menores, adultos = pessoas(lista)

print(f'Menores de idade: {menores}')
print(f'Adultos: {adultos}')


# %%
# Exercício 10 — Função como módulo de decisão
# Crie um programa que utilize uma função para avaliar crédito com base em:
# idade,
# renda,
# histórico (bom ou ruim).
# A função deve retornar a decisão final (aprovado, em análise ou negado), e o programa principal deve apenas chamar essa função e exibir o resultado.

def avaliacao_credito(idade: int, renda: float, historico: bool):
    if idade < 18:
        return 'Negado'

    if renda < 1500:
        return 'Negado'

    if not historico:
        return 'Em análise'

    if renda > 3000:
        return 'Aprovado'

    return 'Em análise'


print('--- AVALIAÇÃO DE CRÉDITO ---')

# Idade
while True:
    try:
        idade = int(input('Idade: '))
        if idade < 0:
            print('Idade inválida.')
            continue
        break
    except ValueError:
        print('Digite um número inteiro válido.')

# Renda
while True:
    try:
        renda = float(input('Renda mensal: '))
        if renda < 0:
            print('Renda inválida.')
            continue
        break
    except ValueError:
        print('Digite um valor numérico válido.')

# Histórico
while True:
    entrada = input('Histórico de crédito (1 = bom | 0 = ruim): ').strip()
    if entrada in ('1', '0'):
        historico = entrada == '1'
        break
    else:
        print('Digite 1 para bom ou 0 para ruim.')

# Chamada da função
resultado = avaliacao_credito(idade, renda, historico)

# Saída final
print('\n--- RESULTADO ---')
print(f'Idade: {idade}')
print(f'Renda: R$ {renda:.2f}')
print(f'Histórico: {"Bom" if historico else "Ruim"}')
print(f'Decisão: {resultado}')

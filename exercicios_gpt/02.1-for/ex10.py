# %%
# Exercício 10 — Análise de dados
# Crie um programa que utilize um for para percorrer uma lista de pessoas (idade e renda).
# O programa deve:
# classificar cada pessoa com base em regras definidas por você,
# gerar um resumo final com totais ou médias.

# Listas de dados (cada índice representa uma pessoa)
idades = [16, 22, 35, 28, 40]
rendas = [0, 1200, 2500, 4000, 1800]

# Contadores por categoria
menor_idade = 0
baixa_renda = 0
renda_media = 0
alta_renda = 0

# Acumuladores para médias
soma_idades = 0
soma_rendas = 0

print('--- ANÁLISE DE PESSOAS ---')

for i in range(len(idades)):
    idade = idades[i]
    renda = rendas[i]

    soma_idades += idade
    soma_rendas += renda

    # Classificação
    if idade < 18:
        classificacao = 'Menor de idade'
        menor_idade += 1

    elif renda < 1500:
        classificacao = 'Adulto - baixa renda'
        baixa_renda += 1

    elif renda < 3000:
        classificacao = 'Adulto - renda média'
        renda_media += 1

    else:
        classificacao = 'Adulto - alta renda'
        alta_renda += 1

    print(f'Pessoa {i + 1} -> Idade: {idade} | Renda: {renda} | {classificacao}')

# Cálculo das médias
total_pessoas = len(idades)
media_idade = soma_idades / total_pessoas
media_renda = soma_rendas / total_pessoas

print('\n--- RESUMO FINAL ---')
print(f'Total de pessoas: {total_pessoas}')
print(f'Menores de idade: {menor_idade}')
print(f'Adultos - baixa renda: {baixa_renda}')
print(f'Adultos - renda média: {renda_media}')
print(f'Adultos - alta renda: {alta_renda}')
print(f'Média de idade: {media_idade:.1f}')
print(f'Média de renda: {media_renda:.2f}')









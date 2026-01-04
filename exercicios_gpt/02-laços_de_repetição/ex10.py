# Exercício 10 — Avaliação de dados com múltiplos critérios
# Crie um programa que leia dados de várias pessoas (idade, renda e histórico).
# Utilize laços de repetição para:
# armazenar os dados,
# avaliar cada pessoa com regras definidas por você,
# exibir um resumo final com totais, médias ou classificações.

# %%

idades = []
rendas = []
historicos = []
situacoes = []

while True:
    print('\nInforme os dados da pessoa (ENTER para parar)\n')
    
    idade_input = input('Idade: ')
    if idade_input == '':
        break
    idade = int(idade_input)
    
    renda = float(input('Renda: '))
    
    historico = input('Histórico (bom/ruim): ').lower()
    
    idades.append(idade)
    rendas.append(renda)
    historicos.append(historico)
    
    if idade >= 18 and renda >= 2000 and historico == 'bom':
        situacao = 'Aprovada'
    else:
        situacao = 'Reprovada'
    
    situacoes.append(situacao)
    print(f'Situação: {situacao}')

total_pessoas = len(idades)
total_aprovadas = situacoes.count('Aprovada')
total_reprovadas = situacoes.count('Reprovada')
media_idade = sum(idades) / total_pessoas if total_pessoas > 0 else 0
media_renda = sum(rendas) / total_pessoas if total_pessoas > 0 else 0

print('\n=== RESUMO FINAL ===')
print(f'Total de pessoas: {total_pessoas}')
print(f'Aprovadas: {total_aprovadas}')
print(f'Reprovadas: {total_reprovadas}')
print(f'Média de idade: {media_idade:.1f}')
print(f'Média de renda: {media_renda:.2f}')


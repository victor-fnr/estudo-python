# Exercício 10 — Avaliação de crédito
# Implemente um sistema que avalie a aprovação de um crédito com base em:
# idade,
# renda mensal,
# valor solicitado,
# histórico (bom ou ruim).
# Utilize múltiplos if, elif e else para tomar a decisão final e justificar o resultado.

# %%

print('Avaliação de Crédito')

score = 0

# Idade
idade = int(input('Idade: '))

if idade < 0:
    print('Idade inválida.')
    exit()
elif idade < 18:
    print('Crédito negado: idade mínima não atingida.')
    exit()
elif 18 <= idade <= 24:
    score += 1
elif 25 <= idade <= 60:
    score += 2
else:   # idade > 60
    score += 1



# Renda
renda = float(input('Renda mensal: '))

if renda < 0:
    print('Valor inválido.')
    exit()
elif renda < 1500:
    score += 0
elif renda <= 3000:
    score += 1
else:
    score += 2



# Valor Solicitado
valor_solicitado = int(input('Valor Solicitado: '))

if valor_solicitado < 0:
    print('Valor inválido.')
    exit()
elif valor_solicitado > renda * 10:
    score += 0
elif valor_solicitado > renda * 5:
    score += 1
else:
    score += 2
   


# Histórico bom ou ruim
historico = input('Histórico bom ou ruim? (s/n): ').strip().lower()

if historico == 'n':
    score += 0
elif historico == 's':
    score += 2
else:
    print('Valor inválido inserido. Programa encerrado.')
    exit()



# Decisão de Crédito
motivos = []

if score <= 2:
    print(f'Pontuação: {score}/8 - Crédito Negado')

    if renda < 1500:
        motivos.append('Renda insuficiente')
    if valor_solicitado > renda * 10:
        motivos.append('Valor solicitado alto')
    if historico == 'n':
        motivos.append('Histórico ruim')
    
    for motivo in motivos:
        print('-', motivo)

    
elif 3 <= score <= 5:
    print(f'Pontuação: {score}/8 - Crédito sob análise/restrições')

else: # 6 <= score <= 8
    print(f'Pontuação: {score}/8 - Crédito aprovado')





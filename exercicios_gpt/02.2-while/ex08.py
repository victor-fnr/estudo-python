# %%
# Exercício 8 — Controle de tentativas
# Implemente um sistema de senha onde o usuário tem no máximo 3 tentativas para acertar a senha correta.

senha = '1234'
tentativas = 3

while tentativas > 0:
    entrada = input('Digite a senha: ')


    if entrada == senha:
        print('Senha correta.')
        break
    
    else:
        tentativas -= 1
        print(f'Senha incorreta. {tentativas} Tentativa(s) restante(s).')

if tentativas == 0:
    print('Acesso bloqueado. Número máximo de tentativas atingido.')

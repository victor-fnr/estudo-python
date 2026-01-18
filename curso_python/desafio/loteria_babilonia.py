# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns. 

# %%

import random

def get_input():
    while True:
        try:
            numero_usuario = int(input('Digite um número: '))

        except ValueError:
            print('Valor inválido!')
            continue

        if 1 <= numero_usuario <= 15: # Se o número for correto
            return numero_usuario

        print('Valor inválido! O valor deve ser entre 1 e 15.')

def check_numbers(sorteio:int, usuario:int)->bool:
    if sorteio == usuario:
        print(f'Parabéns, você acertou! O número sorteado é {sorteio}.')
        return True
    
    elif usuario > sorteio:
        print(f'O número sorteado é menor que {usuario}.')       
        return False

    else:
        print(f'O número sorteado é maior que {usuario}.')
        return False

numero_sorteio = random.randint(1, 15)
total_tentativas = 3

print('-----SORTEIO DA BABILÔNIA-----\n')
print('''REGRAS:
      1. O número sorteado é um número inteiro entre 1 e 15.
      2. Número de tentativas: 3\n''')

for tentativa in range(total_tentativas):
    
    numero_usuario = get_input()
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break

    restantes = total_tentativas - (tentativa + 1)
    if restantes > 0:
        print(f'Tentativas restantes: {restantes}\n')
    
else:
    print('Suas tentativas acabaram!')






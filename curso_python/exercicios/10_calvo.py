# Faça um programa que verifique se a pessoa pertence à família “calvo”.

sobrenome = input('Qual é o seu sobrenome?\n'
                  'R: ').strip().lower()

if sobrenome == 'calvo':
    print('Você pertence à família Calvo.')
else:
    print('Você não pertence à família Calvo.')
    
# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

sobrenome = input('Qual é o seu sobrenome?\n'
                  'R: ').strip().lower()

if sobrenome == 'calvo':
    print('Você pertence à família Calvo.')
elif sobrenome == 'silva':
    print('Você pertence à família Silva.')
else:    
    print('Você não pertence à família Calvo ou Silva.')
    
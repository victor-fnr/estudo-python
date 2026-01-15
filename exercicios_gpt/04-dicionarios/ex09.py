# %%
# Exercício 9 — Agrupamento de dados
# Utilize um dicionário para agrupar valores por categoria (ex.: alunos por turma, produtos por tipo).

genins = [
    ('Shikamaru Nara', 'Time Asuma'),
    ('Ino Yamanaka', 'Time Asuma'),
    ('Chouji Akimichi', 'Time Asuma'),
    ('Rock Lee', 'Time Guy'),
    ('Neji Hyuuga', 'Time Guy'),
    ('Tenten', 'Time Guy'),
    ('Hinata Hyuuga', 'Time Kurenai'),
    ('Kiba Inuzuka', 'Time Kurenai'),
    ('Shino Aburame', 'Time Kurenai'),
    ('Naruto Uzumaki', 'Time Kakashi'),
    ('Sasuke Uchiha', 'Time Kakashi'),
    ('Sakura Haruno', 'Time Kakashi')
]

times = {}

for nome, time in genins:
    if time not in times:
        times[time] = []
    times[time].append(nome)

for time, genins in times.items():
    print(f'\n{time}:')
    for genin in genins:
        print(f'- {genin}')

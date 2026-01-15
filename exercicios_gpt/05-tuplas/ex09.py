# %%
# Exercício 9 — Combinação de dados
# Utilize tuplas para representar registros (por exemplo, nome e idade).
# Armazene vários registros em uma estrutura adequada e processe-os com laços.


registros = [
      ('Cleric', 'Lv: 8'),
      ('Mage', 'Lv: 10'),
      ('Pyromancer', 'Lv: 8'),
      ('Thief', 'Lv: 4'),
      ('Warrior', 'Lv: 9')
]

for nome, lv in registros:
      print(f'{nome} - {lv}')

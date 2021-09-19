a1 = '    '
a2 = '    '
a3 = '    '
b1 = '    '
b2 = '    '
b3 = '    '
c1 = '    '
c2 = '    '
c3 = '    '
px = 0
po = 0
reiniciar = 'T'


def digitenovamente():
      print('Esta casa já esta oucupada excolha outro lugar...')


def placar():
      print(f'''
      _______ _______
     |   X   |   O   |
     |   {px}  V.S  {po}   |
     |_______|_______|''')


def jogodavelha():
      print(f'''
    #   1     2     3  
    A {a1}||{a2}||{a3}
      ================
    B {b1}||{b2}||{b3}
      ================
    C {c1}||{c2}||{c3}
    ''')


while not reiniciar == 'F':
      placar()
      while True:
            valores = 'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'
            jogodavelha()

            while True:
                  while True:
                        xpl = str(input('Player X Digite a casa correspondente: ').strip().lower())
                        if xpl in valores:
                              break
                  if xpl == 'a1':
                        if a1 == '    ':
                              a1 = '  X '
                              break
                  if xpl == 'a2':
                        if a2 == '    ':
                              a2 = '  X '
                              break
                  if xpl == 'a3':
                        if a3 == '    ':
                              a3 = '  X '
                              break
                  if xpl == 'b1':
                        if b1 == '    ':
                              b1 = '  X '
                              break
                  if xpl == 'b2':
                        if b2 == '    ':
                              b2 = '  X '
                              break
                  if xpl == 'b3':
                        if b3 == '    ':
                              b3 = '  X '
                              break
                  if xpl == 'c1':
                        if c1 == '    ':
                              c1 = '  X '
                              break
                  if xpl == 'c2':
                        if c2 == '    ':
                              c2 = '  X '
                              break
                  if xpl == 'c3':
                        if c3 == '    ':
                              c3 = '  X '
                              break
                  digitenovamente()
            jogodavelha()

            # Condição de Vitoria X Player
            if '  X ' in a1 and '  X ' in a2 and '  X ' in a3:
                  print('X Player Wins')
                  px = px + 1
                  break
            if '  X ' in b1 and '  X ' in b2 and '  X ' in b3:
                  print('X Player Wins')
                  px = px + 1
                  break
            if '  X ' in c1 and '  X ' in c2 and '  X ' in c3:
                  print('X Player Wins')
                  px = px + 1
                  break

            if '  X ' in a1 and '  X ' in b1 and '  X ' in c1:
                  print('X Player Wins')
                  px = px + 1
                  break
            if '  X ' in a2 and '  X ' in b2 and '  X ' in c2:
                  print('X Player Wins')
                  px = px + 1
                  break
            if '  X ' in a3 and '  X ' in b3 and '  X ' in c3:
                  print('X Player Wins')
                  px = px + 1
                  break

            if '  X ' in a1 and '  X ' in b2 and '  X ' in c3:
                  print('X Player Wins')
                  px = px + 1
                  break
            if '  X ' in c1 and '  X ' in b2 and '  X ' in a3:
                  print('X Player Wins')
                  px = px + 1
                  break
            while True:
                  while True:
                        opl = str(input('Player O Digite a casa correspondente: ').strip().lower())
                        if opl in valores:
                              break
                  if opl == 'a1':
                        if a1 == '    ':
                              a1 = '  O '
                              break
                  if opl == 'a2':
                        if a2 == '    ':
                              a2 = '  O '
                              break
                  if opl == 'a3':
                        if a3 == '    ':
                              a3 = '  O '
                              break
                  if opl == 'b1':
                        if b1 == '    ':
                              b1 = '  O '
                              break
                  if opl == 'b2':
                        if b2 == '    ':
                              b2 = '  O '
                              break
                  if opl == 'b3':
                        if b3 == '    ':
                              b3 = '  O '
                              break
                  if opl == 'c1':
                        if c1 == '    ':
                              c1 = '  O '
                              break
                  if opl == 'c2':
                        if c2 == '    ':
                              c2 = '  O '
                              break
                  if opl == 'c3':
                        if c3 == '    ':
                              c3 = '  O '
                              break
                  digitenovamente()
            # Condição de Vitoria O Player
            if '  O ' in a1 and '  O ' in a2 and '  O ' in a3:
                  print('O Player Wins')
                  po = po + 1
                  break
            if '  O ' in b1 and '  O ' in b2 and '  O ' in b3:
                  print('O Player Wins')
                  po = po + 1
                  break
            if '  O ' in c1 and '  O ' in c2 and '  O ' in c3:
                  print('O Player Wins')
                  po = po + 1
                  break

            if '  O ' in a1 and '  O ' in b1 and '  O ' in c1:
                  print('O Player Wins')
                  po = po + 1
                  break
            if '  O ' in a2 and '  O ' in b2 and '  O ' in c2:
                  print('O Player Wins')
                  po = po + 1
                  break
            if '  O ' in a3 and '  O ' in b3 and '  O ' in c3:
                  print('O Player Wins')
                  po = po + 1
                  break

            if '  O ' in a1 and '  O ' in b2 and '  O ' in c3:
                  print('O Player Wins')
                  po = po + 1
                  break
            if '  O ' in c1 and '  O ' in b2 and '  O ' in a3:
                  print('O Player Wins')
                  po = po + 1
                  break
            # Condição de Empate
            if a1 != '    ' and a2 != '    ' and a3 != '    ' and b1 != '    ' and b2 != '    ' and b3 != '    ' and c1 != '    ' and c2 != '    ' and c3 != '    ':
                  print('Empate!')

      while True:
            reinicio = str(input('Deseja reiniciar [S/N]').upper())
            if reinicio == 'N':
                  reiniciar = 'F'
                  break
            if reinicio == 'S':
                  reiniciar = 'T'
                  a1 = '    '
                  a2 = '    '
                  a3 = '    '
                  b1 = '    '
                  b2 = '    '
                  b3 = '    '
                  c1 = '    '
                  c2 = '    '
                  c3 = '    '
                  break
            if reinicio != 'S' or reinicio != 'N':
                  print('Invalido digite S ou N...')

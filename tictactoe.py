import re

print('---------')
print('|       |')
print('|       |')
print('|       |')
print('---------')
x_or_o = 1
player = 'X'
tictactoe = [' ' for x in range(9)]
while True:
    entrada = input('Enter the coordinates: ')
    if re.match('\d \d', entrada):
        x, y = entrada.split()
        x, y = int(x), int(y)
    else:
        print('You should enter numbers!')
        continue
    if not ((0 < x < 4) and (0 < y < 4)):
        print('Coordinates should be from 1 to 3!')
    else:
        idx = max(max((y-1), 0) + max((x-1), 0) * 3, 0)
        if tictactoe[idx] in 'XO':
            print('This cell is occupied! Choose another one!')
        else:
            if x_or_o:
                player = 'X'
                x_or_o = 0
            else:
                player = 'O'
                x_or_o = 1
            tictactoe[idx] = player
            print('---------')
            print(f'| {tictactoe[0]} {tictactoe[1]} {tictactoe[2]} |')
            print(f'| {tictactoe[3]} {tictactoe[4]} {tictactoe[5]} |')
            print(f'| {tictactoe[6]} {tictactoe[7]} {tictactoe[8]} |')
            print('---------')
            if re.match('XXX......', ''.join(tictactoe)) or \
                re.match('...XXX...', ''.join(tictactoe)) or \
                re.match('......XXX', ''.join(tictactoe)) or \
                re.match('X..X..X..', ''.join(tictactoe)) or \
                re.match('..X..X..X', ''.join(tictactoe)) or \
                re.match('.X..X..X.', ''.join(tictactoe)) or \
                re.match('X...X...X', ''.join(tictactoe)) or \
                re.match('..X.X.X..', ''.join(tictactoe)):
                print('X wins')
                exit()
            elif re.match('OOO......', ''.join(tictactoe)) or \
                    re.match('...OOO...', ''.join(tictactoe)) or \
                    re.match('......OOO', ''.join(tictactoe)) or \
                    re.match('O..O..O..', ''.join(tictactoe)) or \
                    re.match('..O..O..O', ''.join(tictactoe)) or \
                    re.match('.O..O..O.', ''.join(tictactoe)) or \
                    re.match('O...O...O', ''.join(tictactoe)) or \
                    re.match('..O.O.O..', ''.join(tictactoe)):
                print('O wins')
                exit()
            elif tictactoe[0] in 'XO' and \
                tictactoe[1] in 'XO' and \
                tictactoe[2] in 'XO' and \
                tictactoe[3] in 'XO' and \
                tictactoe[4] in 'XO' and \
                tictactoe[5] in 'XO' and \
                tictactoe[6] in 'XO' and \
                tictactoe[7] in 'XO' and \
                tictactoe[8] in 'XO':
                print('Draw')
                exit()

Board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

boardKeys = []

for key in Board:
    boardKeys.append(key)


def printBoard(board):
    print(Board['1'] + '|' + Board['2'] + '|' + Board['3'])
    print('-+-+-')
    print(Board['4'] + '|' + Board['5'] + '|' + Board['6'])
    print('-+-+-')
    print(Board['7'] + '|' + Board['8'] + '|' + Board['9'])


printBoard(Board)

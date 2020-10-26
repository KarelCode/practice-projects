
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
x_win = ['X', 'X', 'X']
o_win = ['O', 'O', 'O']


def display_board(board):
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])


# Before game
marker = ''
while marker != 'X' and marker != 'O':
    marker = input('Choose your marker X or O: ')

player1 = marker

if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'

print(f'Player 1 is {player1}.\nPlayer 2 is {player2}')
input('Press enter to start the game.')

# Main game loop
rounds = 0
while True:
    print('\n' * 100)
    display_board(board)
    print('\n')
    if player1 == 'X':
        if board[:3] == x_win or board[3:6] == x_win or board[6:] == x_win or board[0:7:3] == x_win or board[1:8:3] == x_win or board[2:9:3] == x_win or board[0:9:4] == x_win or board[2:7:2] == x_win:
            print(f'Congratulations Player 1, you won!\nNumber of rounds: {rounds}')
            break
        elif board[:3] == o_win or board[3:6] == o_win or board[6:] == o_win or board[0:7:3] == o_win or board[1:8:3] == o_win or board[2:9:3] == o_win or board[0:9:4] == o_win or board[2:7:2] == o_win:
            print(f'Congratulations Player 2, you won!\nNumber of rounds: {rounds}')
            break
        if rounds % 2 == 0:
            place = int(input('Where do you want to place your X?'))
            board[place - 1] = 'X'
            rounds += 1
        else:
            place = int(input('Where do you want to place your O?'))
            board[place - 1] = 'O'
            rounds += 1
    else:
        if board[:3] == x_win or board[3:6] == x_win or board[6:] == x_win or board[0:7:3] == x_win or board[1:8:3] == x_win or board[2:9:3] == x_win or board[0:9:4] == x_win or board[2:7:2] == x_win:
            print(f'Congratulations Player 2, you won!\nNumber of rounds: {rounds}')
            break
        elif board[:3] == o_win or board[3:6] == o_win or board[6:] == o_win or board[0:7:3] == o_win or board[1:8:3] == o_win or board[2:9:3] == o_win or board[0:9:4] == o_win or board[2:7:2] == o_win:
            print(f'Congratulations Player 1, you won!\nNumber of rounds: {rounds}')
            break
        if rounds % 2 == 0:
            place = int(input('Where do you want to place your O?'))
            board[place - 1] = 'O'
            rounds += 1
        else:
            place = int(input('Where do you want to place your X?'))
            board[place - 1] = 'X'
            rounds += 1
print('Game over!')
input()
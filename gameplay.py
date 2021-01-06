import board
import player
import random


def restart():
    replay = input("Play again? (y/n)")
    if replay in ['y', 'Y', 'yes', 'YES']:
        for key in board.boardKeys:
            board.Board[key] = " "
        player.Player.character = player.Bot.character = " "
        whoGoesFirst()
    else:
        print("Goodbye.")
        exit()


def checkScore(count, board, player, bot):
    if (board.Board['1'] == board.Board['2'] == board.Board['3'] == player.Player.character or
            board.Board['4'] == board.Board['5'] == board.Board['6'] == player.Player.character or
            board.Board['7'] == board.Board['8'] == board.Board['9'] == player.Player.character or
            board.Board['1'] == board.Board['4'] == board.Board['7'] == player.Player.character or
            board.Board['2'] == board.Board['5'] == board.Board['8'] == player.Player.character or
            board.Board['3'] == board.Board['6'] == board.Board['9'] == player.Player.character or
            board.Board['1'] == board.Board['5'] == board.Board['9'] == player.Player.character or
            board.Board['3'] == board.Board['5'] == board.Board['7'] == player.Player.character):
        board.printBoard(board)
        print("You won")
    elif (board.Board['1'] == board.Board['2'] == board.Board['3'] == player.Bot.character or
          board.Board['4'] == board.Board['5'] == board.Board['6'] == player.Bot.character or
          board.Board['7'] == board.Board['8'] == board.Board['9'] == player.Bot.character or
          board.Board['1'] == board.Board['4'] == board.Board['7'] == player.Bot.character or
          board.Board['2'] == board.Board['5'] == board.Board['8'] == player.Bot.character or
          board.Board['3'] == board.Board['6'] == board.Board['9'] == player.Bot.character or
          board.Board['1'] == board.Board['5'] == board.Board['9'] == player.Bot.character or
          board.Board['3'] == board.Board['5'] == board.Board['7'] == player.Bot.character):
        board.printBoard(board)
        print("Bot won")

    restart()


def play(player, bot):
    count = 0
    space = " "

    while count < 9:  # loop until all spaces are filled
        print(board.printBoard(board.Board))

        if player.Player.turn:
            print("Your turn. Pick a space: ")
            space = input()
            if board.Board[str(space)] == ' ':           # if space is empty,
                board.Board[str(space)] = player.Player.character
                count += 1
            else:                                   # space is occupied
                print("Space already filled.\nPick a space: ")
                continue
        else:
            print("Bot's turn")
            botSpace = random.randint(1, 9)
            if board.Board[str(botSpace)] == ' ':    # if space is empty
                board.Board[str(botSpace)] = player.Bot.character
                count += 1
            else:                               # space is occupied
                continue

        # switch turn
        player.Player.turn = not player.Player.turn

        if 5 <= count < 9:
            checkScore(count, board, player, bot)
        elif count == 9:
            print("It's a tie.")


def whoGoesFirst():
    print("Call the coin toss: ")
    call = input()
    coin = random.randint(1, 2)  # heads = 1, tails = 2

    if call in ['h', 'H', 'heads', 'Heads', 'HEADS']:
        call = 1
    else:
        call = 2

    if call == coin:
        player.Player.turn = True
        print("You WON the coin toss. You will go first. Pick your character (X or O): ")
    else:
        print("You LOST the coin toss. Bot will go first. Pick your character (X or O): ")
        player.Player.turn = False
    character = input()
    if character in ['x', 'X']:
        player.Player.character = 'X'
        player.Bot.character = "O"
    else:
        player.Player.character = 'O'
        player.Bot.character = 'X'
    print("You: " + player.Player.character)
    print("Bot: " + player.Bot.character)
    play(player, player.Bot)


class Game(object):  # initiate the game
    def __init__(self):
        self.board = board.Board
        self.player = player.Player
        self.bot = player.Bot
        whoGoesFirst()


game = Game()

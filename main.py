from row import Row, Color
from board import Board
import random


def createGuess(poss):
    return random.choice(poss)


def startGame(gameBoard):
    print("Game start:")
    while True:
        input("Press enter to guess\n")
        board.addRow(createGuess(board.possibilities))
        board.printBoard()
        black = int(input("Enter amount of black\n"))
        white = int(input("Enter amount of white\n"))
        board.addResult(black, white)
        board.printBoard()
        poss = board.printPossibilities(False)
        if poss == 0:
            print("Error!! no matching possibilities")
            break
        if black == 4:
            print("You win in", board.turns, "turns!!!")
            break
        if board.turns == 10:
            print("You Lose")
            break


if __name__ == '__main__':
    board = Board()
    board.fillPossibilities()
    startGame(board)





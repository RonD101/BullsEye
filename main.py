from row import Row, Color
from board import Board
import random

def createGuess(poss):
    return random.choice(poss)


def startGame(gameBoard, isPlayer, computerInput, data):
    # print("Game start:")
    data[0] += 1
    while True:
        currGuess = createGuess(gameBoard.possibilities)
        if isPlayer is True:
            input("Press enter to guess\n")
            gameBoard.addRow(currGuess)
            gameBoard.printBoard()
            black = int(input("Enter amount of black\n"))
            white = int(input("Enter amount of white\n"))
            gameBoard.addResult(black, white)
            gameBoard.printBoard()
        else:
            black = gameBoard.addRowWithHiddenPattern(computerInput, currGuess)
        poss = gameBoard.printPossibilities(False, False)
        if poss == 0:
            gameBoard.printBoard()
            print("Error!! no matching possibilities")
            data[3] += 1
            break
        if black == 4:
            # gameBoard.printBoard()
            # print("You win in", gameBoard.turns, "turns!!!")
            data[1] = (data[1] * data[4] + gameBoard.turns) / (data[4] + 1)
            data[4] += 1
            data[5] = min(data[5], gameBoard.turns)
            data[6] = max(data[6], gameBoard.turns)
            data[7][gameBoard.turns] = data[7].get(gameBoard.turns, 0) + 1
            break
        if gameBoard.turns == 10:
            data[2] += 1
            gameBoard.printBoard()
            print("You Lose")
            break


if __name__ == '__main__':
    data = [0, 0, 0, 0, 0, 10, 0, {}]  # [#Games, #AvrageTurns, #Loses, #Errors, #Wins, #MinTurns, #MaxTurns, {AmountOfTurns: #Acc}]

    def printData():
        print("Games played: ", data[0])
        print("Average turns: ", data[1])
        print("Amount of wins: ", data[4])
        print("Amount of loses: ", data[2])
        print("Amount of errors: ", data[3])
        print("Min turns: ", data[5])
        print("Max turns: ", data[6])
        for key in sorted(data[7]):
            print("%s: %s" % (key, data[7][key]))
    board = Board()
    isPlayer = input("Enter p to play again human\n") == 'p'
    numberOfGames = 4000
    if isPlayer is True:
        numberOfGames = 1
    for i in range(1, numberOfGames + 1):
        poss = board.fillPossibilities()
        computerInput = createGuess(poss)
        startGame(board, isPlayer, computerInput, data)
        board.cleanBoard()
        if i % 1000 == 0:
            printData()
    printData()





from row import *
from termcolor import colored


class Board:
    row = []
    turns = 0
    possibilities = []

    def fillPossibilities(self):
        hashColor = [-1, -1, -1, -1]
        for color1 in Color:
            hashColor[0] = color1.value
            for color2 in Color:
                hashColor[1] = color2.value
                for color3 in Color:
                    hashColor[2] = color3.value
                    for color4 in Color:
                        hashColor[3] = color4.value
                        if hashColor[0] == hashColor[1] or hashColor[0] == hashColor[2] or hashColor[0] == hashColor[
                            3] or hashColor[1] == hashColor[2] or hashColor[1] == hashColor[3] or hashColor[2] == \
                                hashColor[3]:
                            continue
                        Board.possibilities.append([color1, color2, color3, color4])
        return Board.possibilities

    def printPossibilities(self, shouldPrint=True, GUI=False):
        if GUI is True:
            print("All possible patterns:")
            for poss in Board.possibilities:
                print(colored(poss[0].name, poss[0].name), colored(poss[1].name, poss[1].name),
                      colored(poss[2].name, poss[2].name), colored(poss[3].name, poss[3].name))
        if shouldPrint is True:
            print("Total possibilities: ", len(Board.possibilities))
        return len(Board.possibilities)

    def addRow(self, newRow):
        Board.row.append(Row().createRow(newRow, 0, 0))
        Board.turns += 1

    def addRowWithHiddenPattern(self, hiddenPattern, guess):
        Board.row.append(Row().createRowWithHiddenPattern(hiddenPattern, guess))
        Board.turns += 1
        removePossibilities\
        (self, self.possibilities)
        return Board.row[-1].black

    def addResult(self, black, white):
        assert (black + white <= 4 and black >= 0 and white >= 0 and "Result parameter are incorrect")
        Board.row[-1].black = black
        Board.row[-1].white = white
        # Here you need to change guessing algorithm
        removePossibilities(self, self.possibilities)

    def printBoard(self):
        for row in Board.row:
            print("--------------------------------")
            row.printRow()
            print("--------------------------------")

    def cleanBoard(self):
        Board.row.clear()
        Board.turns = 0
        Board.possibilities.clear()


def removePossibilities(board, possibilities):
    for pos in possibilities[:]:
        for row in board.row:
            black = 0
            white = 0
            for i in range(4):
                if row.guess[i].name == pos[i].name:
                    black += 1
            for i in range(4):
                for j in range(4):
                    if i != j and row.guess[i].name == pos[j].name:
                        white += 1
            if row.white != white or row.black != black:
                possibilities.remove(pos)
                break

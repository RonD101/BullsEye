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

    def printPossibilities(self):
        for poss in Board.possibilities:
            print(colored(poss[0].name, poss[0].name), ", ", colored(poss[1].name, poss[1].name), ", ",
                  colored(poss[2].name, poss[2].name), ", ", colored(poss[3].name, poss[3].name))
        print("Amount of Total possibilities: ", len(Board.possibilities))

    def addRow(self, newRow):
        Board.row.append(Row(newRow, 0, 0))
        Board.turns += 1

    def addResult(self, black, white):
        assert (black + white <= 4 and black >= 0 and white >= 0 and "Result parameter are incorrect")
        Board.row[-1].black = black
        Board.row[-1].white = white
        # Here you need to change guessing algorithm
        # fix possibilities

    def printBoard(self):
        for row in reversed(Board.row):
            print("--------------------------------")
            row.printRow()
            print("--------------------------------")


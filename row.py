from enum import Enum
from termcolor import colored


class Color(Enum):
    red = 0
    green = 1
    blue = 2
    yellow = 3
    magenta = 4
    cyan = 5


class Info(Enum):
    Black = 0
    White = 1


class Row:
    def __init__(self):
        self.guess = []
        self.white = 0
        self.black = 0
        # self.createRow(guess, white, black)

    def createRow(self, guess, white, black):
        self.guess = guess
        self.white = white
        self.black = black
        return self

    def createRowWithHiddenPattern(self, hiddenPattern, guess):
        self.guess = guess
        self.black = len([True for i in range(4) if hiddenPattern[i].name == guess[i].name])
        self.white = len([True for i, value in enumerate(guess) if value in hiddenPattern and hiddenPattern[i].name != value.name])
        return self

    def printRow(self):
        print(colored(self.guess[0].name, self.guess[0].name), colored(self.guess[1].name, self.guess[1].name),
              colored(self.guess[2].name, self.guess[2].name), colored(self.guess[3].name, self.guess[3].name),
              end=" | ")
        for i in range(int(self.black)):
            print(colored(" ", "grey", "on_grey"), end=" ")
        for i in range(int(self.white)):
            print(colored(" ", "white", "on_white"), end=" ")
        print("")


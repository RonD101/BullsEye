
from row import Row, Color
from board import Board


if __name__ == '__main__':
    board = Board()
    board.fillPossibilities()
    board.printPossibilities()
    board.addRow([Color.red, Color.blue, Color.yellow, Color.green])
    board.addResult(1, 2)
    board.addRow([Color.magenta, Color.cyan, Color.red, Color.blue])
    board.addResult(1, 3)
    board.printBoard()


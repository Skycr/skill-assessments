###Miniproject: Tic-Tac-Toe
import pandas as pd
import numpy as np
from numpy import random
import time


class Tictactoe:
    def __init__(self):
        self.matrix = np.array(["."] * 9).reshape(3, 3)

    # error handling for cmd input
    def main(self):
        while True:
            symbol = input("X or O? ")
            if symbol not in ("X", "O"):
                time.sleep(1)
                print("Invalid response. Choose X or O")
            else:
                self.gameloop(symbol)

    def rc_handling(self, XO, matrix):
        while True:
            input_r = int(input("What row? "))
            input_c = int(input("What column "))
            if input_r >= 3 or input_c >= 3:
                print("Invalid selection. Choose 0, 1, or 2 for row and column")
            elif matrix[input_r][input_c] == ".":
                matrix[input_r][input_c] = XO
                break
            else:
                print("error, try again")

    def wincon(self, XO):
        time.sleep(1)
        if XO == "X":
            print("X has won")
            raise SystemExit
        elif XO == "O":
            print("O has won")
            raise SystemExit

    # check if game is draw
    def checkdraw(self, matrix):
        time.sleep(1)
        if np.any(matrix == ".") == False:
            print("Game is a draw")
            raise SystemExit

    # check rows and columns for matches in matrix
    def checkrc(self, matrix):
        for row in matrix:
            if len(set(row)) == 1 and "X" in set(row):
                self.wincon("X")
            elif len(set(row)) == 1 and "O" in set(row):
                self.wincon("O")

        for column in np.transpose(matrix):
            if len(set(column)) == 1 and "X" in set(column):
                self.wincon("X")
            elif len(set(column)) == 1 and "O" in set(column):
                self.wincon("O")

    # check diagonals in matrix
    def checkdiagonals(self, matrix):
        # check left to right diagonoal
        di_lr = np.diag(matrix)
        if len(set(di_lr)) == 1 and "X" in set(di_lr):
            self.wincon("X")
        elif len(set(di_lr)) == 1 and "O" in set(di_lr):
            self.wincon("O")

        # check right to left diagonal
        di_rl = np.diag(np.fliplr(matrix))
        if len(set(di_rl)) == 1 and "X" in set(di_rl):
            self.wincon("X")
        elif len(set(di_rl)) == 1 and "O" in set(di_rl):
            self.wincon("O")

    def player(self, XO, matrix):
        print(f"Player {XO}'s turn")
        self.rc_handling(XO, matrix)
        time.sleep(1)
        print(f"""\

Current Board

{"~" * 21}

{pd.DataFrame(matrix)}

{"~" * 21}
""")
        self.checkrc(matrix)
        self.checkdiagonals(matrix)
        self.checkdraw(matrix)

    def computer(self, XO, matrix):
        print("\n" + "Computer's turn")
        m = np.argwhere(matrix == ".")
        cp = m[np.random.choice(m.shape[0])]
        matrix[cp[0]][cp[1]] = XO
        time.sleep(1)

        print(f"""\

Current Board

{"~" * 21}

{pd.DataFrame(matrix)}

{"~" * 21}
""")
        self.checkrc(matrix)
        self.checkdiagonals(matrix)
        self.checkdraw(matrix)

    def gameloop(self, XO):
        counter = 1
        while True:
            time.sleep(1)
            print(f"""\

{"#" * 21}


{"#" * 6} Round {counter} {"#" * 6}


{"#" * 21}
""")
            time.sleep(1)
            print(f"""\

Current Board

{"~" * 21}

{pd.DataFrame(self.matrix)}

{"~" * 21}
""")
            time.sleep(1)
            if XO == "X":
                self.player("X", self.matrix)
                self.computer("O", self.matrix)
            elif XO == "O":
                self.computer("X", self.matrix)
                self.player("O", self.matrix)
            counter += 1


Tictactoe().main()

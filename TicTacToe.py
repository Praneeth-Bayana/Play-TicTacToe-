import tkinter as tk  # Using tkinter for GUI
from tkinter import messagebox

class BoardGame:  # Creating a class
    def __init__(self):
        self.turn = "x"  # To keep track of the current player
        self.gameBoard = [["", "", ""], ["", "", ""], ["", "", ""]]  # Creating a 3x3 board
        self.appWindow = tk.Tk()  # Initializing the main window with Tkinter
        self.appWindow.title("TicTacToe")  # Setting the window title

        self.cellButtons = []  # Creating a list for the cell buttons

        for row in range(3):
            buttonRow = []
            for col in range(3):
                cell = tk.Button(self.appWindow, text="", width=20, height=10,
                                 command=lambda row=row, col=col: self.playerAction(row, col))
                cell.grid(row=row, column=col)
                buttonRow.append(cell)
            self.cellButtons.append(buttonRow)

    def playerAction(self, row, col):
        if self.gameBoard[row][col] == "":
            self.gameBoard[row][col] = self.turn
            self.cellButtons[row][col].config(text=self.turn)
            if self.checkForWin(self.turn):
                messagebox.showinfo("Game Over", "The winner is " + self.turn)
                self.appWindow.quit()
            elif self.checkForDraw():
                messagebox.showinfo("Game Over", "It's a Draw")
                self.appWindow.quit()

            self.turn = "o" if self.turn == "x" else "x"

    def checkForWin(self, player):
        for i in range(3):
            if player == self.gameBoard[i][0] == self.gameBoard[i][1] == self.gameBoard[i][2]:
                return True
            if player == self.gameBoard[0][i] == self.gameBoard[1][i] == self.gameBoard[2][i]:
                return True
        if player == self.gameBoard[0][0] == self.gameBoard[1][1] == self.gameBoard[2][2]:
            return True
        if player == self.gameBoard[0][2] == self.gameBoard[1][1] == self.gameBoard[2][0]:
            return True
        return False

    def checkForDraw(self):
        for row in self.gameBoard:
            if "" in row:
                return False
        return True

    def startGame(self):
        self.appWindow.mainloop()

gameInstance = BoardGame()
gameInstance.startGame()

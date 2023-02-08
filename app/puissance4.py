import tkinter as tk

class PowerFourGUI:
    def __init__(self, master):
        self.master = master
        self.grid = [[0 for x in range(7)] for y in range(6)]
        self.player = 1
        self.buttons = []
        for row in range(6):
            button_row = []
            for col in range(7):
                button = tk.Button(master, text=" ", command=lambda row=row, col=col: self.play(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def play(self, row, col):
        for i in range(6):
            if self.grid[5 - i][col] == 0:
                self.grid[5 - i][col] = self.player
                if self.player == 1:
                    color = "red"
                else:
                    color = "blue"
                self.buttons[5 - i][col].config(bg=color)
                break

        if self.check_winner():
            tk.messagebox.showinfo("Winner", "Player {} wins!".format(self.player))
            self.master.quit()

        if all(all(val != 0 for val in row) for row in self.grid):
            tk.messagebox.showinfo("Draw", "Draw!")
            self.master.quit()

        self.player = 3 - self.player

    def check_winner(self):
        # check rows
        for row in self.grid:
            for i in range(4):
                if row[i:i + 4] == [self.player, self.player, self.player, self.player]:
                    return True

        # check columns
        for col in range(7):
            for i in range(3):
                if [self.grid[i][col], self.grid[i + 1][col], self.grid[i + 2][col], self.grid[i + 3][col]] == [self.player, self.player, self.player, self.player]:
                    return True

        # check diagonals
        for row in range(3):
            for col in range(4):
                if [self.grid[row][col], self.grid[row + 1][col + 1], self.grid[row + 2][col + 2], self.grid[row + 3][col + 3]] == [self.player, self.player, self.player, self.player]:
                    return True
                if [self.grid[row][col + 3], self.grid[row + 1][col + 2], self.grid[row + 2][col + 1], self.grid[row + 3][col]] == [self.player, self.player, self.player, self.player]:
                    return True
        return False

root = tk.Tk()
game = PowerFourGUI(root)
root.mainloop()

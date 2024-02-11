import tkinter as tk
import tkinter.messagebox
import random

# Initialize the game board
board = [" " for i in range(9)]

# Initialize variables
player = "X"
computer = "O"

# Function to check for a winning condition
win_conditions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def check_winner():
    for i in range(8):
        condition=win_conditions[i]
        if board[condition[0]] == board[condition[1]] == board[condition[2]] !=" ": 
            return board[condition[0]]
        # Check for a tie
        if " " not in board:
            return "Tie"
        
    return None

# Function to update the board
def update_board(index, symbol):           # Symbole is X or O
    board[index] = symbol
    buttons[index].config(text=symbol, state="disabled")

# Function for computer's move
def computer_move():
    empty_cells = [i for i in range(9) if board[i] == " "]
    if empty_cells:
        index = random.choice(empty_cells)
        update_board(index, computer)
        winner = check_winner()
        if winner:
            show_result(winner)
    else:
        show_result("Tie")

# Function to handle player's move
def player_move(index):
    update_board(index, player)
    winner = check_winner()
    if not winner:
        computer_move()
    else:
        show_result(winner)

# Function to display result
def show_result(winner):
    if winner == player:
        tkinter.messagebox.showinfo("Tic Tac Toe", "Congratulations! You win!")
    elif winner == computer:
        tkinter.messagebox.showinfo("Tic Tac Toe", "You lose!")
    else:
        tkinter.messagebox.showinfo("Tic Tac Toe", "It's a tie!")
    reset_game()

# Function to reset the game
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state="normal")

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Helvetica", 20), width=5, height=2,
                       command=lambda i=i: player_move(i))
    button.grid(row=i // 3, column=i % 3, sticky="nsew")
    buttons.append(button)

# Run the game
root.mainloop()

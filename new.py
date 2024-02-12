import tkinter as tk
import tkinter.messagebox
import random

n = 5
# Initialize the game board
board = [" " for _ in range(n**2)]

# Initialize variables
player = "X"
computer = "O"

# Create buttons
def board_button(root):
    global buttons
    buttons = []
    for i in range(n * n):
        button = tk.Button(root,text=" ",font=("Helvetica", 20),width=5,height=2,command=lambda i=i: player_move(i))
        button.grid(row=i // n, column=i % n, sticky="nsew")
        buttons.append(button)

# Function to check for a winner
def check_winner():
  # Check rows
  count = 0
  for i in range(0, n * n, n):
    b = board[i]
    for j in range(n - 1):
      b = board[i + j]
      if b == board[i + j + 1] and b != " ":
        count = count + 1
      if count == n - 1:
        return board[i]
  # Check columns
  count = 0
  for i in range(n):
    for j in range(n - 1):
      b = board[n * j + i]
      if b == board[n * (j + 1) + i] and b != " ":
        count = count + 1
      if count == n - 1:
        return board[n * j + i]

  # Check diagonals
  count = 0
  for i in range(n - 1):
    b = board[n * i + i]
    if b == board[n * (i + 1) + (i + 1)] and b != " ":
      count = count + 1
    if count == n - 1:
      return board[n * i + i]

  # Check anti-diagonals
  count = 0
  for i in range(1, n + 1):
    b = board[n * i - i]
    #count = 0
    if b == board[n * (i + 1) - (i + 1)] and b != " ":
      count = count + 1
    if count == n - 1:
      return board[n * i - i]

  # Check for tie
  if " " not in board:
    return "Tie"
  return None


# Function to update the board
def update_board(index, symbol):
  board[index] = symbol
  buttons[index].config(text=symbol, state="disabled")


# Function for computer's move
def computer_move():
  empty_cells = [i for i in range(n * n) if board[i] == " "]
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
  board = [" " for _ in range(n * n)]
  for button in buttons:
    button.config(text=" ", state="normal")


# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry('350x350')
btn1=tk.Button(root,text="Play with Computer",bd='5',command=lambda : board_button(root))
btn1.grid(row=0, column=3, padx=100)
btn2=tk.Button(root,text="Play with Other Player",bd='5',command=lambda : board_button(root))
btn2.grid(row=1, column=3, pady=10, padx=100)
btn3=tk.Button(root,text="Quit !",bd='5',command=root.destroy)
btn3.grid(row=2, column=3, pady=20, padx=100)

# Run the game
root.mainloop()

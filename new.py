import tkinter as tk
import tkinter.messagebox
import random

n = 3
# Initialize the game board
board = [" " for _ in range(n**2)]

# Initialize variables
player = "x"
computer = "o"
player2 = 'O'
player1 = 'X'

#Hiding buttons
def forget():
  btn1.grid_forget()
  btn2.grid_forget()
  btn3.grid_forget()
  btn3.grid(row=1, column=3, pady=20, padx=100)

#for count of move
def count0():
  global move_count
  move_count = 0

count0()
# Retrive hidden buttons
def retrieve():
  btn2.grid(row=1, column=3, pady=10, padx=100)
  btn1.grid(row=0, column=3, padx=100)
  btn3.grid_forget()
  btn3.grid(row=2, column=3, pady=20, padx=100)


#Remove board window to go to 1st option window
def removeboard():
  for i in buttons:
    i.grid_forget()


# Create buttons
def board_button(root):
  global buttons
  buttons = []
  for i in range(n * n):
    button = tk.Button(root,
                       text=" ",
                       font=("Helvetica", 20),
                       width=5,
                       height=2,
                       command=lambda i=i: player_move(i))
    button.grid(row=i // n, column=i % n, sticky="nsew")
    buttons.append(button)
  forget()


# MAKE MOVE FOR ALL PLAYERS
def make_move(index):
  global move_count
  if (move_count % 2 == 0):
    update_board(index, player1)
    move_count += 1
  else:
    update_board(index, player2)
    move_count += 1
  winner = check_winner()
  if winner:
    show_result(winner)


# Create buttons
def board_button2(root):
  global buttons
  buttons = []
  for i in range(n * n):
    button = tk.Button(root,
                       text=" ",
                       font=("Helvetica", 20),
                       width=5,
                       height=2,
                       command=lambda i=i: make_move(i))
    button.grid(row=i // n, column=i % n, sticky="nsew")
    buttons.append(button)
  forget()


# Function to check for a winner
def check_winner():
  # Check rows
  count = 0
  for i in range(0, n * n, n):
    count = 0
    for j in range(n - 1):
      b = board[i + j]
      if b == board[i + j + 1] and b != " ":
        count = count + 1
      if count == n - 1:
        return board[i]
  # Check columns
  count = 0
  for i in range(n):
    count = 0
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
  global move_count
  if winner == player1:
    tkinter.messagebox.showinfo("Tic Tac Toe",
                                "Congratulations! Player X win!")
  elif winner == computer:
    tkinter.messagebox.showinfo("Tic Tac Toe", "You lose!")
  elif winner == player:
    tkinter.messagebox.showinfo("Tic Tac Toe", "You Win!")
  elif winner == player2:
    tkinter.messagebox.showinfo("Tic Tac Toe",
                                "Congratulations! Player O win!")
  else:
    tkinter.messagebox.showinfo("Tic Tac Toe", "It's a tie!")
  removeboard()
  retrieve()
  del move_count
  count0()

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry('350x350')
btn1 = tk.Button(root,
                 text="Play with Computer",
                 bd='5',
                 command=lambda: board_button(root))
btn1.grid(row=0, column=3, padx=100)
btn2 = tk.Button(root,
                 text="Play with Other Player",
                 bd='5',
                 command=lambda: board_button2(root))
btn2.grid(row=1, column=3, pady=10, padx=100)
btn3 = tk.Button(root, text="Quit !", bd='5', command=root.destroy)
btn3.grid(row=2, column=3, pady=20, padx=100)

# Run the game
root.mainloop()

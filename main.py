import random
import tkinter as tk
from tkinter import messagebox

board = [" " for _ in range(9)]
player_turn = ""
player_icon = ""
computer_icon = ""
game_mode = ""
start_first = ""

def display_board():
    print(f"\n| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |\n")

def is_win(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
            (board[3] == icon and board[4] == icon and board[5] == icon) or \
            (board[6] == icon and board[7] == icon and board[8] == icon) or \
            (board[0] == icon and board[3] == icon and board[6] == icon) or \
            (board[1] == icon and board[4] == icon and board[7] == icon) or \
            (board[2] == icon and board[5] == icon and board[8] == icon) or \
            (board[0] == icon and board[4] == icon and board[8] == icon) or \
            (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

def is_not_available(space):
    if board[space - 1] == "X" or board[space - 1] == "O":
        return True
    else:
        return False

def player_move(player, icon, space):
    if space < 1 or space > 9:
        messagebox.showinfo("Invalid Move", "Invalid input. Please enter a value between 1 and 9.")
        return

    if is_not_available(space):
        messagebox.showinfo("Invalid Move", "Space already taken. Please select an unused space.")
        return

    board[space - 1] = icon
    update_board()

    if is_win(icon):
        messagebox.showinfo("Game Over", f"{player} [{icon}] Won! Congratulations!")
        reset_game()
    elif is_draw():
        messagebox.showinfo("Game Over", "The game ended in a draw.")
        reset_game()
    elif game_mode == "Computer" and player == "Player":
        computer_move()

def computer_move():
    while True:
        space = random.randint(1, 9)
        if not is_not_available(space):
            board[space - 1] = computer_icon
            update_board()

            if is_win(computer_icon):
                messagebox.showinfo("Game Over", f"Computer [{computer_icon}] Won! Hard Luck!")
                reset_game()
            elif is_draw():
                messagebox.showinfo("Game Over", "The game ended in a draw.")
                reset_game()

            break

def update_board():
    for i in range(9):
        buttons[i].config(text=board[i])

def reset_game():
    global board
    board = [" " for _ in range(9)]
    update_board()

def start_game():
    global player_turn, player_icon, computer_icon, game_mode, start_first

    player_turn = game_mode_var.get()
    start_first = first_turn_var.get()

    if player_icon_var.get() == 1:
        player_icon = "X"
        computer_icon = "O"
    else:
        player_icon = "O"
        computer_icon = "X"

    if start_first == "Player":
        player_turn = "Player"
        messagebox.showinfo("Game Start", "You will start the game.")
    else:
        player_turn = "Computer"
        messagebox.showinfo("Game Start", "Computer will start the game.")

    reset_game()

def button_click(index):
    global player_turn

    if player_turn == "Player":
        player_move("Player", player_icon, index + 1)
        player_turn = "Computer"

        if not is_win(player_icon) and not is_draw():
            if game_mode == "Player":
                player_turn = "Player"
            elif game_mode == "Computer":
                player_turn = "Computer"
                computer_move()

def show_welcome_page():
    global game_mode_var, first_turn_var, player_icon_var
    welcome_page = tk.Toplevel(root)
    welcome_page.title("Welcome to Tic Tac Toe")

    game_mode_label = tk.Label(welcome_page, text="Select thegame mode:")
    game_mode_label.pack()

    game_mode_var = tk.StringVar()
    game_mode_var.set("Computer")

    game_mode_radio1 = tk.Radiobutton(welcome_page, text="Play against the computer", variable=game_mode_var, value="Computer")
    game_mode_radio1.pack()

    game_mode_radio2 = tk.Radiobutton(welcome_page, text="Play against another player", variable=game_mode_var, value="Player")
    game_mode_radio2.pack()

    first_turn_label = tk.Label(welcome_page, text="Who starts first?")
    first_turn_label.pack()

    first_turn_var = tk.StringVar()
    first_turn_var.set("Player")

    first_turn_radio1 = tk.Radiobutton(welcome_page, text="Player", variable=first_turn_var, value="Player")
    first_turn_radio1.pack()

    first_turn_radio2 = tk.Radiobutton(welcome_page, text="Computer", variable=first_turn_var, value="Computer")
    first_turn_radio2.pack()

    player_icon_label = tk.Label(welcome_page, text="Choose your character:")
    player_icon_label.pack()

    player_icon_var = tk.IntVar()
    player_icon_var.set(1)

    player_icon_radio1 = tk.Radiobutton(welcome_page, text="X", variable=player_icon_var, value=1)
    player_icon_radio1.pack()

    player_icon_radio2 = tk.Radiobutton(welcome_page, text="O", variable=player_icon_var, value=2)
    player_icon_radio2.pack()

    start_game_button = tk.Button(welcome_page, text="Start Game", command= start_game)
    start_game_button.pack()

    welcome_page.mainloop()


root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", width=10, height=5, command=lambda index=i: button_click(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

show_welcome_page()
root.mainloop()
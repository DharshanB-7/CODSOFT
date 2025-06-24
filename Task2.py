import tkinter as tk
from tkinter import messagebox
import math

# Initialize board
board = [" " for _ in range(9)]
buttons = []

# Check win
def check_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(brd[i] == player for i in cond) for cond in win_conditions)

def is_draw(brd):
    return " " not in brd

# Minimax with alpha-beta
def minimax(brd, depth, is_max, alpha, beta):
    if check_winner(brd, "O"):
        return 1
    if check_winner(brd, "X"):
        return -1
    if is_draw(brd):
        return 0

    if is_max:
        max_eval = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, depth + 1, False, alpha, beta)
                brd[i] = " "
                max_eval = max(max_eval, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, depth + 1, True, alpha, beta)
                brd[i] = " "
                min_eval = min(min_eval, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return min_eval

# AI move
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
    buttons[move].config(text="O", state="disabled")
    check_game_over("O")

# Check if game is over
def check_game_over(player):
    if check_winner(board, player):
        messagebox.showinfo("Game Over", f"{player} wins!")
        disable_all_buttons()
        return True
    elif is_draw(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        disable_all_buttons()
        return True
    return False

# Human move
def on_click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i].config(text="X", state="disabled")
        if not check_game_over("X"):
            window.after(500, ai_move)

# Disable all buttons
def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")

# Reset the game
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ", state="normal")

# Create GUI window
window = tk.Tk()
window.title("Tic-Tac-Toe: Human vs AI")

frame = tk.Frame(window)
frame.pack()

# Create 3x3 buttons
for i in range(9):
    btn = tk.Button(frame, text=" ", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Reset button
reset_btn = tk.Button(window, text="Reset", font=("Arial", 14), command=reset_game)
reset_btn.pack(pady=10)

window.mainloop()

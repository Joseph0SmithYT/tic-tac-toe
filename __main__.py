# I'M IMPROVISING, IF YOU SEE THIS I WAS THROUGH HELL
import os

tictactoe = {
    "A1": " ",
    "A2": " ",
    "A3": " ",
    "B1": " ",
    "B2": " ",
    "B3": " ",
    "C1": " ",
    "C2": " ",
    "C3": " "
    }


def main():
    print_grid()
    while not check_win(tictactoe) or not is_tie(tictactoe):
        player = "X"
        position = input("Enter the position (eg. A1, B3, C2): ").upper()
        if not position in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
            print("Invalid position")
            continue
        if not tictactoe[position] == " ":
            print("Can't place there!")
            continue    
        tictactoe[position] = player
        print_grid()
        gameState(tictactoe, player) #Checks if there's a winner or tie
        tictactoe[get_ai_move(tictactoe)] = "O"
        print_grid()
        gameState(tictactoe, "O")

def validate_input(player, position):
    def other_sign(player):
        if player == "X":
            return "O"
        return "X"
    if other_sign(player) == tictactoe[position]:
        return True
    return False

def print_grid():
    clean_board()
    print(f"Your player: X\nAI player: O\n\n  | 1 | 2 | 3\nA | {tictactoe['A1']} | {tictactoe['A2']} | {tictactoe['A3']}\nB | {tictactoe['B1']} | {tictactoe['B2']} | {tictactoe['B3']}\nC | {tictactoe['C1']} | {tictactoe['C2']} | {tictactoe['C3']}\n")

def gameState(board, player):
    if check_win(board):
        if player == "O":
            print("AI wins!")
            exit()
        print(f"You win!")
        exit()  
    if is_tie(board):
        print("Its a tie!")
        exit()


def available_moves(board):
    return [k for k, v in board.items() if v == " "]
            
def minimax(board, depth, maximizing_player):
    if check_win(board):
        return -1 if maximizing_player else 1  # Negative score for maximizing player (loss)
    if is_tie(board):
        return 0
    elif maximizing_player:
        max_eval = float('-inf')
        for move in available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False)
            board[move] = ' '  # Undo the move
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True)
            board[move] = ' '  # Undo the move
            min_eval = min(min_eval, eval)
        return min_eval

def is_tie(board):
    if not check_win(board) and available_moves(board) == []:
        return True
    return False

def get_ai_move(board):
    best_score = float('-inf')
    best_move = None
    for move in available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '  # Undo the move
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
def check_win(board):

    # Check rows
    for row in ['A', 'B', 'C']:
        if board[row + '1'] + board[row + '2'] + board[row + '3'] == "XXX" or board[row + '1'] + board[row + '2'] + board[row + '3'] == "OOO":
            return True

    # Check columns
    for col in ['1', '2', '3']:
        combo = board['A' + col] + board['B' + col] + board['C' + col]
        if combo == "XXX" or combo == "OOO":
            return True

    # Check diagonals
    if board['A1'] + board['B2'] + board['C3'] == "XXX" or board['A1'] + board['B2'] + board['C3'] == "OOO":
        return True
    if board['A3'] + board['B2'] + board['C1'] == "XXX" or board['A3'] + board['B2'] + board['C1'] == "OOO":
        return True

    return False

def clean_board():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()


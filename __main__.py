# I'M IMPROVISING, IF YOU SEE THIS I WAS THROUGH HELL
import os

class Mark():
    def __init__(self, label):
        self.label = label.upper()
    def opposite(self):
        if self.label == "X":
            return "O"
        elif self.label == "O":
            return "X"
        else:
            return None

board = {
    "A1": Mark(" "), "A2": Mark(" "), "A3": Mark(" "),
    "B1": Mark(" "), "B2": Mark(" "), "B3": Mark(" "),
    "C1": Mark(" "), "C2": Mark("O"), "C3": Mark(" "),
}

def print_grid():
    print(f"Your player: X\nAI player: O\n\n  | 1 | 2 | 3\n\
A | {board['A1'].label} | {board['A2'].label} | {board['A3'].label}\n\
B | {board['B1'].label} | {board['B2'].label} | {board['B3'].label}\n\
C | {board['C1'].label} | {board['C2'].label} | {board['C3'].label}\n")

def clean_grid():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def place_mark(mark, position, board):
    validate_input(position, board, mark)
    board[position] = Mark(mark)

def validate_input(position, board, mark):
    if not position in ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']:
        return False
    if board[position].label == Mark(mark).opposite():
        return False
    return True

#! Done
def check_win(board):
    #Rows and columns
    for row in ['A', 'B', 'C']:
        combo = board[row + '1'].label + board[row + '2'].label + board[row + '3'].label
        if combo == "XXX" \
        or combo == "OOO":
            return board[row + '1'].label
    for col in ['1', '2', '3']:
        combo = board['A' + col].label + board['B' + col].label + board['C' + col].label
        if combo == "XXX" or combo == "OOO":
            return board['A' + col].label
    #Diagonals
    combo = board['A1'].label + board['B2'].label + board['C3'].label
    if combo == "OOO" or combo == "XXX":
        return board["B2"].label
    combo = board['A3'].label + board['B2'].label + board['C1'].label
    if combo == "OOO" or combo == "XXX":
        return board["B2"].label
#! Done
def check_tie(board):
    for spot in board:
        if board[spot].label == " ": return False
        continue
    return True


def main():
    position = input("Where do you wanna place ur thingy?: ").upper()
    place_mark("X", position, board)
    print_grid()
    print(Mark("X").opposite())

def offroad():
    

if __name__ == "__main__":
    main()

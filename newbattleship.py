from random import randint
board = []
for i in range (0,5):
    board.append(["O"]*5)

def print_board(board):
    for row in board:
        print(" ".join(row))
print_board(board)

def random_row(board):
    return randint(0,len(board)-1)
def random_col(board):
    return randint(0,len(board)-1)

for turn in range(0,10):
    guess_row = int(input("Guess row :"))
    guess_col = int(input("Guess column :"))

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

if ship_col == guess_col and ship_row == guess_row:
    print ("Congratulations!")
else:
    if ship_col != guess_col and ship_row != guess_row:
        print("Try again")
        turn = turn+1

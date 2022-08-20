# @Sheeye

# Tic Tac Toe AI game

# D = 17.08.2022


import copy
import random

board = [['#' for x in range(3)] for y in range(3)]
out = []
AI_first = False
difficulty = 1

def new_game():
    global board
    board = [['#' for x in range(3)] for y in range(3)]
    if AI_first:
        if difficulty==3:
            board[1][1]='O'
        else:
            make_move(board)


def print_board():
    print("")
    print("  ABC")
    for x in range(3):
        print(x+1,"", end='')
        for y in range(3):
            print(board[x][y],end='')
        print("")

# Only checks if either player already won the game, otherwise returns 0
def evaluate(board2):
    full = True
    for x in range(3):
        if board2[x][0] == board2[x][1] == board2[x][2]:
            if board2[x][0]=='X':
                return -1
            elif board2[x][0]=='O':
                return 1
    for y in range(3):
        if board2[0][y] == board2[1][y] == board2[2][y]:
            if board2[0][y]=='X':
                return -1
            elif board2[0][y]=='O':
                return 1
    if board2[0][0]==board2[1][1]==board2[2][2]:
        if board2[0][0] == 'X':
            return -1
        elif board2[0][0] == 'O':
            return 1
    if board2[0][2]==board2[1][1]==board2[2][0]:
        if board2[0][2] == 'X':
            return -1
        elif board2[0][2] == 'O':
            return 1
    return 0

def someone_won(eval,x,y):
    global AI_first
    if eval != 0:
        print_board()
        if x!=5: # A workaround
            board[x][y] = board3[x][y]
        print_board()
        if eval > 0:
            print("I've won!")
        else:
            print("I guess I lost...")
        print("Let's play again!")
        AI_first = not AI_first
        new_game()
        return evaluate(board3)

# Looks over all combinations 1 move ahead to see if someone will lose or win next turn.
def make_move(board3):
    global board
    global AI_first
    out=[]
    boardMins = [[5 for x in range(3)] for y in range(3)]
    highest = -3
    Full = True
    for x in range(3):
        for y in range(3):
            if board3[x][y]=='#':
                board3[x][y]='O'
                Full=False
                eval = evaluate(board3)
                if eval!=0:
                    someone_won(eval,x,y)
                    return evaluate(board3)
                else: # For every move checks best possible response, and saves the eval in boardMins
                    for z in range(3):
                        for c in range(3):
                            if board3[z][c] == '#':
                                board3[z][c] = 'X'
                                out.append(evaluate(board3))
                                board3[z][c] = '#'
                    for co in out:
                        if co < boardMins[x][y]:
                            boardMins[x][y]=co
                    board3[x][y] = '#'
                    out.clear()
    if Full:
        print_board()
        print("Looks like a draw to me.")
        print("Let's play again!")
        AI_first = not AI_first
        new_game()
        return()
    choices_x=[]
    choices_y=[]
    for x in range(3):
        for y in range(3):
            if boardMins[x][y]>highest and boardMins[x][y]<=1:
                highest = boardMins[x][y]
                choices_y.clear()
                choices_x.clear()
                choices_x.append(x)
                choices_y.append(y)
            elif boardMins[x][y]==highest and boardMins[x][y]<=1:
                choices_x.append(x) # Adds moves of the same value to 2 arrays for x and y values
                choices_y.append(y)

    if difficulty==3:
        check = 0
        while True: # Hard difficulty prefers corners
            print(check)
            if choices_x[check]-choices_y[check]==1 and len(choices_x)>=2:
                choices_x.pop(0)
                choices_y.pop(0)
            else:
                check+=1
                if check>= len(choices_x)-1:
                    break

    lo = random.randint(0,len(choices_x)-1)
    board[choices_x[lo]][choices_y[lo]]='O'

def random_move():
    global board
    global AI_first
    Full=True
    empty_x = []
    empty_y = []
    eval = evaluate(board)
    if eval != 0:
        someone_won(eval,5,5)
        return evaluate(board)
    for x in range(3):
        for y in range(3):
            if board[x][y] == '#':
                empty_x.append(x)
                empty_y.append(y)
                Full=False
            elif x==y==2 and Full:
                print("Looks like a draw to me.")
                print("Let's play again!")
                AI_first = not AI_first
                new_game()
                return ()
    c = random.randint(0,len(empty_x)-1)
    board[empty_x[c]][empty_y[c]]='O'
    eval = evaluate(board)
    if eval != 0:
        someone_won(eval,empty_x[c],empty_y[c])
        return evaluate(board3)
    elif len(empty_x)==1:
        print("Looks like a draw to me.")
        print("Let's play again!")
        AI_first = not AI_first
        new_game()
        return ()



if __name__ == '__main__':
    print("Choose difficulty:\n")
    print("1. Easy - Basically random moves.")
    print("2. Medium - Looks ahead, but with flawed strategy")
    print("3. Hard - A master. Doesn't lose.")
    print("\n Select by typing a number 1-3 below:\n")
    difficulty = int(input())
    print("Tip: Select a square to place a symbol in by putting in coordinates: Eg. 'A1' like in Warships.\n")
    while True:
        print_board()
        print()
        pos = input().upper()
        board[ord(pos[1])-49][ord(pos[0])-65]="X"
        board3 = copy.deepcopy(board)
        if difficulty>=2:
            make_move(board3)
        else:
            random_move()

# &ahead
# @Sheeye

# Simple text-only 2048 game
# Use WASD to move (confirm with enter)
# Could be expanded in the future

# D = 01.08.2022

import random

# Simple, but works well enough for our purposes
clear = "\n" * 100

lost = False
size = 5
board = [[0 for x in range(size)] for y in range(size)]

def you_lost():
    global lost

    print(clear)
    print("You lost!")
    lost = True

def add_numbers(how_many,which):
    empties = 0
    for x in range(size):
        for y in range(size):
            if board[x][y]==0:
                empties+=1
    # I'm aware of the incredibly poor time complexity of this part, not really scalable; But it's a short 1 hour project and not a full fledged game
    if empties>how_many:
        for i in range(how_many):
            while True:
                x = random.randint(0, size-1)
                y = random.randint(0, size-1)
                if board[x][y] == 0:
                    board[x][y] = which
                    break
    else:
        you_lost()

def print_board():
    print()
    for y in range(size):
        for x in range(size):
            print('{0: <4}'.format(board[x][y]),' ',end='')
        print()
    print()

# Board movement functions, 4 for readability, possible to merge if project will be expanded
def move_left():
    for y in range(size):
        x = 0
        while x < size-1:
            if board[x][y]==0:
                if board[x+1][y]!=0:
                    board[x][y]=board[x+1][y]
                    board[x+1][y]=0
                    if x >= 1:
                        x -= 2
            elif board[x][y]==board[x+1][y]:
                board[x][y]*=2
                board[x+1][y]=0
                if x!=0:
                    x-=1
            x+=1

def move_up():
    for x in range(size):
        y = 0
        while y < size-1:
            if board[x][y]==0:
                if board[x][y+1]!=0:
                    board[x][y]=board[x][y+1]
                    board[x][y+1]=0
                    if y >= 1:
                        y -= 2
            elif board[x][y]==board[x][y+1]:
                board[x][y]*=2
                board[x][y+1]=0
                if y!=0:
                    y-=1
            y+=1

def move_right():
    for y in range(size):
        x = size-1
        while x > 0:
            if board[x][y]==0:
                if board[x-1][y]!=0:
                    board[x][y]=board[x-1][y]
                    board[x-1][y]=0
                    if x <= size-2:
                        x += 2
            elif board[x][y]==board[x-1][y]:
                board[x][y]*=2
                board[x-1][y]=0
                if x!=size-1:
                    x+=1
            x-=1

def move_down():
    for x in range(size):
        y = size-1
        while y > 0:
            if board[x][y]==0:
                if board[x][y-1]!=0:
                    board[x][y]=board[x][y-1]
                    board[x][y-1]=0
                    if y <= size-2:
                        y += 2
            elif board[x][y]==board[x][y-1]:
                board[x][y]*=2
                board[x][y-1]=0
                if y!=size-1:
                    y+=1
            y-=1


if __name__ == '__main__':
    add_numbers(5,1)
    print_board()
    while True:
        direction = input()
        if direction=='a':
            move_left()
        elif direction == 'd':
            move_right()
        elif direction == 'w':
            move_up()
        elif direction == 's':
            move_down()
        else:
            print("?????")
        print(clear)
        add_numbers(3,1)
        if lost == False:
            print_board()
        else:
            break


# &perception -012365
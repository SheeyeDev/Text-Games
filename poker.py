# @Sheeye
# Date = 05.09.2022
# Bot playing the well known 'match' game. Each turn a player takes 1,2 or 3 matches, if there are no matches left, the player who took the last match, wins.

# Note: Play on linux, otherwise color codes will not work

import random
import copy

deck = []
hand = [[0 for x in range(2)] for y in range(2)]
opphand = [[0 for x in range(2)] for y in range(2)]
flop = []
yourchips = 1000
oppchips = 1000
blind = 10
pot=10

done = 0

#enemy AI
bluff_multiplier = 0
bluff_counter = 0
call_range = 0
bluff_chance = 0
bravery = 0
raise_willingness = 0
unraised = 0

def initialize():
    global call_range,bluff_chance,bravery,bluff_multiplier, raise_willingness
    bluff_multiplier = random.randint(50,200)
    call_range=(random.randint(80,300))/100.0
    bluff_chance=random.randint(1,25)
    bravery=random.randint(1,25)
    raise_willingness=random.randint(10,35)

    for y in range(4):
        for x in range(9):
            deck.append(str(x+2)+" "+str(y))
        deck.append("A "+str(y))
        deck.append("J "+str(y))
        deck.append("K "+str(y))
        deck.append("Q "+str(y))

def change_color(x):
    if x == '0':
        print("\033[1;34;50m", end="")
    elif x == '1':
        print("\033[1;35;50m", end="")
    elif x == '2':
        print("\033[1;31;50m", end="")
    elif x == '3':
        print("\033[1;32;50m", end="")

def print_hand(hand):
    #print("Your hand: ")
    for x in range(2):
        change_color(hand[x][1])
        print(hand[x][0],"\033[0;0m",end=" ")
    print("")

def add_card():
    y = random.randint(0, len(deck2) - 1)
    what = deck2[y].split(" ")
    flop.append([what[0], what[1]])
    deck2.pop(y)

def create_flop():
    for x in range(3):
        add_card()

def print_flop():
    symbol(flop)
    print("Flop:")
    for x in range(len(flop)):
        change_color(flop[x][1])
        print(flop[x][0],"\033[0;0m", end=" ")
    print("")

def show_info():
    global yourchips,oppchips, hand
    print("Your hand : ")
    print_hand(hand)
    print_flop()
    print("Your chips : " + str(yourchips))
    print("Opponents chips : " + str(oppchips))
    print("Pot : " + str(pot))

def symbol(hand):
    for x in range(len(hand)):
        hand[x][0]=str(hand[x][0])
        if hand[x][0] == '11':
            hand[x][0] = 'J'
        if hand[x][0] == '12':
            hand[x][0] = 'Q'
        if hand[x][0] == '13':
            hand[x][0] = 'K'
        if hand[x][0] == '14':
            hand[x][0] = 'A'

def next_card():
    global yourchips,oppchips
    if len(flop) <= 4:
        add_card()
    else:
        symbol(hand)
        symbol(opphand)
        symbol(flop)
        print("Flop:")
        print_flop()
        print("Your hand:")
        print_hand(hand)
        print("Opponents hand:")
        print_hand(opphand)
        desymbol(hand)
        desymbol(opphand)
        desymbol(flop)
        #Debug
        #print("Your Strength : " + str(val(hand)))
        #print("Opponents Strength : " + str(val(opphand)))
        if val(hand) > val(opphand):
            print("You won!\n\n")
            yourchips += pot
        elif val(hand) < val(opphand):
            print("You lost!\n\n")
            oppchips += pot
        else:
            print("It's a draw!\n\n")
            oppchips += pot/2
            yourchips += pot/2
        flop.append(0)

def desymbol(hand):
    for x in range(len(hand)):
        if hand[x][0]=='J':
            hand[x][0]='11'
        if hand[x][0]=='Q':
            hand[x][0]='12'
        if hand[x][0]=='K':
            hand[x][0]='13'
        if hand[x][0]=='A':
            hand[x][0]='14'
def val(hand):
    power = 0
    straight_check=[]
    types = [0 for x in range(4)]
    if(int(hand[0][0])==int(hand[1][0])):
        power=100+int(hand[0][0])
    for x in range(2):
        straight_check.append(int(hand[x][0]))
        types[int(hand[x][1])]+=1
        hand[x][0]=int(hand[x][0])
        if hand[x][0]>=power:
            power=hand[x][0]
        addon=100
        for y in range(len(flop)):
            flop[y][0]=int(flop[y][0])
            if x==0:
                straight_check.append(flop[y][0])
                types[int(flop[y][1])]+=1
            if hand[x][0] == flop[y][0]:
                if power<100:
                    power=0
                power += hand[x][0]+addon
                addon+=200
    for x in range(len(flop)-2):
        if straight_check[x]==straight_check[x+1]+1==straight_check[x+2]+2==straight_check[x+3]+3==straight_check[x+4]+4:
            power=250+straight_check[x+4]
    for x in range(4):
        if types[x]>=5:
            if power<=500:
                if 300>=power>=250:
                    power+=10000
                else:
                    power=500
                    print("Flush!")
                    max = 0
                    for z in range(2):
                        if hand[z][1]==x:
                            if hand[z][0]>max:
                                max=hand[z][0]
                    power+=max
    return power

if __name__ == '__main__':
    print("Rules:\nIn order to check write 'c'\nIn order to raise write 'r amount', i.e 'r 25'")
    initialize()
    while 1:
        if yourchips<=0:
            print("You lost the game!")
            break
        if oppchips<=0:
            print("You won the game!")
            break
        blind+=20
        if blind>yourchips:
            blind = yourchips
        if blind>oppchips:
            blind = oppchips
        deck2 = copy.copy(deck)
        flop.clear()
        for x in range(2):
            y = random.randint(0,len(deck2)-1)
            what = deck2[y].split(" ")
            hand[x][0]=what[0]
            hand[x][1] = what[1]
            deck2.pop(y)
        for x in range(2):
            y = random.randint(0,len(deck2)-1)
            what = deck2[y].split(" ")
            opphand[x][0]=what[0]
            opphand[x][1] = what[1]
            deck2.pop(y)
        create_flop()
        yourchips -= blind
        oppchips -= blind
        pot = blind * 2
        while 1:
            print("\n")
            show_info()
            print("Input command:")
            if done==0:
                do = input()
            else:
                done=0
                do="c"
            if do.__contains__("c"):
                dice = random.randint(0,100)
                if dice+(len(flop)-3)*5<=raise_willingness+unraised+5 and oppchips>0:
                    unraised=0
                    desymbol(opphand)
                    desymbol(flop)
                    oppval = val(opphand)
                    riseamm = oppval*random.randrange(40,300)/100.0
                    riseamm = round(riseamm)
                    if riseamm>yourchips :
                        riseamm = yourchips
                    if riseamm>oppchips:
                        riseamm= oppchips
                    oppchips-=riseamm
                    pot+=riseamm
                    print("I raise by ",riseamm," chips!")
                    print("\nCall? [y/n]")
                    co = input()
                    if(co.__contains__("n")):
                        oppchips+=pot
                        break
                    else:
                        yourchips-=riseamm
                        next_card()
                        if len(flop) >= 6:
                            break
                else:
                    unraised+=1
                    next_card()
                    if len(flop)>=6:
                        break
            elif do.__contains__("r"):
                vals = do.split(" ")
                desymbol(opphand)
                desymbol(flop)
                oppval = val(opphand)
                pot+=int(vals[1])
                yourchips-=int(vals[1])
                rando = random.randint(0,100)
                if (oppval>=10 or bluff_counter>=3) and (int(vals[1])<=call_range*oppval+bluff_counter*bluff_multiplier or rando<=bravery):
                    print("I call!")
                    done=1
                    oppchips-=int(vals[1])
                    pot+=int(vals[1])
                else:
                    print("Fine, I fold.")
                    bluff_counter+=1
                    yourchips+=pot
                    break
                symbol(opphand)
                symbol(flop)


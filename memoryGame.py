# @Sheeye
# D = 31.08.2022
# Game for training working memory, remember the symbol and type [Y/N] if the symbol appeared 3 steps ago

import random
import time

emotes = ["💩","🎃","🧠","💋","👑","💍","🤘","⌚","⚔️","✉️","🧬","🦠","❤️","⚖️","❄️","🧲","⚽️","🏈","🎾","🏐","🏹","🎸","🎮","🚗","👿"]
working_Array = []
steps = 3
generate = 10
emotesnr = 10
clear = "\n"*1000
cheat = []

def begin():
    for i in range(steps):
        x = random.randint(0,emotesnr)
        print(emotes[x])
        working_Array.append(emotes[x])
    for i in range(random.randint(1,4)):
        cheat.append(random.randint(0,generate))
    cheat.append(10000)
    cheat.sort()

if __name__ == '__main__':
    start = time.time()
    begin()
    while generate>0:
        x = random.randint(0, emotesnr)
        if generate==cheat[0]:
            #print("cheated")
            print(working_Array[0])
            working_Array.append(working_Array[0])
            cheat.pop(0)
        else:
            print(emotes[x])
            working_Array.append(emotes[x])
        answer = input().lower()
        if working_Array[len(working_Array)-1]==working_Array[0]:
            if answer=="y":
                print(clear)
                generate-=1
                working_Array.pop(0)
            else:
                print("Wrong, you lost!")
                break
        else:
            if answer == "n":
                print(clear)
                generate -= 1
                working_Array.pop(0)
            else:
                print("Wrong, you lost!")
                break
    end = time.time()
    elapse = end - start
    if generate<=0:
        print("Congratulations, you won in ",elapse," seconds!")


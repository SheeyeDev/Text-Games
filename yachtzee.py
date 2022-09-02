# @Sheeye
# D = 02.09.2022

import random

scores = ["X" for i in range(15)]
total = 0
grandTotal = 0

def print_scores():
    print("")
    print("1. Ace : ",scores[0])
    print("2. Twos : ", scores[1])
    print("3. Threes : ", scores[2])
    print("4. Fours : ", scores[3])
    print("5. Fives : ", scores[4])
    print("6. Sixes : ", scores[5])
    print("Bonus : ", scores[13]," (",total,"/ 63 )")
    print("7. 3 of a kind : ", scores[6])
    print("8. 4 of a kind : ", scores[7])
    print("9. Full house : ", scores[8])
    print("10. Small straight : ", scores[9])
    print("11. Large straight : ", scores[10])
    print("12. Yahtzee : ", scores[11])
    print("13. Chance : ", scores[12])
    print("Grand total : : ", grandTotal)

if __name__ == '__main__':
    scores[13]=0
    turn = 0
    while turn<=12:
        print("\n" * 1000)
        turn+=1
        dice=[0 for i in range(5)]
        for x in range(5):
            dice[x]=random.randint(1,6)
        print(dice)
        print_scores()
        reroll_nr=3
        while(reroll_nr>=1):
            print("Type dice nr to reroll seperated by space, or X to exit.", reroll_nr, "rerolls remain.")
            choice = input().lower()
            if choice=="x":
                reroll_nr=0
            else:
                reroll_those=choice.split(" ")
                for x in range(len(reroll_those)):
                    i = ord(reroll_those[x])-49
                    dice[i] = random.randint(1, 6)
                print(dice)
                print_scores()
                reroll_nr-=1
        print("Where to input dice? [type 1-13]")
        place=0
        choice = input().lower()
        for i in range(len(choice)):
            place+=(ord(choice[len(choice)-1-i])-48)*pow(10,i)
        toadd=0
        place-=1
        if place <= 5:
            for x in range(5):
                if dice[x]==place+1:
                    toadd+=place+1
            total+=toadd
            if scores[13]==0 and total>=64:
                scores[13]=35
                grandTotal+=35
        if place==12:
            for x in range(5):
                toadd+=dice[x]
        if place==11:
            dice.sort()
            if dice[0]==dice[4]:
                toadd=dice[0]*5
        if place>=6 and place <= 7:
            dice.sort()
            for x in range(5):
                if x+(place-4)<=4:
                    if dice[x] == dice[x+(place-4)]:
                        toadd = dice[x] * (place-4)
        if place==8:
            dice.sort()
            if dice[0]==dice[2] and dice[3]==dice[4] and dice[0]!=dice[4]:
                toadd = dice[0]*3+dice[3]*2
            elif dice[0]==dice[1] and dice[2]==dice[4] and dice[0]!=dice[4]:
                toadd = dice[0]*2+dice[3]*3
        if 10>=place>=9:
            dice.sort()
            times=0
            addo=0
            for x in range(5):
                if x>=1:
                    if dice[x]==dice[x-1]+1:
                        if times==0:
                            times=2
                            addo=dice[x]+dice[x-1]
                        else:
                            times+=1
                            addo+=dice[x]
                    if times>=place-6:
                        toadd=addo
                        break
        grandTotal += toadd
        scores[place]=toadd



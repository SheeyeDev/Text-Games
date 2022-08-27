# @Sheeye
# D = 27.08.2022

# Gra Wordle w języku polskim.

import codecs
import random

słowa = []
minLength = 3
maxLength = 4
guesses = []

def Wczytaj_słownik():
    global słowa
    f = codecs.open("Wordle_słownik.txt","r","utf-8")
    s = f.read().replace("\n"," ")
    słowa = s.split(" ")
    for x in range(len(słowa)):
        słowa[x] = słowa[x].lower()
        for i in range(len(słowa[x])):
            if (słowa[x][i]=='='):
                słowa[x] = słowa[x][0:i]
                break

def Wyświetl_Tablice():
    global guesses
    for x in range(len(guesses)):
        for z in range(len(guesses[x])):
            print(guesses[x][z],end=" ")
        print("")

if __name__ == '__main__':
    Wczytaj_słownik()
    słowo = ""
    while True:
        słowo = słowa[random.randint(0,len(słowa)-1)]
        if maxLength>=len(słowo)>=minLength:
            break
    guesses = [["?" for x in range(len(słowo))] for i in range(5)]
    guessnr = 0
    Wyświetl_Tablice()
    print("\n\033[1;34;50mA - \033[0;0mDobra pozycja, dobra litera\n\033[1;33;50mA - \033[0;0mDobra litera, zła pozycja\n\033[1;31;50mA - \033[0;0mZła litera\n\nZacznij zgadywać!")
    while True:
        if guessnr<=4:
            guess = input()
            tempsłowo = słowo
            for x in range(len(słowa)):
                if słowa[x] == guess:
                    done=0
                    for x in range(len(guess)):
                        if słowo[x]==guess[x]:
                            guesses[guessnr][x]="\033[1;34;50m" + guess[x] + '\033[0;0m'
                            lista = list(tempsłowo)
                            lista[x] = ' '
                            tempsłowo=''.join(lista)
                            done+=1
                            if(done==len(słowo)):
                                print("Brawo!\nWygrałeś!")
                        elif tempsłowo.__contains__(guess[x]):
                            tempsłowo = tempsłowo.replace(guess[x],"",1)
                            guesses[guessnr][x] = "\033[1;33;50m" + guess[x] + '\033[0;0m'
                        else:
                            guesses[guessnr][x] = "\033[1;31;50m" + guess[x] + '\033[0;0m'
                    Wyświetl_Tablice()
                    guessnr+=1
                    break
                elif x==len(słowa)-1 or len(guess)!=len(słowo):
                    print("Not a valid guess!")
                    break
        else:
            print("Przegrałeś.")
            print("Poprawna odpowiedź to ",słowo)
            break


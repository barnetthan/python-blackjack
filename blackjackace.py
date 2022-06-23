import random as r, sys, string

#draws a new card
def newcard():
    while True:
        a = r.randint(1,13)
        b = r.randint(1,4)
        ace = False
        if a==1: 
            num = 'A'
            val = 1
            ace = True
        for n in range(2,11):
            if n == a: 
                num = a
                val = n
        if a==11: 
            num = 'J'
            val = 10
        if a==12: 
            num = 'Q'
            val = 10
        if a==13: 
            num = 'K'
            val = 10
        if b==1: suit = '♣'
        if b==2: suit = '♦'
        if b==3: suit = '♥'
        if b==4: suit = '♠'
        if suit + ' '+str(num) in usedcards: continue
        return([suit + ' '+ str(num) +' ', val, ace])

print ('Welcome to the game of Blackjack! Your goal is to get closer to 21 than the dealer without going over!')
answer = input('Type \"play\" to play or anything else to end game: ')
print('')
if answer != 'play':
    print('Ok bye lol')
    sys.exit()
print('Your cards are:')
usedcards = []
acepcount = 0
card1 = newcard()
if card1[2]: acepcount+=1
usedcards.append(card1[0])
card2 = newcard()
if card2[2]: acepcount+=1
usedcards.append(card2[0])
val1 = card1[1]
val2 = card2[1]
ptotal = val1+val2
currentcards = card1[0]+card2[0]
print(currentcards)
counter = 2
if acepcount>0 and ptotal+10==21:
    print('BLACKJACK! YOU GOT 21! YOU WIN!!!')
    sys.exit()
while True:
    dec = input('Would you like to hit or stand? ')
    print('')
    if dec == 'hit':
        print('Your cards are now: ')
        nextcard = newcard()
        if nextcard[2]: acepcount+=1
        usedcards.append(nextcard[0])
        ptotal += nextcard[1]
        currentcards = currentcards + nextcard[0]
        print(currentcards)
        print('')
        counter+=1
        if ptotal > 21: 
            print('YOU BUSTED, YOU LOSE!!!!')
        elif ptotal == 21:
            print('BLACKJACK! YOU GOT 21! YOU WIN!!!')
        else:
            continue
        break
    elif dec == 'stand':
        dtotal = 0
        print ('Your hand: ')
        print(currentcards)
        print('')
        print ('Dealer\'s hand: ')
        dcounter = 0
        acedcount = 0
        while dtotal<17 and dcounter<counter:
            acard = newcard()
            if acard[2]: acedcount+=1
            usedcards.append(acard[0])
            dtotal += acard[1]
            print(acard[0], end="")
            dcounter+=1
        print('\n')
        if acepcount>0 and ptotal+10<=21:
            ptotal+=10
        if acedcount>0 and dtotal+10<=21:
            dtotal+=10
        if dtotal > 21: print('The dealer went over 21 and busted! You win!!!')
        elif ptotal == dtotal: print("You tied with the dealer! You both have "+str(ptotal)+"!!")
        elif ptotal > dtotal: print("You win!! You were closer to 21 than the dealer!")
        elif ptotal < dtotal: print("You lose!! You were farther from 21 than the dealer!")
        break
    print("ur actually dumb pick a valid choice smh")
    continue





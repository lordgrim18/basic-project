import random

class Outputs():

    def winner(self):
        print("CONGRATS!!\nThe player has guessed correctly")
        
    def loser(self):
        print("GAME OVER!!\nAll chances have been used up")
        

    def high(self):
        print("WRONG GUESS!! Too high")
        

    def low(self):
        print("WRONG GUESS!! Too low")
        

o=Outputs()

def guess_user(x):
    n=random.randint(1,x)
    g=0
    i=1
    while(i<=5):
        print(f'chance number {i}')
        g=int(input(f'Guess a number (1-{x}) :'))
        if g not in range(1,x+1):
            print("Invalid Input")
        else:
            if g==n:
                o.winner()
                break
            elif g<n:
                o.low()
                i++
            elif g>n:
                o.high()
                i++
   if i==6:
        o.loser()
        
    
def guess_comp(x):
    low=1
    high=x
    i=0
    while (i<=5):
        print(f'chance number {i}')
        n=random.randint(low,high)
        print(f"the guess is {n}")
        l=['c','h','l']
        a=input("is the guess correct(C) or low(L) or high(H): ").lower()
        if a==l[0]:
            o.winner()
            break
        elif a==l[1]:
            o.high()
            high=n-1
            i++
        elif a==l[2]:
            o.low()
            low=n+1
            i++
    if i==6:
        o.loser()
        

def select(x):
    a=input("who do u want the player(guesser) to be - user(U) or system(S): ").lower()
    return a
    

def game():
    print("\n","-"*5,"WELCOME TO THE GUESSING GAME","-"*5,"\nThe player has 5 chances to guess\n")
    c='y'
    while c!='n':
        a=int(input("Enter the number range of the game: "))
        b=select(a)
        print("\nLET THE GAME BEGIN")
        if b=='u':
            guess_user(a)
        elif b=='s':
            guess_comp(a)
        c=input("\nDo u want to continue the game - yes(y) or no(n): ").lower() 
    print("THANKS FOR PLAYING\nSEE YOU LATER")
       
game()

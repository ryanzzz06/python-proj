from random import randint
def shell_game():
    L=["A","B","C"]
    print("The player must guess which of the three shells (A, B, or C) hides the key. They have two attempts to find it. On each attempt, the key is randomly placed under one of the shells")
    print(L)
    at=2
    found=False
    while at>0 and found==False:
        let=L[randint(0,len(L)-1)]
        print("number of attempts left: ",at)
        ans=input("choose a shell").upper()
        if ans==let:
            found=True
            return found
        elif ans not in L:
            print("choice is invalid")
        at=at-1
    print("you have lost, the key was under shell ", let)
    return found

def roll_dice_game():
    att=3
    found=False
    while att>0 and found==False:
        print("number of attempts left: ",att)
        input("Press 'Enter' to roll the dice...")
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        T=(dice1, dice2)
        print ("the values you obtained were: ", T)
        if 6 in T:
            print("you have won the game and a key")
            found=True
            return True
        else:
            d1 = randint(1, 6)
            d2 = randint(1, 6)
            T2 = (d1, d2)
            print ("the values the game master obtained were: ", T2)
            if 6 in T2:
                print("the game master has won the game")
                found=True
                return False
        att=att-1
        print("we are moving on to the next attempt")
    if found==False:
        print("No player has scored a 6 after three attempts so the result is a draw")
        return False
def chance_challenge():
    challenges=[shell_game,roll_dice_game]
    challenge=challenges[randint(0,len(challenges)-1)]
    challenge()
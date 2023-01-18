import random

while True:
    player=input("rock/paper/scissors?: ")
    computer=random.choice(['rock','paper','scissors'])
    if player==computer:
        print("It's a tie!")
    elif player=="rock":
        if computer=="paper":
            print("You lose!, paper covers rock")
        else:
            print("You win!, rock smashes scissors")
    elif player=="paper":
        if computer=="scissors":
            print("You lose!, scissors cuts paper")
        else:
            print("You win!, paper covers rock")
    elif player=="scissors":
        if computer=="rock":
            print("You lose!, rock smashes scissors")
        else:
            print("You win!, scissors cuts paper")
    else:
        print("Check Your Spelling bruv")
        
    
        

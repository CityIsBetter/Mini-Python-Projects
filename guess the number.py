import random

while True:
    num=random.randint(1,100)
    print("A guess a number between 1 and 100, you will have 5 chances")
    chance=1
    correct=0 
    while chance<=5:
        player=int(input("The number u guessed:"))
        if player==num:
            print("You guessed the number correctly")
            print("-----x-----x-----x-----x-----x-----x-----x----x-----")
            correct=1
            chance=0
        elif player>num:
            print("The number you have guessed is more than the actual number")
            print("You have",5-chance,"chances remaining")
        elif player<num:
            print("The number you have guessed is less than the actual number")
            print("You have",5-chance,"chances remaining")
        chance+=1
        if chance==6 and correct==0:
            print("You failed, the correct number is", num)
            print("-----x-----x-----x-----x-----x-----x-----x----x-----")

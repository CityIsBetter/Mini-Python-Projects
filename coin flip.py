import random

while True:
    computer=random.choice(['heads','tails'])
    player=input("Heads or Tails: ")
    if player==computer:
        print("You win")
    else:
        print("You lose")

import random

while True:
    mode=int(input("Enter the number of dice you want to play with(1 or 2):"))
    c1=random.choice([1,6])
    c2=random.choice([1,6])
    p1=random.choice([1,6])
    p2=random.choice([1,6])
    if mode==1:
        ready=input("READY!!, 'yes' or 'no': ")
        if ready=='yes':
            print("You throw your dice... and you get",p1)
            print("Opponent throws their dice... and gets",c1)
            if p1>c1:
                print("You WIN!!!!!!")
            elif p1<c1:
                print("You lose...")
            else:
                print("It's a TIE!!")
            print("-----x-----x-----x-----x----x-----x-----")
    if mode==2:
        ready=input("READY!!, 'yes' or 'no': ")
        if ready=='yes':
            print("You throw your dice... and you get",p1,"and",p2)
            print("Opponent throws their dice... and gets",c1,"and",c2)
            pt=p1+p2
            ct=c1+c2
            if pt>ct:
                print("You WIN!!!!!!")
            elif pt<ct:
                print("You lose...")
            else:
                print("It's a TIE!!")
            print("-----x-----x-----x-----x----x-----x-----")

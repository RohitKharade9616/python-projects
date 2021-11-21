import random
print("s.snake w.water g.gun")
n=int(input("enter no of rounds:\n"))
options=["s","w","g"]
rounds=1
userwin=0
compwin=0
while rounds <= n:
    print(rounds)
    player=input("choose your options\n")
    comp=random.choice(options)
    if comp==player:
        print("game draw")
    if comp=="s":
        if player=="w":
            compwin+=1
        elif player=="g":
            userwin+=1
    elif comp=="w":
        if player=="g":
            compwin+=1
        elif player=="s":
            userwin+=1
    elif comp=="g":
        if player=="s":
            compwin+=1
        elif player=="w":
            userwin+=1
    print(comp)
    if userwin>compwin:
         print("you win in round",rounds)
    else:
         print("you lose in round",rounds)
    rounds+=1
    if userwin>compwin:
        print("congratulations!!you win")
    elif userwin<compwin:
        print("you lose!")
    else:
        print("game draw")


import random
n=random.randint(1,100)
attempts=1
while(attempts<100):
    guessno=int(input("guess the number between 1-100\n"))
    if(guessno>n):
        print("lower no please!")
    elif(guessno<n):
        print("heigher no please!")
    else:
        print(f"you can guess the no in {attempts}")
        break
    attempts=attempts+1
print("game over!")
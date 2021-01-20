import random
number = random.randint(1,9)
print("enter a number")
chances = 0
while chances<5 :
    guess = int(input("Enter your guess "))
    if guess==number:
        print("Congrtulations you won")
        break
    elif guess<number:
        print("enter larger number")
    else:
        print ("guess a lower number")
    chances +=1
if not chances<5:
    print("you lost the number was",number)

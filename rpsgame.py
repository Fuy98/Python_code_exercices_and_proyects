import random

myList = ["r", "p", "s"]
print(myList)

#Your choice
my_choice = input("What is your choice? ")

#Computer selection
random_c = random.choice(myList)
print(random_c)

if my_choice == myList[0]: #r
    if random_c == myList[0]:
        print("Its a Tie")
    elif random_c == myList[2]:
        print("You win and the computer loses")
    elif random_c == myList[1]:
        print("You lose and the computer wins")

if my_choice == myList[1]: #p
    if random_c == myList[0]:
        print("You win and the computer loses")
    elif random_c == myList[2]:
        print("You lose and the computer wins")
    elif random_c == myList[1]:
        print("Its a Tie")

if my_choice == myList[2]:#s
    if random_c == myList[0]:
        print("You lose and the computer wins")
    elif random_c == myList[2]:
        print("Its a Tie")
    elif random_c == myList[1]:
        print("You win and the computer loses")

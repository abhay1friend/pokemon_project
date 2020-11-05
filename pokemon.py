import random
from time import sleep
#"Charmander"=Fire, "Squirtle"=water "Bulbasur"=Trees]
choices = ["Charmander", "Squirtle", "Bulbasur"]

computer = random.choice(choices)
#print(computer)
player = False

name = input("hello, please enter you name:  ")

while player == False:
    print(f"hello, {name} Wecome to Pokemon battles Game.. !!")
    player = input("Which pokemon do you want to choose?\n'Charmander': 'Charmander'\n'Squirtle': 'Squirtle'\n'Bulbasur': 'Bulbasur'\n'Stop the game': 'Stop': ")
    if player == computer:
        print ("Tie..!!")
    elif player == "Charmander":
        if computer == "Squirtle":
            print("\nPlease wait, we are loding results....")
            sleep(2)
            print ("You Losse..!!")
        else:
            print ("You Win..!!")
    elif player == "Squirtle":
        if computer == "Bulbasur":
            print("\nPlease wait, we are loding results....")
            sleep(2)
            print("You Losse..!!")
        else:
            print("You Win..!!")
    elif player == "Bulbasur":
        if computer == "Charmander":
            print("\nPlease wait, we are loding results....")
            sleep(2)
            print("You Losse..!!")
        else:
            print("You Win..!!")
    elif player == "Stop":
        print ("Thanks for playing..!!")
        break
    else:
        print("Thats not a valid play..!1")
        break

    player = False



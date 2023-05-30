import random
from simple_colors import *
print(cyan("Hey Choras and choris wellcome to Saaap Paaani Banduuk game", ['bright', 'italic']))
print(red("you will have 10 chances to defeat the bot" ,['underlined']))
print(magenta("you will use only *s* *w* *g*" , ['bold'] ))
print(blue("where s is snak w, is water and g is gun" , ['bold' ,'italic' , 'bright' , 'underlined' ]))

lis = ["s","w","g"]
ran = random.choice(lis)
attempt = 1
computer_point = 0
your_point = 0

while(attempt <=10):
    inp = input("Choose between S , W , G  = ")
    inp = inp.lower()
    if inp == ran:
        print("tie")
        print(f"you choose {inp} and computer choose {ran}")
        print("Nobody gets point \n")

    elif inp == "s" and ran == "g":
        computer_point = computer_point + 1
        print(f"you choose {inp} and computer choose {ran}")
        print("you lost the round")
        print("computer get 1 point \n")

    elif inp == "s" and ran == "w":
        your_point = your_point + 1
        print(f"you choose {inp} and computer choose {ran}")
        print("you win the round")
        print("you get 1 point \n")



    elif inp == "g" and ran == "s":
        your_point = your_point + 1
        print(f"you choose {inp} and computer choose {ran}")
        print("you win the round")
        print("you get 1 point \n")

    elif inp == "g" and ran == "w":
        computer_point = computer_point + 1
        print(f"you choose {inp} and computer choose {ran}")
        print("you lost the round")
        print("computer get 1 point \n")



    elif inp == "w" and ran == "g":
        your_point = your_point + 1
        print(f"you choose {inp} and computer choose {ran}")
        print("you win the round")
        print("you get 1 point \n")


    elif inp == "w" and ran == "s":
        computer_point = computer_point + 1
        print(f"you choose {inp} and computer choose {ran}")
        print("you lost the round")
        print("computer get 1 point \n")

    else:
        print("Invalid Input")

    print("Number of gueses left = " ,format(10-attempt))
    attempt = attempt + 1
    if(attempt>10):
        print("Game Over!")


print(f"Your point : {your_point}\ncomputer's Point : {computer_point}")
if computer_point> your_point:
    print("Computer win and You lose!")

elif computer_point< your_point:
    print("You win and Computer lose!")

else:
    print("Tie!")
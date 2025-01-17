import random
game=["rock","paper","scissors"]
user_choice=int(input("What do u choose?Type 0 for Rock,Type 1 for Paper,Type 2 for Scissors"))
print(game[user_choice])
computer_choice=random.randint(0,2)
print(f"Computer choice:")
print(game[computer_choice])
if user_choice>=3 or user_choice<0:
    print("Invalid number.You lose")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice==0 and user_choice==2:
    print("You lose")
elif user_choice>computer_choice:
    print("You won")
elif computer_choice>user_choice:
    print("You lose")
elif computer_choice==user_choice:
    print("Its draw")


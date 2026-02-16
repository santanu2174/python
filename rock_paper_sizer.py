"""
WORKFLOW OF PROJECT:
1. Input from user(Rock, Paper, Sizer)
2. computer choice (Computer will choose randomly)
3. Result print

Cases:
A - Rock
Rock - Rock = tie
Rock - Paper = Paper wins
Rock - Sizer = Rock wins

B - Paper
Paper - Rock = Paper wins
Paper - Paper = tie
Paper - Sizer = Sizer wins

C - Sizer
Sizer - Rock = Rock wins
Sizer - Paper = Sizer wins
Sizer - Sizer = tie

"""

import random

item_list = ["Rock", "Paper", "Sizer"]

user_choice = input("Enter your choice (Rock/Paper/Sizer) = ")
computer_choice = random.choice(item_list)

print(f"User choice = {user_choice}")
print(f"Computer choice = {computer_choice}")

# if user_choice == computer_choice:
#     print("Tie")
# elif user_choice == "Rock" and computer_choice == "Paper":
#     print("Computer wins")
# elif user_choice == "Rock" and computer_choice == "Sizer":
#     print("User wins")
# elif user_choice == "Paper" and computer_choice == "Rock":
#     print("User wins")
# elif user_choice == "Paper" and computer_choice == "Sizer":
#     print("Computer wins")
# elif user_choice == "Sizer" and computer_choice == "Rock":
#     print("Computer wins")
# elif user_choice == "Sizer" and computer_choice == "Paper":
#     print("User wins")
# else:
#     print("Invalid choice")


if user_choice == computer_choice:
    print("Tie")
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Computer wins")
    else:
        print("User wins")
elif user_choice == "Paper":
    if computer_choice == "Rock":
        print("user wins")
    else:
        print("computer wins")
elif user_choice == "Sizer":
    if computer_choice == "Rock":
        print("computer wins")
    else:
        print("user wins")
else:
    print("Invalid choice")


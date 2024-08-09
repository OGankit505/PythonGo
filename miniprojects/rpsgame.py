import sys
import random

print("          Welcome to Rock, Paper, Scissors Game!             ")
print("------------------------------------------------------------")

playerchoice = input("Enter your choice (1 for rock 2 for paper 3 for scissors): ")
player=int(playerchoice)

computerchoice = random.choice("123")
computer = int(computerchoice)
print("")

print("Player chooses ", player)
print("Computer chooses ", computer)
print("")

# ladder if else
if player == 1:
    if computer ==2:
        print("Computer wins!")
    elif computer == 3:
        print("Player wins!")
    else:
        print("It's a tie!")
elif player == 2:
    if computer == 1:
        print("Player wins!")
    elif computer == 3:
        print("Computer wins!")
    else:
        print("It's a tie!")
elif player == 3:
    if computer == 1:
        print("Computer wins!")
    elif computer == 2:
        print("Player wins!")
    else:
        print("It's a tie!")


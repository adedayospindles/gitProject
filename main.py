# Rock paper Scissors game between user and computer 

import random

user_wins  = 0
computer_wins  = 0
tie = 0

options = ["R", "P", "S"]

while True:
    
    user_input = input("Type R for Rock/ P for Paper/ S for Scissors or Q to quit: ").upper()

    if user_input == "Q":
        break
    elif user_input not in options:
        print("Invalid input! Please try again!!")
        continue

    # random_number = random.randint(0,2)
    # random_number = random.choice(options)
    # rock: R, paper: P, scissors: S

    # Generate Computer move
    computer_pick = random.choice(options)

    # Print computer move
    print("Computer picked", computer_pick + ".")

    # User move
    if user_input == "R" and computer_pick == "S":
        print("Player picked", user_input + ".")
        print("You won!")
        user_wins += 1

    elif user_input == "R" and computer_pick == "P":
        print("Player picked", user_input + ".")
        print("Computer won!")
        computer_wins += 1

    elif user_input == "P" and computer_pick == "R":
        print("Player picked", user_input + ".")
        print("You won!")
        user_wins += 1
    
    elif user_input == "P" and computer_pick == "S":
        print("Player picked", user_input + ".")
        print("Computer won!")
        computer_wins += 1

    elif user_input == "S" and computer_pick == "P":
        print("Player picked", user_input + ".")
        print("You won!")
        user_wins += 1
    
    elif user_input == "S" and computer_pick == "R":
        print("Player picked", user_input + ".")
        print("Computer won!")
        computer_wins += 1

    else:
        print("Player & computer picked", computer_pick, ". It's a draw, Play again!")
        tie += 1

print("You won", user_wins, 'times.')
print("The computer won", computer_wins, "times.")
print("Player & computer drew", tie, "times.")
print("Goodbye")